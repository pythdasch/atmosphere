# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Image.caption'
        db.delete_column(u'gallery_image', 'caption')

        # Deleting field 'Image.width'
        db.delete_column(u'gallery_image', 'width')

        # Deleting field 'Image.display_caption'
        db.delete_column(u'gallery_image', 'display_caption')

        # Deleting field 'Image.height'
        db.delete_column(u'gallery_image', 'height')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Image.caption'
        raise RuntimeError("Cannot reverse this migration. 'Image.caption' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Image.width'
        raise RuntimeError("Cannot reverse this migration. 'Image.width' and its values cannot be restored.")
        # Adding field 'Image.display_caption'
        db.add_column(u'gallery_image', 'display_caption',
                      self.gf('django.db.models.fields.BooleanField')(default=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Image.height'
        raise RuntimeError("Cannot reverse this migration. 'Image.height' and its values cannot be restored.")

    models = {
        u'gallery.image': {
            'Meta': {'object_name': 'Image'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['gallery']