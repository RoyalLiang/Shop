import xadmin
from .models import *


class GoodsAdmin(object):
    list_display = ['name', 'desc', 'add_time']


xadmin.site.register(Goods, GoodsAdmin)
