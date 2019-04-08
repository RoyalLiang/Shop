import time
import xadmin
from xadmin.views import ModelAdminView
from .models import *
from xadmin import views


class GlobalSettings:
    site_title = '伊特纳(天津)科技发展有限公司后台管理'
    site_footer = '伊特纳(天津)科技发展有限公司'
    menu_style = 'accordion'

    # # 菜单
    def get_site_menu(self):
        return [
            {
                'title': '近期数据统计和分析',
                'perm': self.get_model_perm(Visitor, 'view'),
                'icon': 'fa fa-bar-chart-o',
                'menus': (
                    {
                        'title': '网站浏览情况',
                        # 写死的url进行替换
                        'url': self.get_model_url(Visitor, 'changelist').replace('xadmin/viewsCount/visitor/',
                                                                                 'viewsCount/test/'),
                        # .replace('xadmin/viewsCount/visitor/', 'viewsCount/testview/'),
                        # 'url': 'http://10.17.20.86:8004/sms/data_analysis/msgsend_recent_24hours/',
                        'perm': self.get_model_perm(Visitor, 'view'),
                        'icon': 'fa fa-smile-o'
                    },
                )
            }
        ]


class RecordAdmin:
    # times = time.localtime('timeIn')
    list_display = ['all_time', 'user_agent', 'time']
    # data_charts = {
    #     "address": {'title': "每日访问时间统计", "x-field": "timeIn", "y-field": ("time", 'user_agent')},
    #     # "url": {'title': "每日访问方式统计", "x-field": "pub_ip", "y-field": ("refer",)},
    #     # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    # }


class ViewsByDayAdmin:
    readonly_fields = ['views_count', 'ip_count']
    data_charts = {
        "date": {'title': "每日访问方式统计", "x-field": "date", "y-field": ("views_count", 'ip_count')},
        # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    }


class DeviceByDayAdmin:
    # object_list_template = "test.html"
    data_charts = {
        "test": {'title': "每日访问设备统计", "x-field": "date", "y-field": ("pc_count", 'mobile_count')},
        # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    }


class RegionByDayAdmin:
    data_charts = {
        "test": {'title': "每日访问地区统计", "x-field": "date", "y-field": ('views_count', 'region')},
        # "avg_count": {'title': u"Avg Report", "x-field": "date", "y-field": ('avg_count',), "order": ('date',)}
    }


xadmin.site.register(Visitor, RecordAdmin)
# xadmin.site.register(Visitor, VisitorAdmin)
xadmin.site.register(ViewsByDay, ViewsByDayAdmin)
# xadmin.site.register(ViewsByDay, RecordAdmin)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(DeviceByDay, DeviceByDayAdmin)
xadmin.site.register(RegionByDay, RegionByDayAdmin)
