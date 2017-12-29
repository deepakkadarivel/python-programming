import urllib.request, urllib.parse
import json

# url = 'http://maps.googleapis.com/maps/api/geocode/json?'
url = 'http://py4e-data.dr-chuck.net/geojson?'

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    url = url + urllib.parse.urlencode({'address': address})

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)
    data = uh.read().decode()

    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except ValueError:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('========== Failure to retrieve =============')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    place_id = js['results'][0]['place_id']
    print(place_id)
    try:
        country_code = js['results'][0]['address_components'][2]['short_name']
        print(country_code)
    except IndexError:
        continue
