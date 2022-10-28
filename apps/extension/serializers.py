from asyncore import read
from dataclasses import field, fields
from .models import *
from rest_framework import serializers

from apps.catalogue.models import Category, Product

# ..........***.......... Category ..........***..........

class NewCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'