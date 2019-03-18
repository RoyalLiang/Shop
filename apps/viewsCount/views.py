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
    @csrf_exempt
    def post(self, request):
        views_count_save(request)
        return HttpResponse(json.dumps({'status': 'ok'}))
