# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'PageType'
        db.create_table(u'pages_pagetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140)),
            ('url', self.gf('django.db.models.fields.CharField')(default='/', max_length=50, db_index=True)),
        ))
        db.send_create_signal(u'pages', ['PageType'])

        # Adding model 'Page'
        db.create_table(u'pages_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=140, null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.PageType'])),
            ('content', self.gf('ckeditor.fields.RichTextField')(blank=True)),
        ))
        db.send_create_signal(u'pages', ['Page'])


    def backwards(self, orm):
        # Deleting model 'PageType'
        db.delete_table(u'pages_pagetype')

        # Deleting model 'Page'
        db.delete_table(u'pages_page')


    models = {
        u'pages.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.PageType']"})
        },
        u'pages.pagetype': {
            'Meta': {'object_name': 'PageType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'url': ('django.db.models.fields.CharField', [], {'default': "'/'", 'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['pages']