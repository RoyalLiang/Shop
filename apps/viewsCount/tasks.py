from Shop.celery import app
from django.core.mail import send_mail
from django.db.models import Count
from django.conf import settings
from other.models import UserContactInfo
from .models import Visitor, ViewsByDay, DeviceByDay, RegionByDay, ReferByDay
import json
from goods.models import Message
import time
from datetime import datetime


@app.task
def views_count_save(data):
    '''
    搜集用户访问信息
    :param data:
    :return:
    '''
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
            if not isinstance(tjArr_dic, dict):
                return False
            url = tjArr_dic.get('url', None)
            refer = tjArr_dic.get('refer', '')
            timeIn = tjArr_dic.get('timeIn', None)
            time = tjArr_dic.get('time', None)
            timeOut = tjArr_dic.get('timeOut', None)
        obj['url'] = url
        obj['refer'] = refer
        obj['timeIn'] = int(timeIn)
        obj['time'] = time
        obj['timeOut'] = int(timeOut)
        Visitor(**obj).save()
        return True
    return False


@app.task
def send_goods_email(message):
    '''
    商品详细页面询盘通知
    :param message:
    :return:
    '''
    Message.objects.create(**message).save()
    email_title = 'Test'
    email_body = '用户名：{}，邮箱：{},对货号{}发送了一个请求,内容:{}，请在第一时间处理。'.format(message['name'], message['email'],
                                                                    message['inquire'], message['message'])
    send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [settings.ADMIN_EMAIL])
    if send_status:
        return True
    return False


@app.task
def send_contact_email(data):
    '''
    联系页面询盘通知
    :param data:
    :return:
    '''
    UserContactInfo.objects.create(**data).save()
    email_title = 'Test'
    email_body = '用户名：{}，邮箱：{},联系我们了,所属国家{},内容:{}，请在第一时间处理。'.format(data['name'], data['email'], data['country'],
                                                                    data['message'])
    send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [settings.ADMIN_EMAIL])
    if send_status:
        return True
    return False


@app.task
def data_processing():
    '''
    数据统计
    :return:
    '''
    start = time.mktime(
        time.strptime("%s 00:00:00" % time.strftime("%Y-%m-%d", time.localtime(time.time())),
                      "%Y-%m-%d %H:%M:%S")) - 24 * 60 * 60
    end = int(start) + 24 * 60 * 60 - 1

    views_count = Visitor.objects.filter(timeIn__range=(start * 1000, end * 1000)).count()
    ip_count = Visitor.objects.filter(timeIn__range=(start * 1000, end * 1000)).values('pub_ip').distinct().count()
    # 每日访问量
    if not ViewsByDay.objects.filter(date=datetime.now()).exists():
        ViewsByDay.objects.create(views_count=views_count, ip_count=ip_count)

    res = Visitor.objects.filter(timeIn__range=(start * 1000, end * 1000)).values('address').annotate(Count('address'))
    # 地区统计
    for i in res:
        if not RegionByDay.objects.filter(date=datetime.now(), region=i['address']).exists():
            RegionByDay.objects.create(region=i['address'], views_count=i['address__count'])

    mobile_count = Visitor.objects.filter(timeIn__range=(start * 1000, end * 1000),
                                          user_agent__regex='(iPhone|iPod|iPad|Android|BlackBerry|Mobile){1}').count()
    pc_count = views_count - mobile_count
    # 设备统计
    if not DeviceByDay.objects.filter(date=datetime.now()).exists():
        DeviceByDay.objects.create(pc_count=pc_count, mobile_count=mobile_count)

    search_engine_count = Visitor.objects.filter(timeIn__range=(start * 1000, end * 1000),
                                                 refer__regex='(google.com|yahoo.com|bing.com|go.com|ceek.jp|naver.com|cusco.pt|ciao.es|apali.com){1}').count()
    website_in_count = Visitor.objects.filter(timeIn__range=(start * 1000, end * 1000),
                                              refer__regex=settings.HOST_NAME).count()
    input_count = Visitor.objects.filter(timeIn__range=(start * 1000, end * 1000),
                                         refer='').count()
    other_count = views_count - search_engine_count - website_in_count - input_count
    # 来源统计
    if not ReferByDay.objects.filter(date=datetime.now()).exists():
        ReferByDay.objects.create(search_engine_count=search_engine_count, website_in_count=website_in_count,
                                  input_count=input_count, other_count=other_count)
