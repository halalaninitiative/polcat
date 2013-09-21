# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Saln'
        db.create_table(u'salns_saln', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('profile', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.Profile'])),
            ('net_worth', self.gf('django.db.models.fields.DecimalField')(max_digits=15, decimal_places=3)),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'salns', ['Saln'])


    def backwards(self, orm):
        # Deleting model 'Saln'
        db.delete_table(u'salns_saln')


    models = {
        u'profiles.profile': {
            'Meta': {'object_name': 'Profile'},
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'birthplace': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'education': ('django.db.models.fields.TextField', [], {}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'middle_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sex': ('django.db.models.fields.CharField', [], {'max_length': '7'}),
            'suffix': ('django.db.models.fields.CharField', [], {'max_length': '7'})
        },
        u'salns.saln': {
            'Meta': {'object_name': 'Saln'},
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'net_worth': ('django.db.models.fields.DecimalField', [], {'max_digits': '15', 'decimal_places': '3'}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.Profile']"})
        }
    }

    complete_apps = ['salns']