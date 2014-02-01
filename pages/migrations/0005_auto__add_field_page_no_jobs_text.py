# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Page.no_jobs_text'
        db.add_column(u'pages_page', 'no_jobs_text',
                      self.gf('ckeditor.fields.RichTextField')(default='', blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Page.no_jobs_text'
        db.delete_column(u'pages_page', 'no_jobs_text')


    models = {
        u'pages.page': {
            'Meta': {'object_name': 'Page'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255'}),
            'no_jobs_text': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'order_number': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'thumb': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'home'", 'max_length': '16'})
        }
    }

    complete_apps = ['pages']