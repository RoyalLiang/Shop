from django.db import models


class Visitor(models.Model):
    '''
    访客信息
    '''
    in_ip = models.GenericIPAddressField(verbose_name='内网')
    pub_ip = models.GenericIPAddressField(verbose_name='公网')
    url = models.URLField(verbose_name='url', null=True, blank=True)
    refer = models.URLField(verbose_name='来源', null=True, blank=True)
    timeIn = models.CharField(max_length=16, verbose_name='进入时间戳', null=True, )
    time = models.IntegerField(verbose_name='停留时间', null=True, )
    timeOut = models.CharField(max_length=16, verbose_name='离开时间戳', null=True, )
    user_agent = models.CharField(max_length=500, verbose_name='浏览器信息', null=True, blank=True)
    address = models.CharField(max_length=500, verbose_name='ip地区', null=True, blank=True)

    class Meta:
        verbose_name = '访客信息'
        verbose_name_plural = verbose_name
        unique_together = []

    def __str__(self):
        return '%s/%s' % (self.pub_ip, self.in_ip)
