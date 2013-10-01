# -*- coding:utf-8 -*-
from django import template
from search.forms import SearchForm
from blog.models import last_articles, Category
from outils.dateutils import prev_month, convert_to_list_month
from general_config.models import Edito, SocialNetwork
import datetime

register = template.Library()


@register.inclusion_tag("tags/sidebar.html")
def sidebar_box(request):
    linked = SocialNetwork.objects.get(name='linkedin')
    viadeo = SocialNetwork.objects.get(name="viadeo")
    google = SocialNetwork.objects.get(name="google")
    today = datetime.date.today()
    edito = Edito.objects.order_by('-created_at')[0]
    stop_day = prev_month(today, 3)
    archives = convert_to_list_month(stop_day, today)
    articles = last_articles(length=4)
    categories = Category.actifs.all()
    q = request.GET.get('q', '')
    form = SearchForm({'q': q})
    return {
    'linked':linked,
    'viadeo': viadeo,
    'google': google,
    'edito': edito,
    'archives': archives,
    'form': form,
    'last_articles': articles,
    'categories': categories,
    }
