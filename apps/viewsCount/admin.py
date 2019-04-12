from fileinput import filename

import xlwt
from django.contrib import admin
from django.db.models import Count, Sum, DateTimeField, Min, Max, DateField
from django.db.models.functions import Trunc
from django.http import StreamingHttpResponse

from .models import *


# Register your models here.


# class MyAdminSite(admin.AdminSite):
#     site_header = '伊特纳(天津)科技发展有限公司后台管理'


class RecordAdmin(admin.ModelAdmin):
    # times = time.localtime('timeIn')
    list_display = ['all_time', 'user_agent', 'time']
    actions = ["saveexecl"]  # 自定义的action（导出到excel表格）
    search_fields = ('user_agent', 'all_time')  # 可以搜索的字段

    list_per_page = 500  # 每页显示500条，太多了可能会出现服务器崩掉的情况

    def saveexecl(self, request, queryset):
        Begin = xlwt.Workbook()
        sheet = Begin.add_sheet("response")
        cols = 0
        for query in queryset:
            # you need write colms                     # 好像有个方法可以一次性写入所有列，记不清了，只能用这种简单的方法去实现
            sheet.write(cols, 1, str(query.idfa))  # 写入第一列
            sheet.write(cols, 2, str(query.day_time))  # 写入第二列
            sheet.write(cols, 3, str(query.keyword))  # 写入第三列
            cols += 1
        Begin.save("%s" % (filename))

        def file_iterator(filename, chuck_size=512):
            with open(filename, "rb") as f:
                while True:
                    c = f.read(chuck_size)
                    if c:
                        yield c
                    else:
                        break

        response = StreamingHttpResponse(file_iterator(filename))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{}"'.format("result.xls")
        return response

    saveexecl.short_description = "导出Excel"  # 按钮显示名字
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


@admin.register(TestModel)
class TestAdmin(admin.ModelAdmin):
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
            'day': Sum('date'),
            'views_count': Sum('views_count'),
            'ip_count': Sum('ip_count'),

        }
        response.context_data['date'] = list(
            qs
                .values('date')
                .annotate(**metrics)
        )

        views_by_day = qs.annotate(
            period=Trunc(
                'date',
                'date',
                output_field=DateField(),
            ),
        ).values('views_count').annotate(total=Sum('views_count'))

        views_range = views_by_day.aggregate(
            low=Min('total'),
            high=Max('total'),
        )
        high = views_range.get('high', 0)
        low = views_range.get('low', 0)
        response.context_data['views_by_day'] = [{
            'date': x['date'],
            'total': x['total'] or 0,
            'pct': \
                ((x['total'] or 0) - low / (high - low) * 100)
                if high > low else 0,
        } for x in views_by_day]

        return response


# admin_site = MyAdminSite()
admin.site.register(Visitor, RecordAdmin)
# admin.site.register(Visitor, VisitorAdmin)
admin.site.register(ViewsByDay, ViewsByDayAdmin)
# admin.site.register(ViewsByDay, RecordAdmin)
admin.site.register(DeviceByDay, DeviceByDayAdmin)
admin.site.register(RegionByDay, RegionByDayAdmin)
