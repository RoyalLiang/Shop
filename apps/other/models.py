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
    title = models.CharField(max_length=1000, help_text='厂名', blank=True, verbose_name='厂名')
    image = models.ImageField(upload_to='factory/image', verbose_name='图片', blank=True, )

    class Meta:
        verbose_name = '工厂信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Customer(models.Model):
    '''
    宣传客户
    '''
    title = models.CharField(max_length=1000, help_text='标题', blank=True, verbose_name='标题')
    image = models.ImageField(upload_to='customer/image', verbose_name='图片', blank=True, )

    class Meta:
        verbose_name = '宣传客户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Index(models.Model):
    '''
    首页关键词
    '''
    title = models.CharField(max_length=100, blank=True, verbose_name='title')
    keywords = models.CharField(max_length=100, blank=True, verbose_name='keywords')
    description = models.CharField(max_length=100, blank=True, verbose_name='description')

    class Meta:
        verbose_name = '首页关键词'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
