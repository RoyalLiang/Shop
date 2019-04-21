from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin
# Register your models here.


class NewsAdmin(TranslationAdmin):
    list_display = ['title', 'detail', ]
    search_fields = ['title', ]
    list_filter = ['title', 'detail', ]


class CompanyIntroductionAdmin(TranslationAdmin):
    list_display = ['name', 'detail', 'add_time', ]


class FactoryAdmin(TranslationAdmin):
    list_display = ['title', 'image', ]


class CustomerAdmin(TranslationAdmin):
    list_display = ['title', 'image', ]


class IndexAdmin(TranslationAdmin):
    list_display = ['title', 'keywords', 'description']


class UserContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'country', 'message']


@admin.register(PageInformation)
class PageInformationAdmin(admin.ModelAdmin):
    list_display = ['product_info', 'news_info', 'video_info', 'customer_info', 'factory_info']


@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    search_fields = ['name', 'url']
    list_filter = ['add_time']


admin.site.register(News, NewsAdmin)
admin.site.register(CompanyIntroduction, CompanyIntroductionAdmin)
admin.site.register(Factory, FactoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Index, IndexAdmin)
admin.site.register(UserContactInfo, UserContactMessageAdmin)
