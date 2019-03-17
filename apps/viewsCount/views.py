from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from goods.views import Video as V
import json
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
import markdown
from .tasks import views_count_save

# Create your views here.


class ViewsCount(View):
    def get(self, request):
        # if request.META.get('HTTP_X_FORWARDED_FOR', None):
        #     ip = request.META['HTTP_X_FORWARDED_FOR']
        # else:
        #     ip = request.META['REMOTE_ADDR']
        views_count_save(request)
        return HttpResponse(json.dumps({'status': 'ok'}))

    @csrf_exempt
    def post(self, request):
        print(request.GET)
        print(request.POST)
        if request.META.get('HTTP_X_FORWARDED_FOR', None):
            ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            ip = request.META['REMOTE_ADDR']
        refer = request.META.get('HTTP_REFERER')
        user_agent = request.META.get('HTTP_USER_AGENT')
        return HttpResponse(json.dumps({'status': 'ok'}))
