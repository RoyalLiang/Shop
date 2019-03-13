import xadmin
from .models import *
from xadmin import views
import os
from Shop import settings
from utils import auth


class BaseSettings:
    enable_themes = True
    use_bootswatch = True


class GlobalSettings:
    site_title = '伊特纳(天津)科技发展有限公司后台管理'
    site_footer = '伊特纳(天津)科技发展有限公司'
    menu_style = 'accordion'


class GoodsAdmin:
    list_display = ['name', 'desc', 'goods_sn', 'add_time']
    search_fields = ['name', 'goods_sn']
    list_filter = ['add_time']
    style_fields = {'attr': 'm2m_transfer'}


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


xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(GoodsImage, GoodsImageAdmin)
xadmin.site.register(GoodsAttributes, GoodsAttributesAdmin)
xadmin.site.register(Message, MessageAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(GoodsSeries, GoodsSeriesAdmin)
