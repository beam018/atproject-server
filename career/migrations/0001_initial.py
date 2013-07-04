# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Tab'
        db.create_table('career_tab', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('content', self.gf('ckeditor.fields.RichTextField')()),
        ))
        db.send_create_signal('career', ['Tab'])

        # Adding model 'City'
        db.create_table('career_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('city_name', self.gf('django.db.models.fields.CharField')(max_length=140)),
        ))
        db.send_create_signal('career', ['City'])

        # Adding model 'JobCategory'
        db.create_table('career_jobcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('thumb', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('background', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('content', self.gf('ckeditor.fields.RichTextField')(blank=True)),
        ))
        db.send_create_signal('career', ['JobCategory'])

        # Adding model 'Job'
        db.create_table('career_job', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['career.City'], null=True, blank=True)),
            ('employer', self.gf('django.db.models.fields.CharField')(max_length=140, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default='p', max_length=2)),
            ('top_content', self.gf('ckeditor.fields.RichTextField')(blank=True)),
            ('skills', self.gf('ckeditor.fields.RichTextField')(blank=True)),
            ('desired_skills', self.gf('ckeditor.fields.RichTextField')(blank=True)),
            ('bottom_content', self.gf('ckeditor.fields.RichTextField')(blank=True)),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 1, 22, 0, 0))),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['career.JobCategory'], null=True)),
        ))
        db.send_create_signal('career', ['Job'])


    def backwards(self, orm):
        # Deleting model 'Tab'
        db.delete_table('career_tab')

        # Deleting model 'City'
        db.delete_table('career_city')

        # Deleting model 'JobCategory'
        db.delete_table('career_jobcategory')

        # Deleting model 'Job'
        db.delete_table('career_job')


    models = {
        'career.city': {
            'Meta': {'object_name': 'City'},
            'city_name': ('django.db.models.fields.CharField', [], {'max_length': '140'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'career.job': {
            'Meta': {'object_name': 'Job'},
            'bottom_content': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['career.JobCategory']", 'null': 'True'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['career.City']", 'null': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 1, 22, 0, 0)'}),
            'desired_skills': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'employer': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'skills': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'p'", 'max_length': '2'}),
            'top_content': ('ckeditor.fields.RichTextField', [], {'blank': 'True'})
        },
        'career.jobcategory': {
            'Meta': {'object_name': 'JobCategory'},
            'background': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'content': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'career.tab': {
            'Meta': {'object_name': 'Tab'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'content': ('ckeditor.fields.RichTextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['career']