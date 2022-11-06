from rest_framework import serializers
from oscar.core.loading import get_class, get_model

Invoice = get_model('oscar_invoices', 'Invoice')
InvoiceCreator = get_class('oscar_invoices.utils', 'InvoiceCreator')

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['invoice'] = InvoiceCreator().render_document(
            invoice=instance,
            legal_entity=instance.legal_entity,
            order=instance.order,
            use_path=False,
            request=self.context['request']
        )
        return data


