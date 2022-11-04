from django.utils.translation import gettext_lazy as _ 
from oscar_accounts import models
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = "__all__"