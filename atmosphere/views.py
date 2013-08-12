# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category
from newsletter.models import Newsletter


def coming_soon(request):
    news = get_object_or_404(Newsletter, name="main")
    return render(request, 'coming_soon.html', {
        'newsletter': news,
        })

def index(request):
    categories = Category.objects.select_related().all()
    articles = Article.objects.all()
    return render(request, 'index.html', {
        'articles': articles,
        'categories': categories,
        })
