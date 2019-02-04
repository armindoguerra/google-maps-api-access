import json
import requests

key='<...>'

url ='https://maps.googleapis.com/maps/api/geocode/json'
address = 'Rodovia Amaro Antonio Vieira, 2797'

param = {
    'address': address, 
    'key': key}

response = requests.get(url, params=param)
json_dict = response.json()

with open('data.json', 'w') as outfile:
    json.dump(json_dict, outfile)