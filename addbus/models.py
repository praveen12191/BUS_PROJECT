from django.db import models

class addBus(models.Model):
    driverName = models.CharField(max_length=30)
    ApiKey = models.TextField()
    busNumber = models.IntegerField()
    deviceId = models.IntegerField()
    url = models.TextField()
    