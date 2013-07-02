# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from models import Article, Category


def article(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    return render(request, 'article.html', {
        'article': article,
        })


def single_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    return render(request, 'blog/category.html', {
        'category': category,
        })
