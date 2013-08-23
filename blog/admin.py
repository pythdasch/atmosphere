from django.contrib import admin
from blog.models import Article, Category, Contact
from modeltranslation.admin import TranslationAdmin


class ArticleAdmin(TranslationAdmin):
    # sets values for how the admin site lists your products
    list_display = ('title', 'author', 'created_at', 'pub_date',)
    list_display_links = ('title', 'created_at')
    list_per_page = 20
    ordering = ['-created_at']
    search_fields = ['title', 'content', 'meta_keywords', 'meta_description']
    # sets up slug to be generated from product title
    prepopulated_fields = {'slug': ('title',)}

    def formfield_for_dbfield(self, db_field, **kwargs):
        field = super(ArticleAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        self.patch_translation_field(db_field, field, **kwargs)
        return field

    class Media:
        js = ('/static/tiny_mce/tiny_mce.js', )
    # registers your product model with the admin site
admin.site.register(Article, ArticleAdmin)


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
