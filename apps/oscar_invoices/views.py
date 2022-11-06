from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin
from oscar.core.loading import get_class, get_model
from .serializers import InvoiceSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response


Invoice = get_model('oscar_invoices', 'Invoice')
InvoiceCreator = get_class('oscar_invoices.utils', 'InvoiceCreator')


# class InvoicePreviewView(UserPassesTestMixin, SingleObjectMixin, View):
#     queryset = Invoice.objects.all()

#     def test_func(self):
#         user = self.request.user
#         return user.is_staff

#     def get(self, request, *args, **kwargs):
#         invoice = self.get_object()
#         rendered_invoice = InvoiceCreator().render_document(
#             invoice=invoice,
#             legal_entity=invoice.legal_entity,
#             order=invoice.order,
#             use_path=False,
#             request=request
#         )
#         return HttpResponse(rendered_invoice)


# Invoice API's

class InvoiceListAPIView(generics.ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        queryset = Invoice.objects.all()
        return queryset
    def get(self, request, format=None):
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvoiceDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

    def get(self, request, pk, format=None):
        invoice = self.get_object()
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        invoice = self.get_object()
        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        invoice = self.get_object()
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



