from django.conf.urls.defaults import url, patterns


urlpatterns = patterns('',
    url(r'^(?P<gallery_slug>[-\w]+)/$', \
        'gallery.views.single_gallery', name='single_gallery'),
    url(r'^$', \
        'gallery.views.index_gallery', name='index_gallery'),
)
