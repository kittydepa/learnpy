'''
Practicing using APIs in Python - Dataquest.io blog tutorial https://www.dataquest.io/blog/python-api-tutorial
Using the Open Notify API for the International Space Stations (ISS)
'''

import requests

## The first endpoint example: Using the API to see how many astronauts are currently in space (not that it takes no input)
# The tutorials uses 'https', but this causes an error...
response = requests.get("http://api.open-notify.org/astros.json")
print(response.status_code)

print(response.json())

'''
The json package is part of the standard Python library. It has two main functions:
    1. json.dumps() - takes in a Pytho object, and converts('dumps') it to a string
    2. json.loads() - takes a JSON string, and converts('loads') it to a Python object
'''