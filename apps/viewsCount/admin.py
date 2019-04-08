from django.contrib import admin
from .models import *
# Register your models here.


class MyAdminSite(admin.AdminSite):
    site_header = '伊特纳(天津)科技发展有限公司后台管理'


class RecordAdmin(admin.ModelAdmin):
    # times = time.localtime('timeIn')
    list_display = ['all_time', 'user_agent', 'time']
    # data_charts = {
    #     "address": {'title': "每日访问时间统计", "x-field": "timeIn", "y-field": ("time", 'user_agent')},
    #     # "url": {'title': "每日访问方式统计", "x-field": "pub_ip", "y-field": ("refer",)},
    #     # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    # }


class ViewsByDayAdmin(admin.ModelAdmin):
    readonly_fields = ['views_count', 'ip_count']
    data_charts = {
        "date": {'title': "每日访问方式统计", "x-field": "date", "y-field": ("views_count", 'ip_count')},
        # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    }


class DeviceByDayAdmin(admin.ModelAdmin):
    # object_list_template = "test.html"
    list_display = ['date', 'pc_count', 'mobile_count']
    data_charts = {
        "test": {'title': "每日访问设备统计", "x-field": "date", "y-field": ("pc_count", 'mobile_count')},
        # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    }


class RegionByDayAdmin(admin.ModelAdmin):
    data_charts = {
        "test": {'title': "每日访问地区统计", "x-field": "date", "y-field": ('views_count',)},
        # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    }


admin_site = MyAdminSite()
admin.site.register(Visitor, RecordAdmin)
# admin.site.register(Visitor, VisitorAdmin)
admin.site.register(ViewsByDay, ViewsByDayAdmin)
# admin.site.register(ViewsByDay, RecordAdmin)
admin.site.register(DeviceByDay, DeviceByDayAdmin)
admin.site.register(RegionByDay, RegionByDayAdmin)