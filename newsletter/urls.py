# -*- coding:utf-8 -*-
from django.conf.urls.defaults import *


urlpatterns = patterns('',
    url(r'^subscribe/(?P<object_id>\d+)/$', 'newsletter.views.subscribe', \
        name='subscriber_view'),
    url(r'^sub_success/(?P<object_id>\d+)/$', 'newsletter.views.sub_success'),
    url(r'^unsubscribe/(?P<object_id>\d+)/(?P<subscriber_id>\d+)$', 'newsletter.views.unsubscribe'),
    url(r'^(?P<object_id>\d+)/$', 'newsletter.views.newsletterview', \
        name='newsletter_view'),
)
