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


translator.register(News, NewsTranslationOptions)
translator.register(CompanyIntroduction, CompanyIntroductionTranslationOptions)
translator.register(Factory, FactoryTranslationOptions)
translator.register(Customer, CustomerTranslationOptions)
translator.register(Index, IndexTranslationOptions)
