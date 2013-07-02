# -*- coding:utf-8 -*-
from django.shortcuts import render
from blog.models import Article, Category


def index(request):
    categories = Category.objects.select_related().all()
    articles = Article.objects.all()
    return render(request, 'index.html', {
        'articles': articles,
        'categories': categories,
        })
