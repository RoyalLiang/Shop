from django.shortcuts import render, HttpResponse
from django.views import View
from .models import *
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import markdown


# Create your views here.


# class BackendIndex(View):
#     def get(self, request):
#         return HttpResponse('backend')
