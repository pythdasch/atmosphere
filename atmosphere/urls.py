from django.conf.urls import patterns, include, url
from settings import STATIC_ROOT, MEDIA_ROOT
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from filebrowser.sites import site

admin.autodiscover()

js_info_dict = {
    'domain': 'djangojs',
    'packages': ('atmosphere',),
}

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'atmosphere.views.coming_soon', name='index'),
    url(r'^test/$', 'atmosphere.views.index',),
    url(r'^contact/$', 'atmosphere.views.contact',),
    url(r'^blog/', include('blog.urls')),
    url(r'^support/', include('support.urls')),
    url(r'^admin/filebrowser/', include(site.urls)),
    (r'^search/', include('search.urls')),
    # url(r'^atmosphere/', include('atmosphere.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^grappelli/', include('grappelli.urls')),
    (r'^galleries/', include('gallery.urls')),
    (r'^newsletter/', include('newsletter.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),
    (r'^i18n/', include('django.conf.urls.i18n')),
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog', js_info_dict),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'atmosphere.views.custom404'
handler500 = 'atmosphere.views.custom500'
