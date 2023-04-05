import requests
import requests
import django,os 
from django.shortcuts import render
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bus_project.settings')
django.setup()
from home.models import Location
val = {}
def update(api_key,device_id,url,bus_number):
    # api_key = 'da3c06989059ed209dc4189e30a088c2'
    # device_id = '12704754'
    # url = 'https://www.followmee.com/api/tracks.aspx?key=da3c06989059ed209dc4189e30a088c2&username=kavitha&output=json&function=currentfordevice&deviceid=12704754'
    response = requests.get(url, params={'ak': api_key})
    print(response)
    if response.status_code == 200:
        data = response.json()
        for i in data:
            print(i)
        k = data['Data']
        lat = k[0]['Latitude']
        long = k[0]['Longitude']
        print(lat,long)
        val["lat"] = lat
        val["long"] = long
        location = Location(bus_number=bus_number,device_id=device_id,latitude=lat, longitude=long)
        location.save()
        
    else:
        print("Error: {} status code.".format(response.status_code))
