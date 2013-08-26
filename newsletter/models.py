# -*- coding:utf-8 -*-
from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    language = models.CharField(max_length=3)

    def __unicode__(self):
        return "Email: %s" % (self.email, )

    @models.permalink
    def get_absolute_url(self):
        return ('subscriber', None, {'object_id': self.id})

    class Meta:
        ordering = ["id"]


class Newsletter(models.Model):
    name = models.CharField(max_length=80)
    subscribers = models.ManyToManyField('Subscriber', blank=True, null=True)

    def __unicode__(self):
        return "Newsletter %s" % (self.name, )

    @models.permalink
    def get_absolute_url(self):
        return ('newsletter', None, {'object_id': self.id})

    class Meta:
        ordering = ["id"]
