
from rest_framework import serializers
from oscarapi.serializers import product
from oscarapi.views import product as product_view
from oscarapi.serializers import checkout
from oscar.apps.partner.models import StockRecord
from oscarapi.serializers.utils import OscarModelSerializer
from oscar.apps.wishlists.models import Line
from apps.order.models import Order
from oscar.apps.basket.models import Basket
from datetime import timedelta
from django.utils import timezone
from extension.serializers import ProductSourceSerializer
from apps.catalogue.models import Category, Product
from django.utils.translation import gettext_lazy as _


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
