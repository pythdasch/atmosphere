# -*- coding:utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions
from blog.models import Article, Category, ArticleImages


class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'content','meta_keywords','meta_description',)

translator.register(Article, ArticleTranslationOptions)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'description','meta_keywords','meta_description',)

translator.register(Category, CategoryTranslationOptions)

class ArticleImagesTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(ArticleImages, ArticleImagesTranslationOptions)
