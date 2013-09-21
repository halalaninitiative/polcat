# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Term.party'
        db.add_column(u'terms_term', 'party',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['parties.Party']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Term.party'
        db.delete_column(u'terms_term', 'party_id')


    models = {
        u'parties.party': {
            'Meta': {'object_name': 'Party'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'positions.position': {
            'Meta': {'object_name': 'Position'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
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
        u'terms.term': {
            'Meta': {'object_name': 'Term'},
            'end': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'party': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['parties.Party']"}),
            'position': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['positions.Position']"}),
            'profile': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['profiles.Profile']"}),
            'start': ('django.db.models.fields.DateField', [], {})
        }
    }

    complete_apps = ['terms']