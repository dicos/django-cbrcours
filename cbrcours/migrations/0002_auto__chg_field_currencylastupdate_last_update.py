# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'CurrencyLastUpdate.last_update'
        db.alter_column(u'cbrcource_currencylastupdate', 'last_update', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True))

    def backwards(self, orm):

        # Changing field 'CurrencyLastUpdate.last_update'
        db.alter_column(u'cbrcource_currencylastupdate', 'last_update', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

    models = {
        u'cbrcource.currency': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '35'}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '30', 'decimal_places': '10'})
        },
        u'cbrcource.currencylastupdate': {
            'Meta': {'object_name': 'CurrencyLastUpdate'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_update': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cbrcource']
