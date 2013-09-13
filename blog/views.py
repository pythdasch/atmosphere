# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from models import Article, Category


def single_article(request, article_slug):
    article = get_object_or_404(Article, slug=article_slug)
    return render(request, 'article.html', {
        'article': article,
        })


def single_category(request, category_slug):
    categories = Category.actifs.all()
    category = get_object_or_404(Category, slug=category_slug)
    last_article = category.article_set.order_by('created_at')[0]
    return render(request, 'blog/category.html', {
        'category': category,
        'last_article': last_article,
        'categories': categories,
        })
