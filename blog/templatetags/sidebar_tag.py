# -*- coding:utf-8 -*-
from django import template
from search.forms import SearchForm
from blog.models import last_articles, Category
from outils.dateutils import prev_month, convert_to_list_month
import datetime

register = template.Library()


@register.inclusion_tag("tags/sidebar.html")
def sidebar_box(request):
    today = datetime.date.today()
    stop_day = prev_month(today, 3)
    archives = convert_to_list_month(stop_day, today)
    articles = last_articles(length=4)
    categories = Category.actifs.all()
    q = request.GET.get('q', '')
    form = SearchForm({'q': q})
    return {
    'archives': archives,
    'form': form,
    'last_articles': articles,
    'categories': categories,
    }
