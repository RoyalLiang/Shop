from django.contrib import admin
from .models import *

# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'detail', ]
    search_fields = ['title', ]
    list_filter = ['title', 'detail', ]


class CompanyIntroductionAdmin(admin.ModelAdmin):
    list_display = ['name', 'detail', 'add_time', ]


class FactoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', ]


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', ]


class Indeadmin(admin.ModelAdmin):
    list_display = ['title', 'keywords', 'description']


class UserContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'country', 'message']


admin.site.register(News, NewsAdmin)
admin.site.register(CompanyIntroduction, CompanyIntroductionAdmin)
admin.site.register(Factory, FactoryAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Index, Indeadmin)
admin.site.register(UserContactInfo, UserContactMessageAdmin)
