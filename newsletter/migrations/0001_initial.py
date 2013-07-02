# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subscriber'
        db.create_table(u'newsletter_subscriber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
        ))
        db.send_create_signal(u'newsletter', ['Subscriber'])

        # Adding model 'Newsletter'
        db.create_table(u'newsletter_newsletter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
        ))
        db.send_create_signal(u'newsletter', ['Newsletter'])

        # Adding M2M table for field subscribers on 'Newsletter'
        db.create_table(u'newsletter_newsletter_subscribers', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newsletter', models.ForeignKey(orm[u'newsletter.newsletter'], null=False)),
            ('subscriber', models.ForeignKey(orm[u'newsletter.subscriber'], null=False))
        ))
        db.create_unique(u'newsletter_newsletter_subscribers', ['newsletter_id', 'subscriber_id'])


    def backwards(self, orm):
        # Deleting model 'Subscriber'
        db.delete_table(u'newsletter_subscriber')

        # Deleting model 'Newsletter'
        db.delete_table(u'newsletter_newsletter')

        # Removing M2M table for field subscribers on 'Newsletter'
        db.delete_table('newsletter_newsletter_subscribers')


    models = {
        u'newsletter.newsletter': {
            'Meta': {'ordering': "['id']", 'object_name': 'Newsletter'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'subscribers': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['newsletter.Subscriber']", 'symmetrical': 'False'})
        },
        u'newsletter.subscriber': {
            'Meta': {'ordering': "['id']", 'object_name': 'Subscriber'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['newsletter']