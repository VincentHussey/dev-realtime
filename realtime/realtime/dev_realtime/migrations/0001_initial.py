# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Region'
        db.create_table('dev_realtime_region', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('short', self.gf('django.db.models.fields.CharField')(max_length=10)),
            ('technician', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PolygonField')(blank=True)),
        ))
        db.send_create_signal('dev_realtime', ['Region'])

        # Adding model 'RiverBasinDistrict'
        db.create_table('dev_realtime_riverbasindistrict', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('short', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('dev_realtime', ['RiverBasinDistrict'])

        # Adding model 'Waterbody'
        db.create_table('dev_realtime_waterbody', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('rbd', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dev_realtime.RiverBasinDistrict'])),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('dev_realtime', ['Waterbody'])

        # Adding model 'SensorParameter'
        db.create_table('dev_realtime_sensorparameter', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('export_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal('dev_realtime', ['SensorParameter'])

        # Adding model 'Station'
        db.create_table('dev_realtime_station', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('waterbody', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dev_realtime.Waterbody'])),
            ('ref', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=6)),
            ('publish', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('rbd', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dev_realtime.RiverBasinDistrict'], blank=True)),
            ('region', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dev_realtime.Region'], blank=True)),
            ('county', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('alt_ref', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('geometry', self.gf('django.contrib.gis.db.models.fields.PointField')(blank=True)),
        ))
        db.send_create_signal('dev_realtime', ['Station'])

        # Adding model 'OrdnanceDatumLevels'
        db.create_table('dev_realtime_ordnancedatumlevels', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dev_realtime.Station'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('value', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=3)),
            ('datum', self.gf('django.db.models.fields.CharField')(max_length=3)),
        ))
        db.send_create_signal('dev_realtime', ['OrdnanceDatumLevels'])

        # Adding model 'Threshold'
        db.create_table('dev_realtime_threshold', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dev_realtime.Station'])),
            ('threshold_type', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('level', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('flow', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('period', self.gf('django.db.models.fields.CharField')(max_length=40)),
        ))
        db.send_create_signal('dev_realtime', ['Threshold'])

        # Adding model 'Sensor'
        db.create_table('dev_realtime_sensor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ref', self.gf('django.db.models.fields.CharField')(max_length=4)),
            ('default_parameter', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('dev_realtime', ['Sensor'])

        # Adding model 'StationSensor'
        db.create_table('dev_realtime_stationsensor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dev_realtime.Station'])),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dev_realtime.Sensor'])),
            ('sensor_parameter', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dev_realtime.SensorParameter'])),
        ))
        db.send_create_signal('dev_realtime', ['StationSensor'])

        # Adding model 'Group'
        db.create_table('dev_realtime_group', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dev_realtime.Sensor'])),
        ))
        db.send_create_signal('dev_realtime', ['Group'])

        # Adding M2M table for field station on 'Group'
        db.create_table('dev_realtime_group_station', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('group', models.ForeignKey(orm['dev_realtime.group'], null=False)),
            ('station', models.ForeignKey(orm['dev_realtime.station'], null=False))
        ))
        db.create_unique('dev_realtime_group_station', ['group_id', 'station_id'])

        # Adding model 'Reading'
        db.create_table('dev_realtime_reading', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dev_realtime.Station'])),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dev_realtime.Sensor'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('err_code', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('late', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('dev_realtime', ['Reading'])

        # Adding model 'ReadingSummary'
        db.create_table('dev_realtime_readingsummary', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('day', self.gf('django.db.models.fields.DateTimeField')()),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dev_realtime.Station'])),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dev_realtime.Sensor'])),
            ('min', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('average', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('max', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
        ))
        db.send_create_signal('dev_realtime', ['ReadingSummary'])

        # Adding model 'CurrentReading'
        db.create_table('dev_realtime_currentreading', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('station', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dev_realtime.Station'])),
            ('sensor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['dev_realtime.Sensor'])),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')()),
            ('value', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('err_code', self.gf('django.db.models.fields.IntegerField')(blank=True)),
        ))
        db.send_create_signal('dev_realtime', ['CurrentReading'])


    def backwards(self, orm):
        # Deleting model 'Region'
        db.delete_table('dev_realtime_region')

        # Deleting model 'RiverBasinDistrict'
        db.delete_table('dev_realtime_riverbasindistrict')

        # Deleting model 'Waterbody'
        db.delete_table('dev_realtime_waterbody')

        # Deleting model 'SensorParameter'
        db.delete_table('dev_realtime_sensorparameter')

        # Deleting model 'Station'
        db.delete_table('dev_realtime_station')

        # Deleting model 'OrdnanceDatumLevels'
        db.delete_table('dev_realtime_ordnancedatumlevels')

        # Deleting model 'Threshold'
        db.delete_table('dev_realtime_threshold')

        # Deleting model 'Sensor'
        db.delete_table('dev_realtime_sensor')

        # Deleting model 'StationSensor'
        db.delete_table('dev_realtime_stationsensor')

        # Deleting model 'Group'
        db.delete_table('dev_realtime_group')

        # Removing M2M table for field station on 'Group'
        db.delete_table('dev_realtime_group_station')

        # Deleting model 'Reading'
        db.delete_table('dev_realtime_reading')

        # Deleting model 'ReadingSummary'
        db.delete_table('dev_realtime_readingsummary')

        # Deleting model 'CurrentReading'
        db.delete_table('dev_realtime_currentreading')


    models = {
        'dev_realtime.currentreading': {
            'Meta': {'object_name': 'CurrentReading'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'err_code': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dev_realtime.Sensor']"}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dev_realtime.Station']"}),
            'value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'dev_realtime.group': {
            'Meta': {'object_name': 'Group'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dev_realtime.Sensor']"}),
            'station': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['dev_realtime.Station']", 'symmetrical': 'False'})
        },
        'dev_realtime.ordnancedatumlevels': {
            'Meta': {'ordering': "['datum', 'station']", 'object_name': 'OrdnanceDatumLevels'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'datum': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dev_realtime.Station']"}),
            'value': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '3'})
        },
        'dev_realtime.reading': {
            'Meta': {'object_name': 'Reading'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            'err_code': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'late': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dev_realtime.Sensor']"}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dev_realtime.Station']"}),
            'value': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
        },
        'dev_realtime.readingsummary': {
            'Meta': {'object_name': 'ReadingSummary'},
            'average': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'day': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'max': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'min': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dev_realtime.Sensor']"}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dev_realtime.Station']"})
        },
        'dev_realtime.region': {
            'Meta': {'ordering': "['name']", 'object_name': 'Region'},
            'geometry': ('django.contrib.gis.db.models.fields.PolygonField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'technician': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        },
        'dev_realtime.riverbasindistrict': {
            'Meta': {'ordering': "['name']", 'object_name': 'RiverBasinDistrict'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'short': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        },
        'dev_realtime.sensor': {
            'Meta': {'ordering': "['ref']", 'object_name': 'Sensor'},
            'default_parameter': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'dev_realtime.sensorparameter': {
            'Meta': {'ordering': "['name']", 'object_name': 'SensorParameter'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'export_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        'dev_realtime.station': {
            'Meta': {'ordering': "['ref']", 'object_name': 'Station'},
            'alt_ref': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'county': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'geometry': ('django.contrib.gis.db.models.fields.PointField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '6'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'publish': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rbd': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dev_realtime.RiverBasinDistrict']", 'blank': 'True'}),
            'ref': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dev_realtime.Region']", 'blank': 'True'}),
            'waterbody': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dev_realtime.Waterbody']"})
        },
        'dev_realtime.stationsensor': {
            'Meta': {'ordering': "['station', 'sensor', 'sensor_parameter']", 'object_name': 'StationSensor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sensor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dev_realtime.Sensor']"}),
            'sensor_parameter': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dev_realtime.SensorParameter']"}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dev_realtime.Station']"})
        },
        'dev_realtime.threshold': {
            'Meta': {'object_name': 'Threshold'},
            'flow': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'period': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'station': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dev_realtime.Station']"}),
            'threshold_type': ('django.db.models.fields.CharField', [], {'max_length': '4'})
        },
        'dev_realtime.waterbody': {
            'Meta': {'ordering': "['name']", 'object_name': 'Waterbody'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'rbd': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['dev_realtime.RiverBasinDistrict']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '10'})
        }
    }

    complete_apps = ['dev_realtime']