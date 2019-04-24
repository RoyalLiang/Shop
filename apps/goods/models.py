from datetime import datetime

from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.
class GoodsSeries(models.Model):
    '''
    商品系列
    '''
    name = models.CharField(max_length=50, unique=True, verbose_name='系列名', help_text='系列名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品系列'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# class GoodsCategory(models.Model):
#     """
#     商品分类
#     """
#     name = models.CharField(max_length=50, unique=True, verbose_name='类别名', help_text='类别名')
#     # series = models.ForeignKey(GoodsSeries, verbose_name='系列', on_delete=models.CASCADE)
#     add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
#
#     class Meta:
#         verbose_name = '商品分类'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name


class Goods(models.Model):
    """
    商品信息
    """
    series = models.ForeignKey(GoodsSeries, on_delete=models.CASCADE, verbose_name='商品系列', null=True)
    name = models.CharField(max_length=100, verbose_name='商品名', help_text='商品名')
    goods_sn = models.CharField(max_length=128, unique=True, verbose_name='商品编码')
    goods_front_img = models.ImageField(upload_to='goods/images', verbose_name='商品封面')
    desc = models.TextField(blank=True, verbose_name='商品描述', null=True)
    detail = MDTextField(verbose_name='商品详情', default='', blank=True, null=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    attr = models.ManyToManyField('GoodsAttributes', related_name='goods', verbose_name='商品属性')
    title = models.CharField(max_length=100, blank=True, verbose_name='title', default='', null=True)
    keywords = models.CharField(max_length=100, blank=True, verbose_name='keywords', default='', null=True)
    description = models.CharField(max_length=100, blank=True, verbose_name='description', default='', null=True)
    leval = models.IntegerField(verbose_name='权重', default=0)

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class GoodsImage(models.Model):
    """
    商品轮播图
    """
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name='商品')
    image = models.ImageField(upload_to='goods/banner', verbose_name='商品轮播图')
    index = models.IntegerField(default=0, verbose_name='轮播顺序（第一个轮播图必须为0）')
    alt = models.CharField(max_length=100, verbose_name='图片alt', blank=True, null=True, )
    title = models.CharField(max_length=100, verbose_name='图片title', blank=True, null=True, )
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')


    class Meta:
        verbose_name = '商品轮播图'
        verbose_name_plural = verbose_name
        unique_together = ['goods', 'index']

    def __str__(self):
        return self.goods.name


class Banner(models.Model):
    """
    首页轮播图
    """
    title = models.CharField(default='', max_length=128, verbose_name='标题')
    image = models.ImageField(upload_to='banner', max_length=512, verbose_name='轮播图')
    url = models.URLField(max_length=256, verbose_name='访问地址', blank=True, null=True, )
    index = models.IntegerField(default=0, unique=True, verbose_name='轮播顺序（第一个轮播图必须为0）')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    alt = models.CharField(max_length=100, verbose_name='图片alt', blank=True, null=True)

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class GoodsAttributes(models.Model):
    '''
    商品属性
    '''
    name = models.CharField(max_length=100, verbose_name='属性名', help_text='属性名')
    weight = models.IntegerField(default=0, verbose_name='属性权重', help_text='属性权重')
    value = models.CharField(max_length=100, verbose_name='属性值', help_text='属性值')

    class Meta:
        verbose_name = '商品属性'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name + ":" + self.value


#  3-10

class Message(models.Model):
    '''
    留言板内容
    '''
    inquire = models.CharField(max_length=100, verbose_name='商品型号')
    name = models.CharField(max_length=100, verbose_name='游客', help_text='游客')
    phone = models.CharField(max_length=15, blank=True, verbose_name='手机号', help_text='手机号')
    email = models.EmailField(max_length=100, verbose_name='邮箱', blank=True, null=True)
    address = models.CharField(max_length=1000, verbose_name='地址', blank=True, null=True)
    message = models.TextField(verbose_name='留言')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='留言时间')

    class Meta:
        verbose_name = '留言板内容'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.message


class Video(models.Model):
    '''
    视频
    '''
    title = models.CharField(max_length=1000, help_text='视频标题', verbose_name='视频标题')
    video = models.FileField(upload_to='video/', verbose_name='视频(MP4、FLV)')
    image = models.CharField(default='none', max_length=512, null=True, verbose_name='封面(不用手动添加此项)', blank=True)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '视频'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
