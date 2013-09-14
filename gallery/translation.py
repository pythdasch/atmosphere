# -*- coding:utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions
from gallery.models import Gallery, Author


class GalleryTranslationOptions(TranslationOptions):
    fields = ('name', 'description','meta_keywords','meta_description',)

translator.register(Gallery, GalleryTranslationOptions)

class AuthorTranslationOptions(TranslationOptions):
    fields = ('name', 'biography')

translator.register(Author, AuthorTranslationOptions)
