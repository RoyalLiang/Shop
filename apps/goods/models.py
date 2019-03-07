from datetime import datetime
from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.

class GoodsCategory(models.Model):
    """
    商品分类
    """
    name = models.CharField(max_length=16, null=True, blank=True, verbose_name='类别名', help_text='类别名')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Goods(models.Model):
    """
    商品信息
    """
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name='商品类别', blank=True)
    name = models.CharField(max_length=100, blank=True, verbose_name='商品名', help_text='商品名')
    goods_sn = models.CharField(max_length=128, null=True, blank=True, verbose_name='商品编码')
    goods_front_img = models.ImageField(upload_to='goods/images', verbose_name='商品封面', blank=True, null=True)
    desc = models.TextField(blank=True, verbose_name='商品描述', null=True)
    detail = MDTextField(verbose_name='商品详情', default='', blank=True)
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='商品轮播图', blank=True)
    image = models.ImageField(upload_to='goods/banner', verbose_name='商品轮播图', blank=True, null=True)
    image_url = models.CharField(max_length=500, null=True, blank=True, verbose_name='图片url')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
    首页轮播图
    """
    title = models.CharField(default='', max_length=128, blank=True, verbose_name='标题')
    image = models.ImageField(upload_to='banner', max_length=512, verbose_name='轮播图', blank=True, null=True)
    url = models.URLField(max_length=256, verbose_name='访问地址', blank=True)
    index = models.IntegerField(default=0, verbose_name='轮播顺序', blank=True)
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class GoodsAttributes(models.Model):
    '''
    商品属性
    '''
    name = models.CharField(max_length=100, blank=True, verbose_name='属性', help_text='属性')
