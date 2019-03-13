from django.shortcuts import render
from django.views import View
from .models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import markdown


# Create your views here.


class IndexView(View):
    def get(self, request):
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        all_goods = Goods.objects.all()
        for goods in all_goods:
            goods.detail = markdown.markdown(goods.detail.replace("\r\n", '  \n'), extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ])

        p = Paginator(all_goods, request=request, per_page=1)

        all_goods = p.page(page)

        all_category = GoodsCategory.objects.all()
        all_banner = Banner.objects.all().order_by('index')

        return render(request, 'index.html', {
            'all_category': all_category,
            'all_goods': all_goods,
            'all_banner': all_banner
        })


class GoodsDetail(View):
    def get(self, request, goods_id):
        goods = Goods.objects.filter(id=goods_id).first()
        goods_banners = GoodsImage.objects.filter(goods__id=goods_id).all()
        goods_attrs = GoodsAttributes.objects.filter(goods__id=goods_id)
        return render(request, 'goods/goods-detail.html', {
            'goods': goods,
            'goods_banners': goods_banners,
            'goods_attrs': goods_attrs,
        })


class GoodsGetList(View):
    def get(self, request):
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        all_goods = Goods.objects.all()
        for goods in all_goods:
            goods.detail = markdown.markdown(goods.detail.replace("\r\n", '  \n'), extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ])

        p = Paginator(all_goods, request=request, per_page=1)
        all_goods = p.page(page)
        return render(request, 'backend/goods-list.html', {'all_goods': all_goods})
