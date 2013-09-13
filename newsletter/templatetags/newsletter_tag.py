from django import template
from newsletter.forms import SubscriptionForm

register = template.Library()


@register.inclusion_tag("tags/subscribe_news.html")
def subscribe_news(request):
    form = SubscriptionForm()
    return {
    'sub_form': form,
    }
