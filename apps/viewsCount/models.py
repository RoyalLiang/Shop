from datetime import datetime

from django.db import models


class Visitor(models.Model):
    '''
    访客信息
    '''
    in_ip = models.GenericIPAddressField(verbose_name='内网')
    pub_ip = models.GenericIPAddressField(db_index=True, verbose_name='公网')
    url = models.URLField(verbose_name='url', null=True, blank=True)
    refer = models.URLField(verbose_name='来源', null=True, blank=True)
    timeIn = models.BigIntegerField(db_index=True, verbose_name='进入时间戳', null=True, )
    time = models.IntegerField(verbose_name='停留时间', null=True, )
    timeOut = models.BigIntegerField(verbose_name='离开时间戳', null=True, )
    user_agent = models.CharField(db_index=True, max_length=500, verbose_name='浏览器信息', null=True, blank=True)
    address = models.CharField(db_index=True, max_length=500, verbose_name='ip地区', null=True, blank=True)

    class Meta:
        verbose_name = '访客信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s/%s' % (self.pub_ip, self.in_ip)

    def get_time(self):
        import time
        times = '%Y-%m-%d %H:%M:%S'
        return time.strftime(times, time.localtime(float(self.timeIn)/1000))
    get_time.short_description = '点击时间'
    all_time = property(get_time)


class ViewsByDay(models.Model):
    '''
    每日访问量统计
    '''
    date = models.DateField(unique=True, auto_now_add=True, verbose_name='日期', blank=True)
    views_count = models.IntegerField(verbose_name='浏览次数', default=0, blank=True)
    ip_count = models.IntegerField(verbose_name='ip数', default=0, blank=True)

    class Meta:
        verbose_name = '每日访问量统计'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.date


class ReferByDay(models.Model):
    '''
    每日网站访问来源统计
    '''
    date = models.DateField(unique=True, auto_now_add=True, verbose_name='日期', blank=True)
    search_engine_count = models.IntegerField(default=0, verbose_name='搜索引擎', blank=True)
    website_in_count = models.IntegerField(default=0, verbose_name='站内', blank=True)
    other_count = models.IntegerField(default=0, verbose_name='其他', blank=True)
    input_count = models.IntegerField(default=0, verbose_name='输入/书签', blank=True)

    class Meta:
        verbose_name = '每日网站访问来源统计'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.date


class DeviceByDay(models.Model):
    '''
    每日访问设备统计
    '''
    date = models.DateField(unique=True, auto_now_add=True, verbose_name='日期', blank=True)
    pc_count = models.IntegerField(default=0, verbose_name='非移动设备', blank=True)
    mobile_count = models.IntegerField(default=0, verbose_name='移动设备', blank=True)

    class Meta:
        verbose_name = '每日访问设备统计'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.date


class RegionByDay(models.Model):
    '''
    每日地区访问量统计
    '''
    region = models.CharField(max_length=50, verbose_name='地区', blank=True)
    views_count = models.IntegerField(default=0, verbose_name='浏览次数', blank=True)
    date = models.DateField(auto_now_add=True, verbose_name='日期', blank=True)

    class Meta:
        unique_together = ['region', 'date']
        verbose_name = '每日地区访问量统计'
        verbose_name_plural = verbose_name

    def __str__(self):
        return "%s-%s" % (self.region, self.date)


class TestModel(ViewsByDay):
    class Meta:
        proxy = True
        verbose_name = 'Test'
        verbose_name_plural = verbose_name

