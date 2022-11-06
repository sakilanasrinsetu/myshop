from django.urls import re_path
from oscar.core.loading import get_class
from .views import InvoicePreviewView, InvoiceAPIView

# InvoicePreviewView = get_class("oscar_invoices.views", "InvoicePreviewView")


app_name = "oscar_invoices"
urlpatterns = [
    # re_path(r"/(?P<pk>\d+)/", InvoicePreviewView.as_view(), name="invoice"),
    path("invoice/", InvoiceAPIView.as_view(), name="invoice-api"),
    path("/<int:pk>/", InvoicePreviewView.as_view(), name="invoice"),


]
