from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import AccountViewSet

router = DefaultRouter()
router.register("accounts", AccountViewSet, basename="accounts")


urlpatterns = router.urls