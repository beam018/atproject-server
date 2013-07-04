# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Page.type'
        db.alter_column(u'pages_page', 'type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.PageType'], to_field='name'))
        # Adding unique constraint on 'PageType', fields ['name']
        db.create_unique(u'pages_pagetype', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'PageType', fields ['name']
        db.delete_unique(u'pages_pagetype', ['name'])


        # Changing field 'Page.type'
        db.alter_column(u'pages_page', 'type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.PageType']))

    models = {
        u'pages.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['pages.PageType']", 'to_field': "'name'"})
        },
        u'pages.pagetype': {
            'Meta': {'object_name': 'PageType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '140'})
        }
    }

    complete_apps = ['pages']