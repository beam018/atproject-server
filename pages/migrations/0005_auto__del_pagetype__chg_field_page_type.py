# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PageType'
#        db.delete_table(u'pages_pagetype')


        # Renaming column for 'Page.type' to match new field type.
#        db.rename_column(u'pages_page', 'type_id', 'type')
        # Changing field 'Page.type'
        db.alter_column(u'pages_page', 'type', self.gf('django.db.models.fields.CharField')(max_length=16))
        # Removing index on 'Page', fields ['type']
#        db.delete_index(u'pages_page', ['type_id'])


    def backwards(self, orm):
        # Adding index on 'Page', fields ['type']
        db.create_index(u'pages_page', ['type_id'])

        # Adding model 'PageType'
        db.create_table(u'pages_pagetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=140, unique=True)),
        ))
        db.send_create_signal(u'pages', ['PageType'])


        # Renaming column for 'Page.type' to match new field type.
        db.rename_column(u'pages_page', 'type', 'type_id')
        # Changing field 'Page.type'
        db.alter_column(u'pages_page', 'type_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['pages.PageType'], to_field='name'))

    models = {
        u'pages.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140', 'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '16'})
        }
    }

    complete_apps = ['pages']