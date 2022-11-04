from oscar_accounts import models
from rest_framework.response import Response

from utils import custom_viewset
from .serializers import AccountSerializer

class AccountViewSet(custom_viewset.CustomViewSet):
    queryset = models.Account.objects.all()
    serializer_class = AccountSerializer