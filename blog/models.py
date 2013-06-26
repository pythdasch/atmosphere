# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
import datetime
# Create your models here.


class ActiveCategoryManager(models.Manager):
    def get_query_set(self):
        return super(ActiveCategoryManager, self).get_query_set().filter(is_active=True)


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True,
    help_text='Unique value for product page URL, created from name.')
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    meta_keywords = models.CharField("Meta Keywords", max_length=255,
    help_text='Comma-delimited set of SEO keywords for meta tag')
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
    slug = models.SlugField(unique=True, max_length=50)
    content = HTMLField()
    author = models.ForeignKey(User)
    image = models.ImageField(upload_to='article/image/')
    meta_keywords = meta_keywords = models.CharField("Meta Keywords", max_length=255,
    help_text='Comma-delimited set of SEO keywords for meta tag')
    meta_description = models.CharField("Meta Description", max_length=255,
    help_text='Content for description meta tag')
    is_active = models.BooleanField()
    pub_date = models.DateField()
    created_at = models.DateField(auto_now_add=True)
    categories = models.ManyToManyField(Category)

    objects = ArticleManager()
    published = ActifArtManager()

    class Meta:
        ordering = ['-created_at']
        verbose_name_plural = 'Articles'

    def __unicode__(self):
        return self.title
