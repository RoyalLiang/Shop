import xadmin
from .models import *
from xadmin import views
import os
from Shop import settings
from utils import auth
from django.core.cache import cache
from django.conf import settings
# from viewsCount.models import Visitor


class BaseSettings:
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    site_title = '伊特纳(天津)科技发展有限公司后台管理'
    site_footer = '伊特纳(天津)科技发展有限公司'
    menu_style = 'accordion'

    # def get_site_menu(self):
    #     return [
    #         {
    #             'title': '近期数据统计',
    #             'perm': self.get_model_perm(Visitor, 'change'),
    #             'icon': 'fa fa-bars',
    #             'menus': (
    #                 {
    #                     'title': '浏览器信息',
    #                     'icon': 'fa fa-bars',
    #                     'url': self.get_model_url(Visitor, 'changelist').replace('xadmin/viewsCount/', 'ViewsCount/testview/'),
    #                     # 'perm': self.get_model_perm(Visitor, 'view'),
    #                 },
    #                 # {
    #                 #     'title': '存放位置',
    #                 #     'icon': 'fa fa-archive',
    #                 #     'url': self.get_model_url(Visitor, 'changelist')
    #                 # }
    #             )
    #         },
    #     ]
    # # 菜单
    # def get_site_menu(self):
    #     return [
    #         {
    #             'title': '近期数据统计和分析',
    #             'perm': self.get_model_perm(Visitor, 'view'),
    #             'icon': 'fa fa-bar-chart-o',
    #             'menus': (
    #                 {
    #                     'title': '网站浏览情况',
    #                     # 写死的url进行替换
    #                     'url': self.get_model_url(Visitor, 'changelist').replace('xadmin/viewsCount/visitor/',
    #                                                                              'viewsCount/testview/'),
    #                     # 'url': 'http://10.17.20.86:8004/sms/data_analysis/msgsend_recent_24hours/',
    #                     'perm': self.get_model_perm(Visitor, 'view'),
    #                     'icon': 'fa fa-smile-o'
    #                 },
    #             )
    #         }
    #     ]

    # def get_nav_menu(self):
    #     # 直接返回新增的菜单栏，源码中还有很大一部分的合并功能
    #     site_menu = list(self.get_site_menu() or [])
    #     return site_menu


class GoodsAdmin:
    list_display = ['name', 'desc', 'goods_sn', 'add_time']
    search_fields = ['name', 'goods_sn']
    list_filter = ['add_time']
    style_fields = {'attr': 'm2m_transfer'}

    def save_models(self):
        obj = self.new_obj
        all_goods = cache.get('all_goods')
        if all_goods:
            cache.set('all_goods', list(all_goods).append(obj), settings.CUBES_REDIS_TIMEOUT)
        obj.save()


class GoodsCategoryAdmin:
    list_display = ['name', 'add_time']
    search_fields = ['name']
    list_filter = ['add_time']


class GoodsImageAdmin:
    list_display = ['goods', 'image_url', 'add_time']
    search_fields = ['goods']
    list_filter = ['add_time']


class BannerAdmin:
    list_display = ['title', 'index', 'add_time']
    search_fields = ['title', ]
    list_filter = ['add_time']


class GoodsAttributesAdmin:
    list_display = ['name', 'value']
    search_fields = ['name', 'value']
    list_filter = ['name', ]


class MessageAdmin:
    list_display = ['inquire', 'name', 'phone', 'email', 'address', 'message']
    search_fields = ['name', 'inquire']
    list_filter = ['inquire', 'name', ]


class VideoAdmin:
    list_display = ['title', 'video', ]
    search_fields = ['title', ]
    list_filter = ['title', ]

    def save_models(self):
        obj = self.new_obj
        obj.save()
        video_url = os.path.join(settings.MEDIA_ROOT, str(obj.video))
        obj.image = 'video_image/%s' % auth.get_video_pic(video_url)
        obj.save()


class GoodsSeriesAdmin:
    list_display = ['name', ]
    search_fields = ['name', ]


xadmin.site.register(views.BaseAdminView, BaseSettings)
# xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(GoodsSeries, GoodsSeriesAdmin)
xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(GoodsImage, GoodsImageAdmin)
xadmin.site.register(GoodsAttributes, GoodsAttributesAdmin)
xadmin.site.register(Message, MessageAdmin)
xadmin.site.register(Video, VideoAdmin)
