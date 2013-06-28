# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Image.credit'
        db.delete_column(u'gallery_image', 'credit')

        # Deleting field 'Image.pub_date'
        db.delete_column(u'gallery_image', 'pub_date')

        # Adding field 'Image.name'
        db.add_column(u'gallery_image', 'name',
                      self.gf('django.db.models.fields.CharField')(default=1, max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Image.credit'
        db.add_column(u'gallery_image', 'credit',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'Image.pub_date'
        db.add_column(u'gallery_image', 'pub_date',
                      self.gf('django.db.models.fields.DateTimeField')(default=1),
                      keep_default=False)

        # Deleting field 'Image.name'
        db.delete_column(u'gallery_image', 'name')


    models = {
        u'gallery.image': {
            'Meta': {'object_name': 'Image'},
            'display_caption': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'width': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['gallery']