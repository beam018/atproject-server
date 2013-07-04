# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PageType.url'
        db.delete_column(u'pages_pagetype', 'url')


    def backwards(self, orm):
        # Adding field 'PageType.url'
        db.add_column(u'pages_pagetype', 'url',
                      self.gf('django.db.models.fields.CharField')(default='/', max_length=50, db_index=True),
                      keep_default=False)


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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['pages']