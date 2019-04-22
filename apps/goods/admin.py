from django.contrib import admin
from utils import auth
import os
from Shop import settings
from django.core.cache import cache
from .models import *
from modeltranslation.admin import TranslationAdmin


class BannerAdmin(TranslationAdmin):
    list_display = ['title', 'index', 'add_time']
    search_fields = ['title', ]
    list_filter = ['add_time']


class GoodsAdmin(TranslationAdmin):
    list_display = ['name', 'desc', 'goods_sn', 'add_time']
    search_fields = ['name', 'goods_sn']
    list_filter = ['add_time']
    # style_fields = {'attr': 'm2m_transfer'}
    filter_horizontal = ('attr',)

    def save_model(self, request, obj, form, change):
        '''
        admin
        '''
        all_goods = cache.get('all_goods')
        if all_goods:
            cache.set('all_goods', list(all_goods).append(obj), settings.CUBES_REDIS_TIMEOUT)
        obj.save()
        super().save_model(request, obj, form, change)


# class GoodsCategoryAdmin(TranslationAdmin):
#     list_display = ['name', 'add_time']
#     search_fields = ['name']
#     list_filter = ['add_time']


class GoodsImageAdmin(TranslationAdmin):
    list_display = ['goods', 'image_url', 'add_time']
    search_fields = ['goods']
    list_filter = ['add_time']


class GoodsAttributesAdmin(TranslationAdmin):
    list_display = ['name', 'value']
    search_fields = ['name', 'value']
    list_filter = ['name', ]


class MessageAdmin(admin.ModelAdmin):
    list_display = ['inquire', 'name', 'phone', 'email', 'address', 'message']
    readonly_fields = ('inquire', 'name', 'phone', 'email', 'address', 'message', 'add_time')
    search_fields = ['name', 'inquire']
    list_filter = ['inquire', 'name', ]


class VideoAdmin(TranslationAdmin):
    list_display = ['title', 'video', ]
    search_fields = ['title', ]
    list_filter = ['title', ]

    def save_model(self, request, obj, form, change):
        '''
        admin
        '''
        obj.save()
        video_url = os.path.join(settings.MEDIA_ROOT, str(obj.video))
        # linux设置视频文件权限
        os.system("chmod 644 %s" % video_url)
        obj.image = 'video_image/%s' % auth.get_video_pic(video_url)
        obj.save()
        super().save_model(request, obj, form, change)


class GoodsSeriesAdmin(TranslationAdmin):
    list_display = ['name', ]
    search_fields = ['name', ]


admin.site.register(Banner, BannerAdmin)
admin.site.register(GoodsSeries, GoodsSeriesAdmin)
# admin.site.register(GoodsCategory, GoodsCategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(GoodsImage, GoodsImageAdmin)
admin.site.register(GoodsAttributes, GoodsAttributesAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Video, VideoAdmin)
