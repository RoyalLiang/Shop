import xadmin
from .models import *


class NewsAdmin:
    list_display = ['title', 'detail', ]
    search_fields = ['title', ]
    list_filter = ['title', 'detail', ]


xadmin.site.register(News, NewsAdmin)
