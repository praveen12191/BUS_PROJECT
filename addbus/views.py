from django.shortcuts import render
from .models import addBus

def addbus(request):
    all = addBus.objects.all()
    for i in all:
        print(i.driverName)
    return render(request,'addbus.html')