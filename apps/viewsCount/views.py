from django.shortcuts import HttpResponse, render
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json
from .tasks import views_count_save
from .models import *
import pymysql


# Create your views here.


class ViewsCount(View):
    @csrf_exempt
    def post(self, request):
        try:
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
        except Exception as e:
            print(1)


class TestView(View):
    def get(self, request):
        all_data = Visitor.objects.all()

        data = [i.user_agent for i in all_data]
        conn = pymysql.connect('47.100.164.154', 'admin', 'Lzy96800..', 'shop', charset='utf8')
        cursor = conn.cursor()
        # cursor.execute("SELECT FROM_UNIXTIME(timeIn/1000, '%Y-%m-%d'),user_agent,count(*) from viewsCount_visitor group by user_agent,FROM_UNIXTIME(timeIn/1000, '%Y-%m-%d')")
        cursor.execute(
            "SELECT user_agent,count(*) from viewsCount_visitor group by user_agent,FROM_UNIXTIME(timeIn/1000, '%Y-%m-%d')")
        data1 = cursor.fetchall()
        cursor.execute(
            "SELECT FROM_UNIXTIME(timeIn/1000, '%Y-%m-%d') from viewsCount_visitor group by FROM_UNIXTIME(timeIn/1000, '%Y-%m-%d')")
        date_li = cursor.fetchall()
        my_data = {}.fromkeys([date for date in date_li], [])

        cursor.execute(
            "SELECT FROM_UNIXTIME(timeIn/1000, '%Y-%m-%d'),user_agent from viewsCount_visitor group by user_agent,FROM_UNIXTIME(timeIn/1000, '%Y-%m-%d') order by FROM_UNIXTIME(timeIn/1000, '%Y-%m-%d')")
        # cursor.execute("select FROM_UNIXTIME(timeIn/1000, '%Y-%m-%d'),user_agent,count(*) from viewsCount_visitor where DATE_SUB(CURDATE(), INTERVAL 7 DAY) <= date(FROM_UNIXTIME(timeIn/1000, '%Y-%m-%d')) group by user_agent,FROM_UNIXTIME(timeIn/1000, '%Y-%m-%d')")
        # cursor.execute("select user_agent FROM_UNIXTIME(timeIn/1000, '%Y-%m-%d') from viewsCount_visitor group by FROM_UNIXTIME(timeIn/1000, '%Y-%m-%d')")
        test = cursor.fetchall()
        # sql = "SELECT FROM_UNIXTIME(timeIn/1000, '%Y-%m-%d') as t (SELECT user_agent,count(*) from viewsCount_visitor group by user_agent) from viewsCount_visitor group by t"
        # cursor.execute(sql)
        # by_day = cursor.fetchall()
        # print(by_day)
        # my_data['time'] = date_li
        # for i in range(len(data1)):
        #     my_data['ie'].append(data1[i][0])
        #     my_data['count'].append(data1[0][i])
        # print(my_data)
        # print(test)
        cursor.close()
        conn.close()

        # data = [data.count(i) for i in set(data)]
        name = []
        all_time = []
        import time
        times = '%Y-%m-%d'
        # for i in all_data:

        times = [time.strftime(times, time.localtime(float(i.timeIn) / 1000)) for i in all_data]
        for i in data:
            if i not in name:
                name.append(i)
        for i in times:
            if i not in all_time:
                all_time.append(i)

        # 获取每日浏览次数
        day_data = ViewsByDay.objects.all().order_by('date')
        day = [i.date.strftime('%Y-%m-%d') for i in day_data]
        day_data = [i.views_count for i in day_data]
        return render(request, 'test1.html', {
            'data': json.dumps(data),
            'name': json.dumps(name),
            'all_time': json.dumps(all_time),
            'data1': json.dumps(data1),
            'date_li': json.dumps(date_li),
            'day_data': json.dumps(day_data),
            'day': json.dumps(day),
        })
