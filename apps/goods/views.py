from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.db.models import Q
from django.core.cache import cache
from .models import *
from pure_pagination import Paginator, PageNotAnInteger
import markdown
import json
from viewsCount.tasks import send_goods_email
from django.conf import settings
from other.models import Index, CompanyIntroduction, PageInformation, Brands


# Create your views here.


class IndexView(View):
    def get(self, request):
        all_goods = cache.get('all_goods')
        all_series = GoodsSeries.objects.all()
        com_info = CompanyIntroduction.objects.last()
        all_brands = Brands.objects.all()
        if not all_goods:
            all_goods = Goods.objects.all().order_by('-leval')[:4]
            cache.set('all_goods', all_goods, settings.CUBES_REDIS_TIMEOUT)
        for goods in all_goods:
            goods.detail = markdown.markdown(goods.detail.replace("\r\n", '  \n'), extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                'markdown.extensions.toc',
            ])
        # all_category = cache.get('all_category')
        # if not all_category:
        #     all_category = GoodsCategory.objects.all()
        #     cache.set('all_category', all_category, settings.CUBES_REDIS_TIMEOUT)
        all_banner = cache.get('all_banner')
        if not all_banner:
            all_banner = Banner.objects.order_by('index')
            cache.set('all_banner', all_banner, settings.CUBES_REDIS_TIMEOUT)
        index_info = Index.objects.last()
        videos = Video.objects.all()
        if len(videos) > 2:
            video1 = videos[len(videos) - 1]
            video2 = videos[len(videos) - 2]
        elif len(videos) == 1:
            video1 = videos[0]
            video2 = None
        else:
            video1 = None
            video2 = None
        return render(request, 'index.html', {
            # 'all_category': all_category,
            'all_goods': all_goods,
            'all_banner': all_banner,
            'index_info': index_info,
            'all_series': all_series,
            'com_info': com_info,
            'all_brands': all_brands,
            'video1': video1,
            'video2': video2,

        })


