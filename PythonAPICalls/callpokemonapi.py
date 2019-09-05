import requests
import json

r = requests.get('https://pokeapi.co/api/v2/ability/4/').json()


#print(r['pokemon'][0]['pokemon']['name'])
print(r['pokemon'])

for item in r['pokemon']:
    print(item['pokemon']['name'])
