# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Renaming column for 'Post.pub_place' to match new field type.
        db.rename_column(u'posts_post', 'pub_place', 'pub_place_id')
        # Changing field 'Post.pub_place'
        db.alter_column(u'posts_post', 'pub_place_id', self.gf('django.db.models.fields.related.ForeignKey')(max_length=140, to=orm['posts.PostPlace'], null=True))
        # Adding index on 'Post', fields ['pub_place']
        db.create_index(u'posts_post', ['pub_place_id'])


        # Renaming column for 'Post.post_type' to match new field type.
        db.rename_column(u'posts_post', 'post_type', 'post_type_id')
        # Changing field 'Post.post_type'
        db.alter_column(u'posts_post', 'post_type_id', self.gf('django.db.models.fields.related.ForeignKey')(max_length=140, to=orm['posts.PostType'], null=True))
        # Adding index on 'Post', fields ['post_type']
        db.create_index(u'posts_post', ['post_type_id'])


    def backwards(self, orm):
        # Removing index on 'Post', fields ['post_type']
        db.delete_index(u'posts_post', ['post_type_id'])

        # Removing index on 'Post', fields ['pub_place']
        db.delete_index(u'posts_post', ['pub_place_id'])


        # Renaming column for 'Post.pub_place' to match new field type.
        db.rename_column(u'posts_post', 'pub_place_id', 'pub_place')
        # Changing field 'Post.pub_place'
        db.alter_column(u'posts_post', 'pub_place', self.gf('django.db.models.fields.CharField')(default='', max_length=140))

        # Renaming column for 'Post.post_type' to match new field type.
        db.rename_column(u'posts_post', 'post_type_id', 'post_type')
        # Changing field 'Post.post_type'
        db.alter_column(u'posts_post', 'post_type', self.gf('django.db.models.fields.CharField')(default='', max_length=140))

    models = {
        u'posts.post': {
            'Meta': {'object_name': 'Post'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'post_type': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '140', 'to': u"orm['posts.PostType']", 'null': 'True', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 8, 29, 0, 0)'}),
            'pub_place': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '140', 'to': u"orm['posts.PostPlace']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'posts.postplace': {
            'Meta': {'object_name': 'PostPlace'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        },
        u'posts.posttype': {
            'Meta': {'object_name': 'PostType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '140'})
        }
    }

    complete_apps = ['posts']