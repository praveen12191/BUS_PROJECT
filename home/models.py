from django.db import models

# Create your models here.

class Location(models.Model):
    bus_number = models.IntegerField()
    device_id = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()