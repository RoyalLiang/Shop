from fileinput import filename

import xlwt
from django.contrib import admin
from django.db.models import Count, Sum, Aggregate, StdDev, Variance
from django.db.models.functions import Trunc
from django.http import StreamingHttpResponse, HttpResponse
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.


@admin.register(Visitor)
class RecordAdmin(ImportExportModelAdmin):
    list_display = ['all_time', 'user_agent', 'all_time', 'pub_ip', 'address']
    list_filter = ['user_agent', 'address', 'pub_ip']


@admin.register(DeviceByDayModel)
class DeviceByDayAdmin(ImportExportModelAdmin):
    change_list_template = 'admin/device_by_day.html'
    list_filter = ['date']
    search_fields = ['date']

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'days': Sum('date'),
            'pc_count': Sum('pc_count'),
            'mobile_count': Sum('mobile_count'),

        }
        response.context_data['date'] = list(
            qs
                .values('date')
                .annotate(**metrics)
        )

        return response


@admin.register(RegionByDay)
class RegionByDayAdmin(ImportExportModelAdmin):
    # change_list_template = 'admin/refer_by_day.html'
    list_filter = ['date']
    search_fields = ['date']
    list_display = ['date', 'region', 'views_count']


@admin.register(ViewsByDayModel)
class ViewsByDayAdmin(ImportExportModelAdmin):
    list_filter = (
        'date',
    )
    change_list_template = 'admin/admin_test.html'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'days': Sum('date'),
            'views_count': Sum('views_count'),
            'ip_count': Sum('ip_count'),

        }
        response.context_data['date'] = list(
            qs
                .values('date')
                .annotate(**metrics)
        )

        return response


@admin.register(ReferByDayModel)
class ReferByDayModelAdmin(ImportExportModelAdmin):
    change_list_template = 'admin/refer_by_day.html'
    list_filter = ['date']
    search_fields = ['date']
    list_per_page = 1

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context
        )

        try:
            qs = response.context_data['cl'].queryset
        except (AttributeError, KeyError):
            return response

        metrics = {
            'days': Sum('date'),
            'search_engine_count': Sum('search_engine_count'),
            'website_in_count': Sum('website_in_count'),
            'other_count': Sum('other_count'),
            'input_count': Sum('input_count'),

        }
        response.context_data['date'] = list(
            qs
                .values('date')
                .annotate(**metrics)
                .order_by('date')
        )

        return response
