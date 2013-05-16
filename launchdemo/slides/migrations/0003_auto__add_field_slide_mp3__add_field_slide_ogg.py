# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Slide.mp3'
        db.add_column('slides_slide', 'mp3',
                      self.gf('django.db.models.fields.files.FileField')(default='noaudio', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'Slide.ogg'
        db.add_column('slides_slide', 'ogg',
                      self.gf('django.db.models.fields.files.FileField')(default='noaudio', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Slide.mp3'
        db.delete_column('slides_slide', 'mp3')

        # Deleting field 'Slide.ogg'
        db.delete_column('slides_slide', 'ogg')


    models = {
        'slides.slide': {
            'Meta': {'object_name': 'Slide'},
            'graph_snippet': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mp3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'ogg': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'point': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['slides']