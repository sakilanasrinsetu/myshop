from django.db import models
from oscar.apps.partner.abstract_models import AbstractPartner
from oscar.models.fields.slugfield import SlugField
from django.utils.translation import gettext_lazy as _

class PartnerType(models.Model):
    name = models.CharField(max_length=50)
    slug = SlugField(_('Slug'), max_length=255, db_index=True)
    

class Partner(AbstractPartner):
    partner_type = models.ForeignKey(PartnerType, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='partners'
    )


from oscar.apps.partner.models import *  # noqa isort:skip


