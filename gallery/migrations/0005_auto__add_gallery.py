# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Gallery'
        db.create_table(u'gallery_gallery', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal(u'gallery', ['Gallery'])

        # Adding M2M table for field photos on 'Gallery'
        db.create_table(u'gallery_gallery_photos', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gallery', models.ForeignKey(orm[u'gallery.gallery'], null=False)),
            ('image', models.ForeignKey(orm[u'gallery.image'], null=False))
        ))
        db.create_unique(u'gallery_gallery_photos', ['gallery_id', 'image_id'])


    def backwards(self, orm):
        # Deleting model 'Gallery'
        db.delete_table(u'gallery_gallery')

        # Removing M2M table for field photos on 'Gallery'
        db.delete_table('gallery_gallery_photos')


    models = {
        u'gallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'description': ('tinymce.models.HTMLField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photos': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['gallery.Image']", 'symmetrical': 'False'})
        },
        u'gallery.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['gallery']