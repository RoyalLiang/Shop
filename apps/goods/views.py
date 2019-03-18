from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.db.models import Q
from django.core.cache import cache
from .models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import markdown
import json


# Create your views here.


class IndexView(View):
    def get(self, request):
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        all_goods = cache.get('all_goods')
        if not all_goods:
            all_goods = Goods.objects.values('id', 'category', 'name', 'goods_front_img', 'goods_sn', 'desc',
                                             'detail', ).all()
            cache.set('all_goods', all_goods, settings.CUBES_REDIS_TIMEOUT)
        for goods in all_goods:
            goods['detail'] = markdown.markdown(goods['detail'].replace("\r\n", '  \n'), extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ])

        p = Paginator(all_goods, request=request, per_page=1)

        all_goods = p.page(page)
        all_category = cache.get('all_category')
        if not all_category:
            all_category = GoodsCategory.objects.values('id', 'name', 'series').all()
            cache.set('all_category', all_category)
        all_banner = cache.get('all_banner')
        if not all_banner:
            all_banner = Banner.objects.values('id', 'title', 'image', 'url', 'index', ).order_by('index')
            cache.set('all_banner', all_banner)

        return render(request, 'index.html', {
            'all_category': all_category,
            'all_goods': all_goods,
            'all_banner': all_banner
        })


class GoodsDetail(View):
    def get(self, request, goods_id):
        goods = cache.get('goods_%s' % goods_id)
        if not goods:
            goods = Goods.objects.filter(id=goods_id).values('id', 'category', 'name', 'goods_front_img', 'goods_sn',
                                                             'desc',
                                                             'detail', ).first()
            cache.set('goods_%s' % goods_id, goods)
        goods['detail'] = markdown.markdown(goods['detail'].replace("\r\n", '  \n'), extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        current_category = cache.get('category_%s' % goods['category'])
        if not current_category:
            current_category = GoodsCategory.objects.filter(id=goods['category']).values('id', 'name', 'series').first()
            cache.set('category_%s' % goods['category'], current_category)

        current_series = cache.get('series_%s' % current_category['series'])
        if not current_series:
            current_series = GoodsSeries.objects.filter(id=current_category['series']).values('id', 'name', ).first()
            cache.set('series_%s' % current_category['series'], current_series)

        goods_banners = cache.get('goods_banners_%s' % goods_id)
        if not goods_banners:
            goods_banners = GoodsImage.objects.filter(goods__id=goods_id).values('id', 'image', 'image_url',
                                                                                 'index', ).all()
            cache.set('goods_banners_%s' % goods_id, goods_banners)

        goods_attrs = cache.get('goods_attrs_%s' % goods_id)
        if not goods_attrs:
            goods_attrs = GoodsAttributes.objects.filter(goods__id=goods_id).values('id', 'name', 'value').all()
            cache.set('goods_attrs_%s' % goods_id, goods_attrs)
        return render(request, 'goods/goods-detail.html', {
            'goods': goods,
            'goods_banners': goods_banners,
            'goods_attrs': goods_attrs,
            'sid': current_series['id'],
            'cid': current_category['id'],
            'sname': current_series['name'],
            'cname': current_category['name'],
        })


# class GoodsGetList(View):
#     def get(self, request):
#         try:
#             page = request.GET.get('page', 1)
#         except PageNotAnInteger:
#             page = 1
#         all_goods = Goods.objects.all()
#         for goods in all_goods:
#             goods.detail = markdown.markdown(goods.detail.replace("\r\n", '  \n'), extensions=[
#                 'markdown.extensions.extra',
#                 'markdown.extensions.codehilite',
#                 'markdown.extensions.toc',
#             ])
#
#         p = Paginator(all_goods, request=request, per_page=1)
#         all_goods = p.page(page)
#         return render(request, 'backend/goods-list.html', {'all_goods': all_goods})


class ProductsList(View):
    def get(self, request):
        sid = request.GET.get('sid', None)
        cid = request.GET.get('cid', None)
        series = cache.get('all_series')
        if not series:
            series = GoodsSeries.objects.values('id', 'name', ).all()
            cache.set('all_series', series)
        if cid and cid.isdigit():
            cid = int(cid)
            current_category = cache.get('category_%s' % cid)
            if not current_category:
                current_category = GoodsCategory.objects.filter(id=cid).values('id', 'name', 'series').first()
                cache.set('category_%s' % cid, current_category)
            sid = current_category['series']
            categorys = cache.get('categorys_by_s%s' % sid)
            if not categorys:
                categorys = GoodsCategory.objects.filter(series__id=sid).values('id', 'name', 'series').all()
                cache.set('categorys_by_s%s' % sid, categorys)
            goods_list = list(Goods.objects.filter(category__id=cid).prefetch_related('goodsimage_set'))
        elif sid and sid.isdigit():
            sid = int(sid)
            categorys = cache.get('categorys_by_s%s' % sid)
            if not categorys:
                categorys = GoodsCategory.objects.filter(series__id=sid).values('id', 'name', 'series').all()
                cache.set('categorys_by_s%s' % sid, categorys)
            goods_list = []
            for category in categorys:
                goods_list.extend(
                    list(Goods.objects.filter(category__id=category['id']).prefetch_related('goodsimage_set')))
        else:
            categorys = cache.get('all_category')
            if not categorys:
                categorys = GoodsCategory.objects.values('id', 'name', 'series').all()
                cache.set('all_category', categorys)
            goods_list = []
            for category in categorys:
                goods_list.extend(
                    list(Goods.objects.filter(category__id=category['id']).prefetch_related('goodsimage_set')))
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
                          'title': 'Products',
                      })


class Search(View):
    def get(self, request):
        query = request.GET.get('query', None)
        goods_list = []
        series = GoodsSeries.objects.filter(name__icontains=query).all()
        categorys = []
        for s in series:
            categorys.extend(list(GoodsCategory.objects.filter(series=s).all()))
        for c in categorys:
            goods_list.extend(list(Goods.objects.filter(category=c).all()))
        category = GoodsCategory.objects.filter(name__icontains=query).all()
        for c in category:
            goods_list.extend(list(Goods.objects.filter(category=c).all()))
        goods_list.extend(list(
            Goods.objects.filter(Q(name__icontains=query) | Q(goods_sn__icontains=query)).all()))
        goods_list = list(set(goods_list))
        for goods in goods_list:
            goods.goodsimage = list(goods.goodsimage_set.all())
        return render(request, 'goods/products.html',
                      {
                          'sid': None,
                          'cid': None,
                          'categorys': None,
                          'series': None,
                          'goods_list': goods_list,
                          'title': 'Search',
                      })


class AddMessage(View):
    def get(self, request):
        return HttpResponse()

    @csrf_exempt
    def post(self, request):
        inquire = request.POST.get('inquire', None)
        name = request.POST.get('name', None)
        phone = request.POST.get('phone', None)
        email = request.POST.get('email', None)
        address = request.POST.get('address', None)
        message = request.POST.get('message', None)
        Message.objects.create(inquire=inquire, name=name, phone=phone, email=email, address=address,
                               message=message).save()
        dic = {'status': 'ok'}
        return HttpResponse(json.dumps(dic))
