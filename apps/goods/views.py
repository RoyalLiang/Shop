from django.shortcuts import render
from django.views import View
from .models import *
import markdown


# Create your views here.


class IndexView(View):
    def get(self, request):
        all_category = GoodsCategory.objects.all()
        all_goods = Goods.objects.all()
        # goods_list = [markdown.markdown(goods.detail for goods in all_goods)]
        for goods in all_goods:
            goods.detail = markdown.markdown(goods.detail.replace("\r\n", '  \n'), extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ])
        return render(request, 'index.html', {
            'all_category': all_category,
            'all_goods': all_goods
        })
