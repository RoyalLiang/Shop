from datetime import datetime
from django.db import models
from mdeditor.fields import MDTextField


# Create your models here.

# class GoodsCategory(models.Model):
#     """
#     商品分类
#     """
#     name = models.CharField(max_length=16, null=True, blank=True, verbose_name='类别名', help_text='类别名')
#     add_time = models.DateField(default=datetime.now, verbose_name='添加时间')
#
#     class Meta:
#         verbose_name = '商品分类'
#         verbose_name_plural = verbose_name
#
#     def __str__(self):
#         return self.name