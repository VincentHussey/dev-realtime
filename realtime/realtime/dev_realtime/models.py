#from django.db import models
# settings for django.contrib.gis
from django.contrib.gis.db import models

# settings for south
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^django\.contrib\.gis"])

# Create your models here.

# Region - set of gauges managed by a single technician
class Region(models.Model):
   name = models.CharField(max_length=30)
   short = models.CharField(max_length=10)
   technician = models.CharField(max_length=30,blank=True)
   # GIS data - this can be created using convex hull
   geometry = models.PolygonField(srid=2157,blank=True)
   objects = models.GeoManager()
   class Meta:
      ordering = ['name']


   def __unicode__(self):
      return u'%s' % (self.short)

# RDB - River basin District as defined under Water Framework Directive
# In the north west, some hydrometric areas are split between RBDs
class RiverBasinDistrict(models.Model):
   name = models.CharField(max_length=30)
   short = models.CharField(max_length=10)
   class Meta:
      ordering = ['name']
   def __unicode__(self):
      return u'%s' % (self.name)

# Waterbody - as defined in EPA Register of Hydrometric Stations in Ireland
class Waterbody(models.Model):
   name = models.CharField(max_length=50)
   rbd = models.ForeignKey(RiverBasinDistrict)
   type = models.CharField(max_length=10)
   class Meta:
      ordering = ['name']
   def __unicode__(self):
      return u'%s' % (self.name)

# Sensor parameter - measured parameter
class SensorParameter(models.Model):
   name = models.CharField(max_length=30)
   description = models.CharField(max_length=100)
   export_name = models.CharField(max_length=20)
   class Meta:
      ordering = ['name']
   def __unicode__(self):
      return u'%s' % (self.name)

# Station - station where measurements are made
class Station(models.Model):
   name = models.CharField(max_length=100)
   waterbody = models.ForeignKey(Waterbody)
   ref = models.CharField(max_length=12)
   latitude = models.DecimalField(max_digits=10, decimal_places=6)
   longitude = models.DecimalField(max_digits=10, decimal_places=6)
   publish = models.BooleanField()
   rbd = models.ForeignKey(RiverBasinDistrict,blank=True)
   region = models.ForeignKey(Region,blank=True)
   county = models.CharField(max_length=20)
   alt_ref = models.CharField(max_length=12,blank=True)
   # GIS data
   geometry = models.PointField(blank=True)
   objects = models.GeoManager()

   class Meta:
      ordering = ['ref']

   def __unicode__(self):
      return u'%s' % (self.ref)

   def hydrometric_area(self):
      return u'%s' % (self.ref[5:7])

# Station OD levels
class OrdnanceDatumLevels(models.Model):
   DATUM = (
      (u'ODM', u'Malin Head'),
      (u'ODP', u'Poolbeg'),
      (u'NNN', u'Unknown'),
   )
   station = models.ForeignKey(Station)
   datetime = models.DateTimeField()
   value = models.DecimalField(max_digits=10, decimal_places=3)
   datum = models.CharField(max_length=3, choices=DATUM)
   class Meta:
      ordering = ['datum','station']
      verbose_name_plural = 'ordnance datum levels'
   def __unicode__(self):
      return u'%s %s' % (self.station, self.value)

# Station thresholds
class Threshold(models.Model):
   THRESHOLD_TYPE = (
      (u'Amax', u'Highest Annual Max on record'),
      (u'Amed', u'Median Annual Max'),
      (u'Amin', u'Minimum Annual Max on record'),
      (u'Mean', u'Mean Annual'),
      (u'Qbar', u'Mean Flood'),
   )
   station = models.ForeignKey(Station)
   threshold_type = models.CharField(max_length=4, choices=THRESHOLD_TYPE)
   level = models.FloatField(null=True,blank=True)
   flow = models.FloatField(null=True,blank=True)
   period = models.CharField(max_length=40)
   def __unicode__(self):
      return u'%s %s' % (self.station, self.threshold_type)
      
 
# Sensor - sensor numbers returned by gauges
# the same number might have a different meaning for different sites
# the default_parameter is the current convention for that sensor type
class Sensor(models.Model):
   ref = models.CharField(max_length=4)
   default_parameter = models.IntegerField() 

   #ForeignKey(SensorParameter)
   # station = models.ForeignKey(Station)
   # parameter = models.ForeignKey(SensorParameter)

   class Meta:
      ordering = ['ref']

   def __unicode__(self):
      return u'%s' % (self.ref)

# Station - Sensor
class StationSensor(models.Model):
   station = models.ForeignKey(Station)
   sensor = models.ForeignKey(Sensor)
   sensor_parameter = models.ForeignKey(SensorParameter) 
   class Meta:
      ordering = ['station','sensor','sensor_parameter']

   def __unicode__(self):
      return u'%s %s %s' % (self.station, self.sensor, self.sensor_parameter)

# Group - to show several stations together
class Group(models.Model):
   name = models.CharField(max_length=100)
   description = models.CharField(max_length=200)
   sensor = models.ForeignKey(Sensor)
   station = models.ManyToManyField(Station)

   def __unicode__(self):
      return u'%s' % (self.name)   

# Reading
class Reading(models.Model):
   station = models.ForeignKey(Station)
   sensor = models.ForeignKey(Sensor)
   datetime = models.DateTimeField()
   value = models.FloatField(null=True,blank=True)
   err_code = models.IntegerField(blank=True)
   late = models.BooleanField()
   def __unicode__(self):
      if (self.value):
          return u'%f' % (self.value)
      else:
          return None

# summary readings - daily
class ReadingSummary(models.Model):
   day = models.DateTimeField()
   station = models.ForeignKey(Station)
   sensor = models.ForeignKey(Sensor)
   min = models.FloatField(null=True,blank=True)
   average = models.FloatField(null=True,blank=True)
   max = models.FloatField(null=True,blank=True)

# current readings
class CurrentReading(models.Model):
   station = models.ForeignKey(Station)
   sensor = models.ForeignKey(Sensor)
   datetime = models.DateTimeField()
   value = models.FloatField(null=True,blank=True)
   err_code = models.IntegerField(blank=True)
   def __unicode__(self):
      return u'%f' % (self.value)

