# -*- coding:utf-8 -*-
from modeltranslation.translator import translator, TranslationOptions
from general_config.models import Edito


class EditoTranslationOptions(TranslationOptions):
    fields = ('texte',)

translator.register(Edito, EditoTranslationOptions)
