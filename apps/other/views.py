from django.shortcuts import render, HttpResponse
from django.views import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import markdown


# Create your views here.


class CompanyIntroduction(View):
    def get(self, request):
        return render(request, 'other/CompanyIntroduction.html')


class Video(View):
    def get(self, request):
        return render(request, 'other/Video.html')


class Factory(View):
    def get(self, request):
        return render(request, 'other/Factory.html')


class Customer(View):
    def get(self, request):
        return render(request, 'other/Customer.html')
