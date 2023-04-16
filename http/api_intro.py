import requests

url = 'https://earthquake.usgs.gov/fdsnws/event/1/query?'
response = requests.get(url, headers={'Accept': 'application/json'}, params={
    'format': 'geojson',
    'starttime': '2019-01-01',
    'endtime': '2019-05-01',
    'latitude': '51.51',
    'longitude': '-0.12',
    'maxradiuskm': '2000'

})

# print(response.json())

data = response.json()
print(data['features'][1]['properties']['place'])
