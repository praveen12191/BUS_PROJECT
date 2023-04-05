from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .import views
from accounts.models import driver
from accounts.models import student
from collections import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from my_jwt import generate_token
from django.db.models import Count
import json

import demo
import requests



def register(request):
    if(request.method=='POST'): #after data added in the form 
        rno = request.POST['rno']
        email = request.POST['email']
        busnumber = request.POST['busnumber']
        stopname = request.POST['stopname']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if(pass1==pass2):
            if(student.objects.filter(rno=rno).exists()):
                messages.info(request,'user name exists')
                return redirect('register')
            else:
                user = student(rno=rno,email=email,busnumber=int(busnumber),stopname=stopname,password=pass1)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'password miss match')
            return redirect('register')
            
    return render(request,"register.html") #in nav bar just call the register.html which is GET



def login(request):
    if(request.method=='POST'):
        rno = request.POST['rno']
        busnumber = request.POST['busnumber']
        pass1 = request.POST['password1']
        try:
            obj = student.objects.get(rno=rno)
            if(obj.password!=pass1):
                messages.info(request,"wrong password")
                return redirect('login')
            if(obj.busnumber==int(busnumber)):
                obj.attendence = 1
                obj.save()
                demo.busnumber = busnumber
                token = generate_token(rno)
                demo.rno = rno
                return redirect('studentview')
        except:
            messages.info(request,"User not exist")
            return render(request,"login.html") 
    else:
        return render(request,"login.html") 
    
    
    
def logout(request):
    auth.logout(request)
    return redirect("/")


def driverRegister(request):
    if(request.method=='POST'): #after data added in the form 
        name = request.POST['name']
        busnumber = request.POST['busnumber']
        api = request.POST['apikey']
        deviceid = request.POST['deviceid']
        url = request.POST['url']
        user = driver(drivername=name,busnumber=int(busnumber),ApiKey=api,deviceId=deviceid,url=url)
        user.save()
        return redirect('driverLogin')
    return render(request,"driverRegister.html") #in nav bar just call the register.html which is GET


def driverLogin(request):
    if(request.method=='POST'):
        name = request.POST['name']
        busnumber = request.POST['busnumber']
        try:
            obj = driver.objects.get(busnumber=int(busnumber),drivername=name)
            stopname = student.objects.filter(busnumber=busnumber,attendence=1).values('stopname')
            stop = {}
            for x in stopname:
                for y in x:
                    if(x[y] not in stop):
                        stop[x[y]] = 1
                    else:
                        stop[x[y]]+=1
            return render(request,"driverview.html",{'ext':stop})
        except:
            messages.info(request,"invalid username")
            return redirect('driverLogin')
    return render(request,"driverLogin.html")
       

def driverview(request):
    return render(request,"driverview.html")

def studentview(request):
    if(request.method=="POST"):
        return render(request,"studentview.html") 
    return render(request,"studentview.html") 



def notpresent(request):
    rno = demo.rno
    busnumber = demo.busnumber
    obj = student.objects.get(rno=rno)
    obj.attendence = 0
    obj.save()
    return redirect('/')