import xadmin
from .models import *
from xadmin import views


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


xadmin.site.register(GoodsCategory, GoodsCategoryAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(GoodsImage, GoodsImageAdmin)




