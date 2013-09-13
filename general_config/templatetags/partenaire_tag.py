# -*- coding:utf-8 -*-
from django import template
from general_config.models import Partenaire
register = template.Library()


@register.inclusion_tag("tags/footer_partenaire.html")
def footer_partenaire(request):
    partenaires = Partenaire.objects.order_by('created_at')[:5]
    return {
    'partenaires': partenaires,
    }
