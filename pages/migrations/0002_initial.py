# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table(u'pages_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('thumb', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('ckeditor.fields.RichTextField')(blank=True)),
            ('type', self.gf('django.db.models.fields.CharField')(default='home', max_length=16)),
            ('oreder_number', self.gf('django.db.models.fields.IntegerField')(default=0, max_length=2)),
        ))
        db.send_create_signal(u'pages', ['Page'])


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table(u'pages_page')


    models = {
        u'pages.page': {
            'Meta': {'object_name': 'Page'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'oreder_number': ('django.db.models.fields.IntegerField', [], {'default': '0', 'max_length': '2'}),
            'thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'home'", 'max_length': '16'})
        }
    }

    complete_apps = ['pages']