from oscarapi.views import product
from rest_framework.permissions import IsAuthenticated

# from apps.custom.serializers.product import CategorySerializer, ProductLinkSerializer, ProductDetailSerializer, CategoryDetailSerializer
# from oscar.apps.catalogue.models import Category
from apps.catalogue.models import Category


from rest_framework import serializers
from oscarapi.views import product as product_view
from oscarapi.serializers import checkout


class ProductLinkSerializer(product.ProductLinkSerializer):
    price = serializers.SerializerMethodField()
    title = serializers.SerializerMethodField()
    unit = serializers.SerializerMethodField()
    short_description = serializers.SerializerMethodField()

    def get_short_description(self, obj):
        return _(obj.short_description)

    def get_unit(self, obj):
        return _(obj.unit.__str__())

    def get_title(self, obj):
        return _(obj.title)

    def get_price(self, obj):
        strategy = product_view.Selector().strategy(
            request=self.context.get("request"),
            user=self.context.get("request").user)
        ser = checkout.PriceSerializer(
            strategy.fetch_for_product(obj).price,
            context=self.context
        )

        price = ser.data
        price["currency"] = _(price["currency"])
        price["excl_tax"] = _(price["excl_tax"])
        price["incl_tax"] = _(price["incl_tax"])
        price["tax"] = _(price["tax"])

        return price

    class Meta(product.ProductLinkSerializer.Meta):
        fields = [
            "id",
            "title",
            "short_description",
            "images",
            "price",
            'index',
            'unit',
        ]


class ProductList(product.ProductList):
    serializer_class = ProductLinkSerializer

    def get_queryset(self):

        qs = super(ProductList, self).get_queryset()

        structure = self.request.query_params.get("structure")
        if structure is not None:
            return qs.filter(structure=structure)

        category = self.request.query_params.get("category")
        if category is not None:
            category_id_list = [int(category)]
            categories = Category.objects.filter(pk=category).first().get_children()
            for category in categories:
                category_id_list.append(category.pk)
                category_id_list += list(category.get_children().values_list("pk", flat=True))
            return qs.filter(categories__pk__in=category_id_list)

        return qs

