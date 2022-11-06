from django.urls import re_path, path
from oscar.core.loading import get_class
from .views import *

# InvoicePreviewView = get_class("oscar_invoices.views", "InvoicePreviewView")


app_name = "oscar_invoices"
urlpatterns = [
    # re_path(r"/(?P<pk>\d+)/", InvoicePreviewView.as_view(), name="invoice"),
    path('/view', InvoiceListAPIView.as_view(), name="invoice"),
    path('/view/<int:pk>', InvoiceDetailAPIView.as_view(), name="invoice"),
    # path("/<int:pk>/", InvoicePreviewView.as_view(), name="invoice"),
]
