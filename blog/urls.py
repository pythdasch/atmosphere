from django.conf.urls import patterns, url


urlpatterns = patterns('',
    # Examples:
    url(r'^article/(?P<article_slug>[-\w]+)/$', \
        'blog.views.article', name='article'),
    url(r'^(?P<category_slug>[-\w]+)/$', \
        'blog.views.single_category', name='single_category'),
)
