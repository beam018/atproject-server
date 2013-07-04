# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mail'
        db.create_table('mailer_mail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True)),
            ('template', self.gf('django.db.models.fields.TextField')()),
            ('type', self.gf('django.db.models.fields.CharField')(default='s', max_length=1)),
        ))
        db.send_create_signal('mailer', ['Mail'])


    def backwards(self, orm):
        # Deleting model 'Mail'
        db.delete_table('mailer_mail')


    models = {
        'mailer.mail': {
            'Meta': {'object_name': 'Mail'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'template': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True'}),
            'type': ('django.db.models.fields.CharField', [], {'default': "'s'", 'max_length': '1'})
        }
    }

    complete_apps = ['mailer']