# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'DataSet.frequency'
        db.add_column('dhis_data_set', 'frequency', self.gf('django.db.models.fields.PositiveIntegerField')(default=12), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'DataSet.frequency'
        db.delete_column('dhis_data_set', 'frequency')


    models = {
        'main.dataelement': {
            'Meta': {'object_name': 'DataElement', 'db_table': "'dhis_data_element'"},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_element_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'data_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.DataSet']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'main.dataset': {
            'Meta': {'object_name': 'DataSet', 'db_table': "'dhis_data_set'"},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_set_id': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '32'}),
            'frequency': ('django.db.models.fields.PositiveIntegerField', [], {'default': '12'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'})
        },
        'main.datavalueset': {
            'Meta': {'object_name': 'DataValueSet', 'db_table': "'dhis_data_value_set'"},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.DataSet']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'org_unit': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.FormhubService']"})
        },
        'main.formdataelement': {
            'Meta': {'unique_together': "(('data_value_set', 'data_element'),)", 'object_name': 'FormDataElement', 'db_table': "'dhis_form_data_element'"},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'data_element': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.DataElement']"}),
            'data_value_set': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.DataValueSet']"}),
            'form_field': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'main.formhubservice': {
            'Meta': {'object_name': 'FormhubService', 'db_table': "'dhis_formhub_servicet'"},
            'created_on': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_string': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'json': ('django.db.models.fields.TextField', [], {}),
            'modified_on': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '32'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['main']
