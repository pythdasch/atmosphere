# -*- coding:utf-8 -*-
from django.contrib import admin
from blog.models import Article, Category, Contact, Metakeys
from modeltranslation.admin import TranslationAdmin


class ArticleAdmin(admin.ModelAdmin):
    # sets values for how the admin site lists your products
    list_display = (u'title', u'author', u'created_at', u'pub_date',)
    list_display_links = (u'title', u'created_at')
    list_per_page = 20
    ordering = [u'-created_at']
    search_fields = [u'title', u'content', u'meta_keywords', u'meta_description']
    # sets up slug to be generated from product title
    prepopulated_fields = {u'slug': (u'title',)}

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/js/jquery-1.9.1.js',
            '/static/js/textarea.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'filebrowser/js/TinyMCEAdmin.js',

        )
        css = {'screen': ('modeltranslation/css/tabbed_translation_fields.css',),}



class MyTranslatedArticleAdmin(ArticleAdmin, TranslationAdmin):
    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(MyTranslatedArticleAdmin,
        self).formfield_for_dbfield(db_field, **kwargs)
        self.patch_translation_field(db_field, field, **kwargs)
        # override the TinyMCE language settings for this field's widget
        return field

admin.site.register(Article, MyTranslatedArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
#sets up values for how admin site lists categories
    list_display = ('name', 'created_at', 'updated_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description']
    # sets up slug to be generated from category
admin.site.register(Category, CategoryAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at',)


admin.site.register(Contact, ContactAdmin)

class MetakeysAdmin(admin.ModelAdmin):
    list_display = ('titre', 'meta_keys')

admin.site.register(Metakeys, MetakeysAdmin)
