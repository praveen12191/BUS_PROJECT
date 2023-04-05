from django.db import models

class driver(models.Model):
    drivername = models.CharField(max_length=30)
    busnumber = models.IntegerField()
    ApiKey = models.TextField()
    deviceId = models.IntegerField()
    url = models.TextField()
class student(models.Model):
    rno = models.CharField(max_length=40);
    email = models.CharField(max_length=30)
    busnumber = models.IntegerField()
    stopname = models.TextField()
    attendence = models.BooleanField(default=1)
    password = models.CharField(max_length=30)
    password = models.CharField(max_length=30)