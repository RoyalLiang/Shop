from Shop.celery import app
from .models import Visitor
import json


@app.task
def views_count_save(request):
    if request.META.get('HTTP_X_FORWARDED_FOR', None):
        in_ip = request.META['HTTP_X_FORWARDED_FOR']
    else:
        in_ip = request.META['REMOTE_ADDR']
    data_json = request.POST.get('data', None)
    if data_json:
        obj = {}
        data_dic = json.loads(data_json)
        obj['in_ip'] = in_ip
        obj['pub_ip'] = data_dic.get('ip', None)
        obj['address'] = data_dic.get('address', None)
        user_agent = data_dic.get('user_agent', None)
        if user_agent:
            user_agent_dic = json.loads(user_agent)
            user_agent = "%s:%s" % (user_agent_dic['terminal'], user_agent_dic['browser'])
        obj['user_agent'] = user_agent
        tjArr = data_dic.get('tjArr', None)
        url = None
        refer = None
        timeIn = None
        time = None
        timeOut = None
        if tjArr:
            tjArr_dic = json.loads(tjArr)
            url = tjArr_dic.get('url', None)
            refer = tjArr_dic.get('refer', None)
            timeIn = tjArr_dic.get('timeIn', None)
            time = tjArr_dic.get('time', None)
            timeOut = tjArr_dic.get('timeOut', None)
        obj['url'] = url
        obj['refer'] = refer
        obj['timeIn'] = str(timeIn)
        obj['time'] = time
        obj['timeOut'] = str(timeOut)
        Visitor(**obj).save()
        return True
    return False
