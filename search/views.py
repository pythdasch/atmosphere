# -*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from search import posts, store
from atmosphere.settings_general import POST_PER_PAGE
from outils.textutils import encode
import sys

def results(request, template_name="search/results.html"):
    # get current search phrase
    q = request.GET.get('q', '')
    reload(sys)
    sys.setdefaultencoding("latin-1")
    q = encode(str(q))

    # get current page number. Set to 1 is missing or invalid
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        page = 1
    # retrieve the matching products
    matching = posts(q).get('posts')
    # generate the pagintor object
    paginator = Paginator(matching, POST_PER_PAGE)
    try:
        results = paginator.page(page).object_list
    except (InvalidPage, EmptyPage):
        results = paginator.page(1).object_list
    # store the search
    store(request, q)
    # the usual...
    page_title = 'Search Results for: ' + q
    return render_to_response(template_name, locals(),
    context_instance=RequestContext(request))
