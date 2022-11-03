import requests
import json

response = requests.get('http://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')

# print(response.json()) # this will list out everything that the api holds.

# print(response.json()['items']) # this will return the value affiliated with this key 'items'

for data in response.json()['items']:
    if data['answer_count'] == 0:
        print(data['title'])
        print(data['link'])
    else:
        print('skipped')
    print()
