from datetime import datetime
from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.

class News(models.Model):
    '''
    新闻
    '''
    title = models.CharField(max_length=1000, help_text='新闻标题', blank=True, verbose_name='新闻标题')
    image = models.ImageField(upload_to='news/image', verbose_name='封面图片')
    detail = MDTextField(verbose_name='新闻详情', blank=True)
    add_time = models.DateField(default=datetime.now, verbose_name='发布时间')

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class CompanyIntroduction(models.Model):
    '''
    公司信息
    '''
    name = models.CharField(max_length=100, verbose_name='公司名称', blank=True)
    detail = MDTextField(verbose_name='详细信息')
    addr = models.CharField(max_length=200, default='', verbose_name='公司地址', blank=True, null=True)
    tel = models.CharField(max_length=20, default='', verbose_name='公司电话', blank=True, null=True)
    email = models.EmailField(default='', verbose_name='公司邮箱', blank=True, null=True)
    web = models.CharField(max_length=50, default='', verbose_name='公司网站', blank=True, null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='发布时间')

    class Meta:
        verbose_name = '公司信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Factory(models.Model):
    '''
    工厂信息
    '''
    title = models.CharField(max_length=1000, help_text='厂名', verbose_name='厂名')
    image = models.ImageField(upload_to='factory/image', verbose_name='图片', )

    class Meta:
        verbose_name = '工厂信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Customer(models.Model):
    '''
    宣传客户
    '''
    title = models.CharField(max_length=1000, help_text='标题', verbose_name='标题')
    image = models.ImageField(upload_to='customer/image', verbose_name='图片', )

    class Meta:
        verbose_name = '宣传客户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Index(models.Model):
    '''
    首页关键词
    '''
    title = models.CharField(max_length=100, verbose_name='title', default='', )
    keywords = models.CharField(max_length=100, verbose_name='keywords', default='', )
    description = models.CharField(max_length=100, verbose_name='description', default='', )

    class Meta:
        verbose_name = '首页关键词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class UserContactInfo(models.Model):
    """
    用户联系信息
    """
    name = models.CharField(max_length=100, verbose_name='昵称', default='')
    phone = models.CharField(max_length=100, blank=True, null=True, verbose_name='联系电话', default='')
    email = models.EmailField(max_length=100,  verbose_name='邮箱', default='')
    country = models.CharField(max_length=100, verbose_name='国家', default='')
    message = models.TextField(verbose_name='联系内容',  default='', )
    add_time = models.DateTimeField(default=datetime.now, verbose_name='联系时间')

    class Meta:
        verbose_name = '联系我们'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name + self.country + '，发起了联系'
