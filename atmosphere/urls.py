from django.conf.urls import patterns, include, url
from settings import STATIC_ROOT, MEDIA_ROOT
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'atmosphere.views.coming_soon', name='index'),
    url(r'test/^$', 'atmosphere.views.index'),
    url(r'^blog/', include('blog.urls')),
    # url(r'^atmosphere/', include('atmosphere.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^tinymce/', include('tinymce.urls')),
    (r'^galleries/', include('gallery.urls')),
    (r'^newsletter/', include('newsletter.urls')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': STATIC_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
