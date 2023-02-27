import requests
import django,os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bus_project.settings')
django.setup()
from home.models import Location
def update(api_key,device_id,url,bus_number):
    # api_key = '507a9a77c149643e1c486eba001f979b'
    # device_id = '12684903'
    print("hello")
    #url =  	'https://www.followmee.com/api/tracks.aspx?key=5a1456603bc811e83ed20425cf67aafc&username=hariravi&output=json&function=currentfordevice&deviceid=12684978'
    response = requests.get(url, params={'ak': api_key})
    if response.status_code == 200:
        data = response.json()
        print(data)
        k = data['Data']
        lat = k[0]['Latitude']
        long = k[0]['Longitude']
        location = Location(bus_number=bus_number,device_id=device_id,latitude=lat, longitude=long)
        location.save()
    else:
        print("Error: {} status code.".format(response.status_code))
