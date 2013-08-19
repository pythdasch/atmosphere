from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^$', 'support.views.index', \
        name='support_index'),
    url(r'^login/$', 'support.views.login_in', \
        name='support_login'),
)
