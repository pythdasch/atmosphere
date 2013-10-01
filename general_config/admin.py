# -*- coding:utf-8 -*-
from django.contrib import admin
from general_config.models import Partenaire, MainSlider, Edito, SocialNetwork
from modeltranslation.admin import TranslationAdmin


admin.site.register(Partenaire)
admin.site.register(MainSlider)
admin.site.register(SocialNetwork)


class EditoAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/js/jquery-1.9.1.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/js/textedito.js',
            'filebrowser/js/TinyMCEAdmin.js',
        )
        css = {'screen': ('modeltranslation/css/tabbed_translation_fields.css',),}


class MyTranslatedEditoAdmin(EditoAdmin, TranslationAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(MyTranslatedEditoAdmin,
        self).formfield_for_dbfield(db_field, **kwargs)
        self.patch_translation_field(db_field, field, **kwargs)
        return field

admin.site.register(Edito, MyTranslatedEditoAdmin)
