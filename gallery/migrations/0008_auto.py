# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field gallery on 'Image'
        m2m_table_name = db.shorten_name(u'gallery_image_gallery')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('image', models.ForeignKey(orm[u'gallery.image'], null=False)),
            ('gallery', models.ForeignKey(orm[u'gallery.gallery'], null=False))
        ))
        db.create_unique(m2m_table_name, ['image_id', 'gallery_id'])

        # Removing M2M table for field photos on 'Gallery'
        db.delete_table(db.shorten_name(u'gallery_gallery_photos'))


    def backwards(self, orm):
        # Removing M2M table for field gallery on 'Image'
        db.delete_table(db.shorten_name(u'gallery_image_gallery'))

        # Adding M2M table for field photos on 'Gallery'
        m2m_table_name = db.shorten_name(u'gallery_gallery_photos')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('gallery', models.ForeignKey(orm[u'gallery.gallery'], null=False)),
            ('image', models.ForeignKey(orm[u'gallery.image'], null=False))
        ))
        db.create_unique(m2m_table_name, ['gallery_id', 'image_id'])


    models = {
        u'gallery.gallery': {
            'Meta': {'object_name': 'Gallery'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'gallery.image': {
            'Meta': {'object_name': 'Image'},
            'gallery': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['gallery.Gallery']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['gallery']