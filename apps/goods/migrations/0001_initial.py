# Generated by Django 2.1.7 on 2019-03-13 23:16

import datetime
from django.db import migrations, models
import django.db.models.deletion
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=128, verbose_name='标题')),
                ('image', models.ImageField(blank=True, max_length=512, upload_to='banner', verbose_name='轮播图')),
                ('url', models.URLField(blank=True, max_length=256, verbose_name='访问地址')),
                ('index', models.IntegerField(blank=True, default=0, unique=True, verbose_name='轮播顺序')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='商品名', max_length=100, verbose_name='商品名')),
                ('goods_sn', models.CharField(blank=True, max_length=128, null=True, verbose_name='商品编码')),
                ('goods_front_img', models.ImageField(blank=True, upload_to='goods/images', verbose_name='商品封面')),
                ('desc', models.TextField(blank=True, null=True, verbose_name='商品描述')),
                ('detail', mdeditor.fields.MDTextField(blank=True, default='', verbose_name='商品详情')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '商品',
                'verbose_name_plural': '商品',
            },
        ),
        migrations.CreateModel(
            name='GoodsAttributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='属性名', max_length=100, verbose_name='属性名')),
                ('value', models.CharField(blank=True, help_text='属性值', max_length=100, verbose_name='属性值')),
            ],
            options={
                'verbose_name': '商品属性',
                'verbose_name_plural': '商品属性',
            },
        ),
        migrations.CreateModel(
            name='GoodsCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='类别名', max_length=16, unique=True, verbose_name='类别名')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '商品分类',
                'verbose_name_plural': '商品分类',
            },
        ),
        migrations.CreateModel(
            name='GoodsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='goods/banner', verbose_name='商品轮播图')),
                ('image_url', models.URLField(blank=True, max_length=500, null=True, verbose_name='访问地址')),
                ('index', models.IntegerField(blank=True, unique=True, verbose_name='轮播顺序')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('goods', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='goods.Goods', verbose_name='商品')),
            ],
            options={
                'verbose_name': '商品轮播图',
                'verbose_name_plural': '商品轮播图',
            },
        ),
        migrations.CreateModel(
            name='GoodsSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, help_text='系列名', max_length=16, unique=True, verbose_name='系列名')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '商品系列',
                'verbose_name_plural': '商品系列',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inquire', models.CharField(blank=True, max_length=100, verbose_name='商品型号')),
                ('name', models.CharField(blank=True, help_text='游客', max_length=100, verbose_name='游客')),
                ('phone', models.CharField(blank=True, help_text='手机号', max_length=15, verbose_name='手机号')),
                ('email', models.EmailField(blank=True, max_length=100, verbose_name='邮箱')),
                ('address', models.CharField(blank=True, max_length=1000, verbose_name='地址')),
                ('message', models.TextField(blank=True, verbose_name='留言')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='留言时间')),
            ],
            options={
                'verbose_name': '留言板内容',
                'verbose_name_plural': '留言板内容',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, help_text='视频标题', max_length=1000, verbose_name='视频标题')),
                ('video', models.FileField(blank=True, upload_to='video/', verbose_name='视频')),
                ('add_time', models.DateField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '视频',
                'verbose_name_plural': '视频',
            },
        ),
        migrations.AddField(
            model_name='goodscategory',
            name='series',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsSeries', verbose_name='系列'),
        ),
        migrations.AddField(
            model_name='goods',
            name='attr',
            field=models.ManyToManyField(blank=True, related_name='goods', to='goods.GoodsAttributes', verbose_name='商品属性'),
        ),
        migrations.AddField(
            model_name='goods',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='goods.GoodsCategory', verbose_name='商品类别'),
        ),
    ]
