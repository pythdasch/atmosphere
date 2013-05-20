from django.conf.urls import patterns, include, url
from settings import STATIC_ROOT, MEDIA_ROOT
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'atmosphere.views.index', name='index'),
    url(r'^blog/', include('blog.urls')),
    # url(r'^atmosphere/', include('atmosphere.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),
)
