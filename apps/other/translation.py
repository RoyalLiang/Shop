from modeltranslation.translator import translator, TranslationOptions
from .models import *


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'detail',)


class CompanyIntroductionTranslationOptions(TranslationOptions):
    fields = ('name', 'detail', 'addr')


class FactoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class CustomerTranslationOptions(TranslationOptions):
    fields = ('title',)


class IndexTranslationOptions(TranslationOptions):
    fields = ('title', 'keywords', 'description')


class PageInformationTranslationOptions(TranslationOptions):
    fields = ('product_info', 'video_info', 'customer_info', 'factory_info', 'news_info')


class BrandsTranslationOptions(TranslationOptions):
    fields = ('name', 'desc')


translator.register(News, NewsTranslationOptions)
translator.register(CompanyIntroduction, CompanyIntroductionTranslationOptions)
translator.register(Factory, FactoryTranslationOptions)
translator.register(Customer, CustomerTranslationOptions)
translator.register(Index, IndexTranslationOptions)
translator.register(PageInformation, PageInformationTranslationOptions)
translator.register(Brands, BrandsTranslationOptions)
