'''
Practicing using APIs in Python - Dataquest.io blog tutorial https://www.dataquest.io/blog/python-api-tutorial
Using the Open Notify API for the International Space Stations (ISS)
'''

import requests, json

## The first endpoint example: Using the API to see how many astronauts are currently in space (not that it takes no input)
# The tutorials uses 'https', but this causes an error...
response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)
