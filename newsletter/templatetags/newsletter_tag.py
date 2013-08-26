# -*- coding:utf-8 -*-
from django import template
from newsletter.forms import SubscriptionForm
from newsletter.models import Newsletter

register = template.Library()


@register.inclusion_tag("tags/subscribe_news.html")
def subscribe_news(request):
    news = Newsletter.objects.get(name='main')
    form = SubscriptionForm()
    return {
    'sub_form': form,
    'newsletter': news,
    }
