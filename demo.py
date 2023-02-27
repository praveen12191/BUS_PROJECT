import requests
api_key = '49a85f49f6dbbc24dcc9f7aa9c4116df'
device_id = '12684904'
response = requests.get('https://www.followmee.com/api/location/12684904', params={'ak': api_key})
print(response.text)
print(123)