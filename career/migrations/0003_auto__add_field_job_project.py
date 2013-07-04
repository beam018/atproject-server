# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Job.project'
        db.add_column('career_job', 'project',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Job.project'
        db.delete_column('career_job', 'project')


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
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 23, 0, 0)'}),
            'desired_skills': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
            'employer': ('django.db.models.fields.CharField', [], {'max_length': '140', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'project': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '255'}),
            'requirements': ('ckeditor.fields.RichTextField', [], {'blank': 'True'}),
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