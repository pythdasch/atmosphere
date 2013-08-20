# -*- coding:utf-8 -*-
from django import template
from blog.models import Category, last_articles
from gallery.models import Gallery

register = template.Library()


@register.inclusion_tag("tags/footer_slider.html")
def footer_slider(request):

    return {
    'categories': categories,
    }


@register.inclusion_tag("tags/gallery_tag.html")
def gallery_tag():
    galleries = Gallery.objects.all()
    return {
    'galleries': galleries,
    }
