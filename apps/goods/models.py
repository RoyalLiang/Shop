from datetime import datetime
from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.

class GoodsCategory(models.Model):
    """
    商品分类
    """
    name = models.CharField(max_length=16, null=True, blank=True, verbose_name='类别名', help_text='类别名')

    class Meta:
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name


class Goods(models.Model):
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name='商品类别')
    name = models.CharField(max_length=100, blank=True, verbose_name='商品名', help_text='商品名')
    img = models.ImageField(upload_to='goods/images', verbose_name='商品图片')
    desc = models.CharField(max_length=100, blank=True, verbose_name='商品描述')
    detail = MDTextField(verbose_name='商品详情')
    add_time = models.DateField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name
