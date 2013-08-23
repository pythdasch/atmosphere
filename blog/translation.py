
from modeltranslation.translator import translator, TranslationOptions
from blog.models import Article, Category

class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'content','meta_keywords','meta_description',)

translator.register(Article, ArticleTranslationOptions)
