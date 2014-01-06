# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Page.thumb'
        db.alter_column(u'pages_page', 'thumb', self.gf('filebrowser.fields.FileBrowseField')(max_length=255))

        # Changing field 'Page.image'
        db.alter_column(u'pages_page', 'image', self.gf('filebrowser.fields.FileBrowseField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'Page.thumb'
        db.alter_column(u'pages_page', 'thumb', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

        # Changing field 'Page.image'
        db.alter_column(u'pages_page', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100))

    models = {
        u'pages.page': {
            'Meta': {'object_name': 'Page'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255'}),
            'order_number': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'thumb': ('filebrowser.fields.FileBrowseField', [], {'max_length': '255'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'home'", 'max_length': '16'})
        }
    }

    complete_apps = ['pages']