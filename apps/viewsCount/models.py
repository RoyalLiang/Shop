from datetime import datetime
from django.db import models


class Visitor(models.Model):
    '''
    访客信息
    '''
    ip = models.GenericIPAddressField(verbose_name='IP')
    refer = models.URLField(verbose_name='来源', null=True, blank=True)
    user_agent = models.CharField(max_length=500, verbose_name='浏览器信息', null=True, blank=True)
    address = models.CharField(max_length=500, verbose_name='ip地区', null=True, blank=True)
    count = models.IntegerField(default=1, verbose_name='访问次数', blank=True)
    time = models.DateTimeField(default=datetime.now, verbose_name='时间', blank=True)

    class Meta:
        verbose_name = '访客信息'
        verbose_name_plural = verbose_name
        unique_together = []

    def __str__(self):
        return self.ip + "--" + str(self.count)
