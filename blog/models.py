# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import datetime
import random
import tagging


def all_articles():
    return Article.objects.all()

def last_articles(length=12):
    try:
        articles = Article.objects.order_by('-created_at')[:length]
    except:
        raise Exception('Not enough articles for this query')
    return articles

def categories_article(category_name, length=5):
    category = Category.objects.filter(name=category_name)
    return Article.objects.filter(categories=category)[:length]

def oneofeach():
    try:
        categories = Category.objects.all()
        eachlist = []
        for category in categories:
            try:
                article = Article.objects.order_by('-created_at')[0]
                eachlist.append(article)
            except:
                pass
    except:
        raise Exception('There is no articles for this query')
    return eachlist

def articles_aleatoires(length=3):
    all_articles = Article.objects.all()
    if length > len(all_articles):
        length = len(all_articles)
    random_articles = random.sample(set(all_articles), length)
    return random_articles


class ActiveCategoryManager(models.Manager):
    def get_query_set(self):
        return super(ActiveCategoryManager, self).get_query_set().filter(is_active=True)


class Category(models.Model):
    name = models.CharField("Nom de la catégorie", max_length=50, help_text="le nom est affiché dans le site comme tel. Faites attention")
    slug = models.SlugField(max_length=50, unique=True,
    help_text='Unique value for product page URL, created from name.')
    description = models.TextField("Description de la catégorie.")
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords", max_length=255,
    help_text='Mots séparés de virgules pour le référencement')
    meta_description = models.CharField("Meta Description", max_length=255,
    help_text='Content for description meta tag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    actifs = ActiveCategoryManager()

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __unicode__(self):
        return self.name

    @models.permalink
    def get_absolute_url(self):
        return ('catalog_category', (), {'category_slug': self.slug})


class ActifArtManager(models.Manager):
    def get_query_set(self):
        now = datetime.datetime.now()
        return super(ActifArtManager, self).get_query_set().filter(pub_date__gte=now, is_active=True)


class ArticleManager(models.Manager):
    """return the popular article"""


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=50, help_text="Cet élèment n'est pas à modifier. Il permet de passer de page en page.")
    content = models.TextField()
    author = models.ForeignKey(User, help_text="Veuillez choisir votre auteur")
    image = models.ImageField(upload_to='article/image/', blank=True, null=True)
    meta_keywords = meta_keywords = models.CharField("Meta Keywords", max_length=255,
    help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", max_length=255,
    help_text='Content for description meta tag')
    is_active = models.BooleanField("est actif ?", help_text="Ce bouton vous permet d'activer la publication tout de suite ou alors de désactiver un article.")
    pub_date = models.DateField("Date de publication", help_text="Veuillez choisir la date à laquelle l'article sera publié")
    created_at = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category)

    objects = ArticleManager()
    published = ActifArtManager()

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = u'Articles'

    def __unicode__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=75)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'contacts'

    def __unicode__(self):
        return self.name +' : '+ self.subject


class Metakeys(models.Model):
    titre = models.CharField(max_length=100, help_text="Le titre correspond à ce que l'on verra sur l'onglet du site. Le titre du site doit être court.")
    meta_keys = models.CharField(max_length=255, help_text="Les Meta-Keys sont des clefs utilisés par google pour définir un site\
        Il faut séparé chaque mot par une virgule.")
    meta_descriptions = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Metakeys'

#Django-tagging
tagging.register(Article)
