from django import template
from search.forms import SearchForm
from blog.models import last_articles, Category

register = template.Library()


@register.inclusion_tag("tags/sidebar.html")
def sidebar_box(request):
    articles = last_articles(length=4)
    categories = Category.actifs.all()
    q = request.GET.get('q', '')
    form = SearchForm({'q': q})
    return {
    'form': form,
    'last_articles': articles,
    'categories': categories,
    }
