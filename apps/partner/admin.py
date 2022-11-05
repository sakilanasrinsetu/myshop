
from django.contrib import admin
from .models import *



admin.site.register(PartnerType)


from oscar.apps.partner.admin import *  # noqa
