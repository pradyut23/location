import urllib.request, urllib.parse, urllib.error
import json
import ssl

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

parms = dict()
parms['address'] = address
parms['key'] = 42
url = serviceurl + urllib.parse.urlencode(parms)

print('Retrieving', url)
uh = urllib.request.urlopen(url,context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('Failure To Retrieve')
    print(data)

#print(json.dumps(js, indent=2))

location = id = js["results"][0]["formatted_address"]
lat = id = js["results"][0]["geometry"]["location"]["lat"]
lng = id = js["results"][0]["geometry"]["location"]["lng"]
print("")
print("Full Address with Latitude and Longitude:-")
print(location)
print("Latitude:",lat)
print("Longitude:",lng)
