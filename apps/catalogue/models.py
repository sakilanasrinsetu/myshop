from django.db import models
from django.utils.translation import gettext_lazy as _
from oscar.apps.catalogue.abstract_models import (AbstractProduct,
                                                  AbstractCategory)
from oscar.utils.models import get_image_upload_path

class Product(AbstractProduct):
    short_description = models.TextField(_('Short Description'), blank=True)
    index = models.IntegerField(default=0, blank=True)
    unit = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        ordering = ('index',)

class Category(AbstractCategory):
    thumbnail_image = models.ImageField(
        upload_to=get_image_upload_path, max_length=255, blank=True, null=True)



from oscar.apps.catalogue.models import *  # noqa isort:skip