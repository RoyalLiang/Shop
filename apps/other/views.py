from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from pure_pagination import Paginator, PageNotAnInteger
from django.views import View
from goods.views import Video, GoodsSeries
from django.core.cache import cache
from django.conf import settings

from viewsCount.tasks import send_contact_email
from .models import *
import markdown


# Create your views here.


class CompanyIntroduction_view(View):
    def get(self, request):
        company_info = cache.get('company_info')
        all_series = GoodsSeries.objects.all()
        all_brands = Brands.objects.all()
        if not company_info:
            company_info = CompanyIntroduction.objects.last()
            cache.set('company_info', company_info, settings.CUBES_REDIS_TIMEOUT)
        company_info.detail = markdown.markdown(company_info.detail.replace("\r\n", '  \n'), extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        index_info = cache.get('index_info')
        if not index_info:
            index_info = Index.objects.last()
            cache.set('index_info', index_info)
        index_info = {'title': 'CompanyIntroduction', 'description': index_info.description,
                      'keywords': index_info.keywords}
        return render(request, 'other/CompanyIntroduction.html', {
            'company_info': company_info,
            'index_info': index_info,
            'all_series': all_series,
            'all_brands': all_brands,
        })


class Video_view(View):
    def get(self, request):
        video_info = PageInformation.objects.get(pk=1)
        all_series = GoodsSeries.objects.all()
        all_brands = Brands.objects.all()
        com_info = CompanyIntroduction.objects.get(pk=1)
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        videos = cache.get('all_videos')
        if not videos:
            videos = Video.objects.all()
            cache.set('all_videos', videos, settings.CUBES_REDIS_TIMEOUT)
        p = Paginator(videos, request=request, per_page=3)
        videos = p.page(page)
        index_info = cache.get('index_info')
        if not index_info:
            index_info = Index.objects.last()
            cache.set('index_info', index_info)
        index_info = {'title': 'Video', 'description': index_info.description,
                      'keywords': index_info.keywords}
        return render(request, 'other/Video.html', {
            'videos': videos,
            'index_info': index_info,
            'video_info': video_info,
            'all_series': all_series,
            'com_info': com_info,
            'all_brands': all_brands,
        })


class Factory_view(View):
    def get(self, request):
        all_series = GoodsSeries.objects.all()
        com_info = CompanyIntroduction.objects.get(pk=1)
        page_info = PageInformation.objects.get(pk=1)
        all_brands = Brands.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        all_factory = cache.get('all_factory')
        if not all_factory:
            all_factory = Factory.objects.all()
            cache.set('all_factory', all_factory, settings.CUBES_REDIS_TIMEOUT)
        p = Paginator(all_factory, request=request, per_page=3)
        all_factory = p.page(page)
        index_info = cache.get('index_info')
        if not index_info:
            index_info = Index.objects.last()
            cache.set('index_info', index_info)
        index_info = {'title': 'Factory', 'description': index_info.description,
                      'keywords': index_info.keywords}
        return render(request, 'other/Factory.html', {
            'all_factory': all_factory,
            'index_info': index_info,
            'page_info': page_info,
            'all_series': all_series,
            'com_info': com_info,
            'all_brands': all_brands,

        })


class Customer_view(View):
    def get(self, request):
        all_series = GoodsSeries.objects.all()
        com_info = CompanyIntroduction.objects.get(pk=1)
        page_info = PageInformation.objects.get(pk=1)
        all_brands = Brands.objects.all()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        all_customer = cache.get('all_customer')
        if not all_customer:
            all_customer = Customer.objects.all()
            cache.set('all_customer', all_customer, settings.CUBES_REDIS_TIMEOUT)
        p = Paginator(all_customer, request=request, per_page=3)
        all_customer = p.page(page)
        index_info = cache.get('index_info')
        if not index_info:
            index_info = Index.objects.last()
            cache.set('index_info', index_info)
        index_info = {'title': 'Customer', 'description': index_info.description,
                      'keywords': index_info.keywords}
        return render(request, 'other/Customer.html', {
            'all_customer': all_customer,
            'index_info': index_info,
            'page_info': page_info,
            'all_series': all_series,
            'com_info': com_info,
            'all_brands': all_brands,
        })


class News_view(View):
    def get(self, request):
        all_series = GoodsSeries.objects.all()
        com_info = CompanyIntroduction.objects.get(pk=1)
        page_info = PageInformation.objects.get(pk=1)
        all_brands = Brands.objects.all()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        all_news = cache.get('all_news')
        if not all_news:
            all_news = News.objects.all()
            cache.set('all_news', all_news, settings.CUBES_REDIS_TIMEOUT)
        p = Paginator(all_news, request=request, per_page=3)
        all_news = p.page(page)
        index_info = cache.get('index_info')
        if not index_info:
            index_info = Index.objects.last()
            cache.set('index_info', index_info)
        index_info = {'title': 'News', 'description': index_info.description,
                      'keywords': index_info.keywords}
        return render(request, 'other/NEWS.html', {
            'all_news': all_news,
            'index_info': index_info,
            'page_info': page_info,
            'all_series': all_series,
            'com_info': com_info,
            'all_brands': all_brands,
        })


class News_detail(View):
    def get(self, request, news_id):
        news = cache.get('news_%s' % news_id)
        all_series = GoodsSeries.objects.all()
        com_info = CompanyIntroduction.objects.get(pk=1)
        all_brands = Brands.objects.all()
        if not news:
            news = News.objects.get(id=int(news_id))
            cache.set('news_%s' % news_id, news, settings.CUBES_REDIS_TIMEOUT)
        pnews = cache.get('news_%s' % (int(news_id) - 1))
        if not news:
            pnews = News.objects.get(id=int(news_id) - 1)
            cache.set('news_%s' % (int(news_id) - 1), pnews, settings.CUBES_REDIS_TIMEOUT)
        nnews = cache.get('news_%s' % (int(news_id) + 1))
        if not news:
            nnews = News.objects.get(id=int(news_id) + 1)
            cache.set('news_%s' % (int(news_id) + 1), nnews, settings.CUBES_REDIS_TIMEOUT)
        news.detail = markdown.markdown(news.detail.replace("\r\n", '  \n'), extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
        ])
        index_info = cache.get('index_info')
        if not index_info:
            index_info = Index.objects.last()
            cache.set('index_info', index_info)
        index_info = {'title': 'News:%s' % news.title, 'description': index_info.description,
                      'keywords': index_info.keywords}
        return render(request, 'other/NEWS_detail.html', {
            'pnews': pnews,
            'news': news,
            'nnews': nnews,
            'index_info': index_info,
            'all_series': all_series,
            'com_info': com_info,
            'all_brands': all_brands,
        })


class ContactView(View):
    """
    联系我们
    """

    def get(self, request):
        all_series = GoodsSeries.objects.all()
        com_message = CompanyIntroduction.objects.get(pk=1)
        all_brands = Brands.objects.all()
        return render(request, 'contact.html', {
            'com_message': com_message,
            'all_series': all_series,
            'all_brands': all_brands,
        })

    @csrf_exempt
    def post(self, request):
        data = dict()
        data['name'] = request.POST.get('name', None)
        data['phone'] = request.POST.get('phone', None)
        data['email'] = request.POST.get('email', None)
        data['country'] = request.POST.get('country', None)
        data['message'] = request.POST.get('message', None)
        send_contact_email.delay(data)
        return HttpResponse('{"status": "success"}', content_type='application/json')