class GoodsDetail(View):
    def get(self, request, goods_id):
        all_series = GoodsSeries.objects.all()
        com_info = CompanyIntroduction.objects.last()
        all_brands = Brands.objects.all()
        goods = cache.get('goods_%s' % goods_id)
        if not goods:
            goods = Goods.objects.filter(id=goods_id).first()
            cache.set('goods_%s' % goods_id, goods, settings.CUBES_REDIS_TIMEOUT)
        goods.detail = markdown.markdown(goods.detail.replace("\r\n", '  \n'), extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        # current_category = cache.get('category_by_g%s' % goods_id)
        # if not current_category:
        #     current_category = goods.category
        #     cache.set('category_by_g%s' % goods_id, current_category, settings.CUBES_REDIS_TIMEOUT)
        # current_series = cache.get('series_by_c%s' % current_category.id)
        # if not current_series:
        #     current_series = current_category.series
        #     cache.set('series_by_c%s' % current_category.id, current_series, settings.CUBES_REDIS_TIMEOUT)
        current_series = cache.get('series_by_g%s' % goods_id)
        if not current_series:
            current_series = goods.series
            cache.set('series_by_g%s' % goods_id, current_series, settings.CUBES_REDIS_TIMEOUT)
        goods_banners = cache.get('goods_banners_%s' % goods_id)
        if not goods_banners:
            goods_banners = goods.goodsimage_set.all()
            cache.set('goods_banners_%s' % goods_id, goods_banners, settings.CUBES_REDIS_TIMEOUT)
        goods_attrs = cache.get('goods_attrs_%s' % goods_id)
        if not goods_attrs:
            goods_attrs = GoodsAttributes.objects.filter(goods__id=goods_id).all().order_by('-weight')[:3]
            cache.set('goods_attrs_%s' % goods_id, goods_attrs, settings.CUBES_REDIS_TIMEOUT)
        return render(request, 'goods/goods-detail.html', {
            'goods': goods,
            'goods_banners': goods_banners,
            'goods_attrs': goods_attrs,
            'sid': current_series.id,
            # 'cid': current_category.id,
            'sname': current_series.name,
            # 'cname': current_category.name,
            'all_series': all_series,
            'com_info': com_info,
            'all_brands': all_brands
        })


class ProductsList(View):
    def get(self, request):
        com_info = CompanyIntroduction.objects.last()
        page_info = PageInformation.objects.last()
        page_info = markdown.markdown(page_info.product_info.replace("\r\n", '  \n'), extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        all_brands = Brands.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        sid = request.GET.get('sid', None)
        # cid = request.GET.get('cid', None)
        series = cache.get('all_series')
        if not series:
            series = GoodsSeries.objects.all()
            cache.set('all_series', series, settings.CUBES_REDIS_TIMEOUT)
        # if cid and cid.isdigit():
        #     cid = int(cid)
        #     current_category = cache.get('category_%s' % cid)
        #     if not current_category:
        #         current_category = GoodsCategory.objects.filter(id=cid).first()
        #         cache.set('category_%s' % cid, current_category, settings.CUBES_REDIS_TIMEOUT)
        #     sid = current_category.series.id
        #     query = '%s-%s' % (current_category.series.name, current_category.name)
        #     categorys = cache.get('categorys_by_s%s' % sid)
        #     if not categorys:
        #         categorys = GoodsCategory.objects.filter(series__id=int(sid)).all()
        #         cache.set('categorys_by_s%s' % sid, categorys)
        #     goods_list = list(Goods.objects.filter(category__id=int(cid)).prefetch_related('goodsimage_set').order_by('-leval'))
        # elif sid and sid.isdigit():
        if sid and sid.isdigit():
            sid = int(sid)
            # categorys = cache.get('categorys_by_s%s' % sid)
            # if not categorys:
            #     categorys = GoodsCategory.objects.filter(series__id=int(sid)).all()
            #     cache.set('categorys_by_s%s' % sid, categorys, settings.CUBES_REDIS_TIMEOUT)
            # goods_list = []
            # for category in categorys:
            #     goods_list.extend(
            #         list(Goods.objects.filter(category__id=category.id).prefetch_related('goodsimage_set').order_by('-leval')))
            goods_list = Goods.objects.filter(series__id=sid).prefetch_related('goodsimage_set').order_by('-leval')
            query = GoodsSeries.objects.filter(id=sid).first().name
        else:
            # categorys = cache.get('all_category')
            # if not categorys:
            #     categorys = GoodsCategory.objects.all()
            #     cache.set('all_category', categorys, settings.CUBES_REDIS_TIMEOUT)
            # goods_list = []
            # for category in categorys:
            #     goods_list.extend(
            #         list(Goods.objects.filter(category__id=category.id).prefetch_related('goodsimage_set').order_by(
            #             '-leval')))
            # categorys = None
            series = cache.get('all_series')
            if not series:
                series = GoodsSeries.objects.all()
                cache.set('all_series', series, settings.CUBES_REDIS_TIMEOUT)
            goods_list = []
            for s in series:
                goods_list.extend(
                    list(Goods.objects.filter(series__id=s.id).prefetch_related('goodsimage_set').order_by(
                        '-leval')))
            sid = None
            # cid = None
            query = 'All'
        for goods in goods_list:
            goods.goodsimage = list(goods.goodsimage_set.all())
        p = Paginator(goods_list, request=request, per_page=5)
        goods_list = p.page(page)
        index_info = cache.get('index_info')
        if not index_info:
            index_info = Index.objects.last()
            cache.set('index_info', index_info)
        index_info = {'title': 'Products-%s' % query, 'description': index_info.description,
                      'keywords': index_info.keywords}
        return render(request, 'goods/products.html',
                      {
                          'sid': sid,
                          # 'cid': cid,
                          # 'categorys': categorys,
                          'all_series': series,
                          'goods_list': goods_list,
                          'index_info': index_info,
                          'page_info': page_info,
                          'com_info': com_info,
                          'all_brands': all_brands,
                      })


class Search(View):
    def get(self, request):
        all_series = GoodsSeries.objects.all()
        com_info = CompanyIntroduction.objects.get(pk=1)
        all_brands = Brands.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        query = request.GET.get('query', None)
        goods_list = []
        series = GoodsSeries.objects.filter(name__icontains=query).all()
        # categorys = []
        # for s in series:
        #     categorys.extend(list(GoodsCategory.objects.filter(series=s).all()))
        for s in series:
            goods_list.extend(list(Goods.objects.filter(series=s).all()))
        # category = GoodsCategory.objects.filter(name__icontains=query).all()
        # for c in category:
        #     goods_list.extend(list(Goods.objects.filter(category=c).all()))
        goods_list.extend(list(
            Goods.objects.filter(Q(name__icontains=query) | Q(goods_sn__icontains=query)).all()))
        goods_list = list(set(goods_list))
        for goods in goods_list:
            goods.goodsimage = list(goods.goodsimage_set.all())
        p = Paginator(goods_list, request=request, per_page=5)
        goods_list = p.page(page)
        index_info = cache.get('index_info')
        if not index_info:
            index_info = Index.objects.last()
            cache.set('index_info', index_info)
        index_info = {'title': 'Search:%s' % query, 'description': index_info.description,
                      'keywords': index_info.keywords}
        return render(request, 'goods/products.html',
                      {
                          'sid': None,
                          'cid': None,
                          # 'categorys': None,
                          'goods_list': goods_list,
                          'index_info': index_info,
                          'com_info': com_info,
                          'all_series': all_series,
                          'all_brands': all_brands,
                      })


class AddMessage(View):

    @csrf_exempt
    def post(self, request):
        message = {}
        message['inquire'] = request.POST.get('inquire', None)
        message['name'] = request.POST.get('name', None)
        message['phone'] = request.POST.get('phone', None)
        message['email'] = request.POST.get('email', None)
        message['address'] = request.POST.get('address', None)
        message['message'] = request.POST.get('message', None)
        send_goods_email.delay(message)
        return HttpResponse(json.dumps({'status': 'ok'}))
