from django.urls import path
from .views import TestView
from utils.resource import VisitorResource, RegionByDayResource, DeviceByDayResource, ReferByDayResource, \
    ViewsByDayResource

app_name = 'viewsCount'
urlpatterns = [
    path('visitor-export/', VisitorResource.export_excel, name='visitor_export'),
    path('region-export/', RegionByDayResource.export_excel, name='region_export'),
    path('refer-export/', ReferByDayResource.export_excel, name='refer_export'),
    path('device-export/', DeviceByDayResource.export_excel, name='device_export'),
    path('views-export/', ViewsByDayResource.export_excel, name='views_export'),

]
