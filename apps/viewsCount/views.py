from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
from .tasks import views_count_save


# Create your views here.


class ViewsCount(View):
    @csrf_exempt
    def post(self, request):
        views_count_save(request)
        return HttpResponse(json.dumps({'status': 'ok'}))
