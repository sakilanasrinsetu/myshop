from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponse
from django.views.generic import View
from django.views.generic.detail import SingleObjectMixin
from oscar.core.loading import get_class, get_model
from .serializers import InvoiceSerializer
from rest_framework import generics, status
from rest_framework.views import APIView


Invoice = get_model('oscar_invoices', 'Invoice')
InvoiceCreator = get_class('oscar_invoices.utils', 'InvoiceCreator')


class InvoicePreviewView(UserPassesTestMixin, SingleObjectMixin, View):
    queryset = Invoice.objects.all()

    def test_func(self):
        user = self.request.user
        return user.is_staff

    def get(self, request, *args, **kwargs):
        invoice = self.get_object()
        rendered_invoice = InvoiceCreator().render_document(
            invoice=invoice,
            legal_entity=invoice.legal_entity,
            order=invoice.order,
            use_path=False,
            request=request
        )
        return HttpResponse(rendered_invoice)


# Invoice API's

class InvoiceAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        invoice = Invoice.objects.get(pk=kwargs['pk'])
        serializer = InvoiceSerializer(invoice)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        invoice = Invoice.objects.get(pk=kwargs['pk'])
        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        invoice = Invoice.objects.get(pk=kwargs['pk'])
        invoice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, *args, **kwargs):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        invoice = Invoice.objects.get(pk=kwargs['pk'])
        serializer = InvoiceSerializer(invoice, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





