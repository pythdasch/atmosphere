# -*- coding:utf-8 -*-
from django import template
from blog.models import Category, articles_aleatoires
from gallery.models import Gallery

register = template.Library()


@register.inclusion_tag("tags/footer_slider.html")
def footer_slider(request):
    slider_article = articles_aleatoires(length=8)
    return {
    'slider_article': slider_article,
    }


@register.inclusion_tag("tags/gallery_tag.html")
def gallery_tag():
    galleries = Gallery.objects.all()
    return {
    'galleries': galleries,
    }
