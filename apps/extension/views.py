from django.shortcuts import render
from .models import *


from .serializers import ProductLinkSerializer
from oscarapi.views import product
from apps.catalogue.models import Category


# Create your views here.


class ProductList(product.ProductList):
    serializer_class = ProductLinkSerializer

    def get_queryset(self):
        """
        Allow filtering on structure so standalone and parent products can
        be selected separately, eg::

            http://127.0.0.1:8000/api/products/?structure=standalone

        or::

            http://127.0.0.1:8000/api/products/?structure=parent

        allow filtering on category
            http://127.0.0.1:8000/api/products/?category=1
        """
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