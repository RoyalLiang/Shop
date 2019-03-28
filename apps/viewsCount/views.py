from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
from .tasks import views_count_save


# Create your views here.


class ViewsCount(View):
    @csrf_exempt
    def post(self, request):
        if request.META.get('HTTP_X_FORWARDED_FOR', None):
            in_ip = request.META['HTTP_X_FORWARDED_FOR']
        else:
            in_ip = request.META['REMOTE_ADDR']
        data_json = request.POST.get('data', None)
        data = {
            'in_ip': in_ip,
            'data_json': data_json,
        }
        views_count_save.delay(data)
        return HttpResponse(json.dumps({'status': 'ok'}))


class TestView(View):
    def get(self, request):
        return render(request, 'test.html')
