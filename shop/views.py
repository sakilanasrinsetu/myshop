from django.shortcuts import render

from oscar.apps.partner.models import * 
# from oscar.apps.category.models import * 

from utils.custom_viewset import CustomViewSet

from utils.response_wrapper import ResponseWrapper
from .serializers import *
from .models import *
from django.core.mail import EmailMultiAlternatives
from django.core.mail import send_mail
from datetime import datetime
from django.utils import timezone
import datetime
import random
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework import permissions, status, viewsets
import json

# Create your views here.

class CloudCafeInformationViewSet(CustomViewSet):
    serializer_class = CloudCafeInformationSerializer
    queryset = Partner.objects.all()
    lookup_field = 'pk'
    
    def cloud_cafe_information_details(self, request, *args, **kwargs):
        cloud_cafe_information_qs = CloudCafeInformation.objects.all().last()
        if not cloud_cafe_information_qs:
            return ResponseWrapper(error_msg='cloud cafe information Details Not Found', status=400)
        serializer = CloudCafeInformationSerializer(instance=cloud_cafe_information_qs)
        return ResponseWrapper(data=serializer.data, status=200)   
