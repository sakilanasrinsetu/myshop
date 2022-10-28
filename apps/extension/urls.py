from django.urls import path

from .views import *

urlpatterns = [
    path('new_category/',
         NewCategoryViewSet.as_view({'get': 'list','post': 'create',
                                    'delete':'destroy'},
                                 name='new_category')),

    path('new_category/<pk>/',
         NewCategoryViewSet.as_view({'patch': 'update','put': 'update',
                                    'get':'retrieve'},
                                 name='new_category')),                            

]