from modeltranslation.translator import translator, TranslationOptions
from .models import *


class GoodsTranslationOptions(TranslationOptions):
    fields = ('name', 'desc', 'detail', 'title', 'keywords', 'description')


class GoodsSeriesTranslationOptions(TranslationOptions):
    fields = ('name',)


class GoodsCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class GoodsImageTranslationOptions(TranslationOptions):
    fields = ('alt', 'title')


class BannerTranslationOptions(TranslationOptions):
    fields = ('title', 'alt')


class GoodsAttributesTranslationOptions(TranslationOptions):
    fields = ('name', 'value')


class VideoTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Goods, GoodsTranslationOptions)
translator.register(GoodsSeries, GoodsSeriesTranslationOptions)
translator.register(GoodsCategory, GoodsCategoryTranslationOptions)
translator.register(GoodsImage, GoodsImageTranslationOptions)
translator.register(Banner, BannerTranslationOptions)
translator.register(GoodsAttributes, GoodsAttributesTranslationOptions)
translator.register(Video, VideoTranslationOptions)
