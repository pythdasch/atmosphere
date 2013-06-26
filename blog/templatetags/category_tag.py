from django import template
from blog.models import Category
from photologue.models import Gallery

register = template.Library()


@register.inclusion_tag("tags/category_nav.html")
def category_nav(request):
    categories = Category.actifs.all()
    return {
    'categories': categories,
    }


@register.inclusion_tag("tags/gallery_tag.html")
def gallery_tag():
    galleries = Gallery.objects.all()
    return {
    'galleries': galleries,
    }
