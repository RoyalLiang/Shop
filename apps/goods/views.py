from django.shortcuts import render, HttpResponse
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
            'sid': goods.category.series.id,
            'cid': goods.category.id,
            'sname': goods.category.series.name,
            'cname': goods.category.name,
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


class ProductsList(View):
    def get(self, request):
        sid = request.GET.get('sid', None)
        cid = request.GET.get('cid', None)
        series = GoodsSeries.objects.all()
        if cid and cid.isdigit():
            cid = int(cid)
            sid = GoodsSeries.objects.filter(goodscategory__id=cid)[0].id
            categorys = GoodsCategory.objects.filter(series__id=sid)
            goods_list = list(Goods.objects.filter(category__id=cid).prefetch_related('goodsimage_set'))
        elif sid and sid.isdigit():
            sid = int(sid)
            categorys = GoodsCategory.objects.filter(series__id=sid)
            goods_list = []
            for category in categorys:
                goods_list.extend(
                    list(Goods.objects.filter(category__id=category.id).prefetch_related('goodsimage_set')))
        else:
            categorys = GoodsCategory.objects.all()
            goods_list = []
            for category in categorys:
                goods_list.extend(
                    list(Goods.objects.filter(category__id=category.id).prefetch_related('goodsimage_set')))
            categorys = None
            sid = None
            cid = None
        for goods in goods_list:
            goods.goodsimage = list(goods.goodsimage_set.all())
        return render(request, 'goods/products.html',
                      {
                          'sid': sid,
                          'cid': cid,
                          'categorys': categorys,
                          'series': series,
                          'goods_list': goods_list,
                      })
