import phonenumbers
import opencage
import folium
import json,os
from django.http import HttpResponse
from django.template import loader
from opencage.geocoder import OpenCageGeocode
from django.shortcuts import render
from geopy import Nominatim
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
import requests
from home.models import Location
import script
# api_key = '507a9a77c149643e1c486eba001f979b'
# device_id = '12684904'

# url =  	'https://www.followmee.com/api/tracks.aspx?key=5a1456603bc811e83ed20425cf67aafc&username=hariravi&output=json&function=currentfordevice&deviceid=12684978'
# response = requests.get(url, params={'ak': api_key})
# if response.status_code == 200:
#     data = response.json()
#     print(data)
#     k = data['Data']
#     lat = k[0]['Latitude']
#     long = k[0]['Longitude']
#     map = folium.Map(location=[lat, long], zoom_start=13)
#     marker = folium.Marker(location=[lat, long], popup="Device Location")
#     marker.add_to(map)
#     map.save("map.html")
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

def home(request):
    return render(request,"index.html")
def get_loc(request):
    api_key = '507a9a77c149643e1c486eba001f979b'
    device_id = '12684978'
    #url = 'https://www.followmee.com/api/tracks.aspx?key=5a1456603bc811e83ed20425cf67aafc&username=hariravi&output=json&function=currentfordevice&deviceid=12684978'
    url =  	'https://www.followmee.com/api/tracks.aspx?key=d76937ef4c298e0cac21b72f519a9547&username=praveen816&output=json&function=currentfordevice&deviceid=123456'
    bus_number = int(request.POST["num"])
    print(url)
    if(bus_number==1):
        script.update(api_key,device_id,url,bus_number)
        data = Location.objects.all().values()
        for i in data:
            if(i['device_id']==device_id):
                file_path = os.path.join(BASE_DIR, 'map.html')
                return render(request,'map.html') 
def not_exit(request):
    not_present = request.POST["not_present"]
    return render(request,"loc.html",{"bus":"not_present"})

