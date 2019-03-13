from django.shortcuts import render, HttpResponse
from django.views import View
from goods.views import Video as V
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import markdown


# Create your views here.


class CompanyIntroduction(View):
    def get(self, request):
        return render(request, 'other/CompanyIntroduction.html')


class Video(View):
    def get(self, request):
        videos = V.objects.all()
        return render(request, 'other/Video.html',
                      {'videos': videos})


class Factory(View):
    def get(self, request):
        return render(request, 'other/Factory.html')


class Customer(View):
    def get(self, request):
        return render(request, 'other/Customer.html')
