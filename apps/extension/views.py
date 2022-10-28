from django.shortcuts import render
from .models import *
from apps.catalogue.models import Category, Product

from .serializers import *

from utils.custom_viewset import CustomViewSet
from utils.response_wrapper import ResponseWrapper


# Create your views here.


class NewCategoryViewSet(CustomViewSet):
    serializer_class = NewCategorySerializer
    queryset = Category.objects.all()
    lookup_field = 'pk'