# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Subscriber.language'
        db.add_column(u'newsletter_subscriber', 'language',
                      self.gf('django.db.models.fields.CharField')(default='en', max_length=3),
                      keep_default=False)

        # Adding unique constraint on 'Subscriber', fields ['email']
        db.create_unique(u'newsletter_subscriber', ['email'])


    def backwards(self, orm):
        # Removing unique constraint on 'Subscriber', fields ['email']
        db.delete_unique(u'newsletter_subscriber', ['email'])

        # Deleting field 'Subscriber.language'
        db.delete_column(u'newsletter_subscriber', 'language')


    models = {
        u'newsletter.newsletter': {
            'Meta': {'ordering': "['id']", 'object_name': 'Newsletter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['newsletter.Subscriber']", 'null': 'True', 'blank': 'True'})
        },
        u'newsletter.subscriber': {
            'Meta': {'ordering': "['id']", 'object_name': 'Subscriber'},
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        }
    }

    complete_apps = ['newsletter']