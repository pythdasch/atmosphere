from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    url(r'^article/(?P<article_slug>[-\w]+)/$', \
        'blog.views.single_article', name='article'),
    url(r'^(?P<category_slug>[-\w]+)/$', \
        'blog.views.single_category', name='single_category'),
    url(r'^archive/(?P<year>[-\w]+)/(?P<month>[-\w]+)$', 'blog.views.archive_view')
)
