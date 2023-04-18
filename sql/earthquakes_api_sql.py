import requests
import sqlite3


def save_earthquakes(place_magnitude_list):
    conn = sqlite3.connect('earthquakes_api_db.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE earthquakes (place TEXT, magnitude REAL)")
    cursor.executemany("INSERT INTO earthquakes VALUES (?, ?)", place_magnitude_list)
    conn.commit()
    conn.close()


def select_all_earthquakes():
    conn = sqlite3.connect('earthquakes_api_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM earthquakes")
    data = cursor.fetchall()
    [print(row) for row in data]
    conn.commit()
    conn.close()


url = 'http://earthquake.usgs.gov/fdsnws/event/1/query?'

# start_time = input('Enter the start time')
# end_time = input('Enter the end time')
# latitude = input('Enter the latitude')
# longitude = input('Enter the longitude')
# max_radius_km = input('Enter the max radius in km')
# min_magnitude = input('Enter the min magnitude')

response = requests.get(url, headers={'Accept': 'application/json'}, params={
    'format': 'geojson',
    'starttime': '2019-01-01',
    'endtime': '2019-05-01',
    'latitude': '51.51',
    'longitude': '-0.12',
    'maxradiuskm': '2000',
    'minmagnitude': '3'

})

data = response.json()

earthquake_list = data['features']
place_magnitude_list = []
count = 0
for earthquake in earthquake_list:
    count += 1
    place_magnitude_list.append((earthquake['properties']['place'], earthquake['properties']['mag']))


# save_earthquakes(place_magnitude_list)
select_all_earthquakes()