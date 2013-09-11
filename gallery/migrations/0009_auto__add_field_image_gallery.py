# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Image.gallery'
        db.add_column(u'gallery_image', 'gallery',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['gallery.Gallery']),
                      keep_default=False)

        # Removing M2M table for field gallery on 'Image'
        db.delete_table(db.shorten_name(u'gallery_image_gallery'))


    def backwards(self, orm):
        # Deleting field 'Image.gallery'
        db.delete_column(u'gallery_image', 'gallery_id')

        # Adding M2M table for field gallery on 'Image'
        m2m_table_name = db.shorten_name(u'gallery_image_gallery')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('image', models.ForeignKey(orm[u'gallery.image'], null=False)),
            ('gallery', models.ForeignKey(orm[u'gallery.gallery'], null=False))
        ))
        db.create_unique(m2m_table_name, ['image_id', 'gallery_id'])


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
            'gallery': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['gallery.Gallery']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['gallery']