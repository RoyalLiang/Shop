import xadmin
from .models import *


class NewsAdmin:
    list_display = ['title', 'detail', ]
    search_fields = ['title', ]
    list_filter = ['title', 'detail', ]


class CompanyIntroductionAdmin:
    list_display = ['name', 'detail', 'add_time', ]


class FactoryAdmin:
    list_display = ['title', 'image', ]


class CustomerAdmin:
    list_display = ['title', 'image', ]


class IndexAdmin:
    list_display = ['title', 'keywords', 'description']


class UserContactMessageAdmin:
    list_display = ['name', 'email', 'country', 'message']


xadmin.site.register(News, NewsAdmin)
xadmin.site.register(CompanyIntroduction, CompanyIntroductionAdmin)
xadmin.site.register(Factory, FactoryAdmin)
xadmin.site.register(Customer, CustomerAdmin)
xadmin.site.register(Index, IndexAdmin)
xadmin.site.register(UserContactInfo, UserContactMessageAdmin)
