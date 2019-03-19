from django.shortcuts import render, HttpResponse
from django.views import View
from goods.views import Video as V
from django.core.cache import cache
from django.conf import settings


# Create your views here.


class CompanyIntroduction(View):
    def get(self, request):
        return render(request, 'other/CompanyIntroduction.html')


class Video(View):
    def get(self, request):
        videos = cache.get('all_videos')
        if not videos:
            videos = V.objects.all()
            cache.set('all_videos', videos, settings.CUBES_REDIS_TIMEOUT)
        return render(request, 'other/Video.html',
                      {'videos': videos})


class Factory(View):
    def get(self, request):
        return render(request, 'other/Factory.html')


class Customer(View):
    def get(self, request):
        return render(request, 'other/Customer.html')
