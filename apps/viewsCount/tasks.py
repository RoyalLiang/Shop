from Shop.celery import app
from django.core.mail import send_mail
from django.conf import settings
from .models import Visitor
import json
from goods.models import Message


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


@app.task
def send_goods_email(request):
    inquire = request.POST.get('inquire', None)
    name = request.POST.get('name', None)
    phone = request.POST.get('phone', None)
    email = request.POST.get('email', None)
    address = request.POST.get('address', None)
    message = request.POST.get('message', None)
    Message.objects.create(inquire=inquire, name=name, phone=phone, email=email, address=address,
                           message=message ).save()
    email_title = 'Test'
    email_body = '用户名：{}，邮箱：{},对货号{}发送了一个请求,内容:{}，请在第一时间处理。'.format(name, email,
                                                                    inquire, message)
    send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [settings.ADMIN_EMAIL])
    if send_status:
        pass
