from Shop.celery import app
from django.core.mail import send_mail
from django.conf import settings

from other.models import UserContactInfo
from .models import Visitor
import json
from goods.models import Message


@app.task
def views_count_save(data):
    in_ip = data['in_ip']
    data_json = data['data_json']
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
def send_goods_email(message):
    Message.objects.create(**message).save()
    email_title = 'Test'
    email_body = '用户名：{}，邮箱：{},对货号{}发送了一个请求,内容:{}，请在第一时间处理。'.format(message['name'], message['email'],
                                                                    message['inquire'], message['message'])
    send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [settings.ADMIN_EMAIL])
    if send_status:
        pass

@app.task
def send_contact_email(request):
    # inquire = request.POST.get('inquire', None)
    name = request.POST.get('name', None)
    phone = request.POST.get('phone', None)
    email = request.POST.get('email', None)
    country = request.POST.get('country', None)
    message = request.POST.get('message', None)
    UserContactInfo.objects.create(name=name, phone=phone, email=email, country=country,
                                   message=message).save()
    email_title = 'Test'
    email_body = '用户名：{}，邮箱：{},联系我们了,所属国家{},内容:{}，请在第一时间处理。'.format(name, email, country,
                                                                    message)
    send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [settings.ADMIN_EMAIL])
    if send_status:
        pass

