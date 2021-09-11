'''
Practicing using APIs in Python - Dataquest.io blog tutorial https://www.dataquest.io/blog/python-api-tutorial
Using the Open Notify API for the International Space Stations (ISS)
'''

import requests, json

## Part 1 - The first endpoint example: Using the API to see how many astronauts are currently in space (not that it takes no input)
# The tutorials uses 'https', but this causes an error...
response = requests.get("http://api.open-notify.org/astros.json")
# print(response.status_code)

# print(response.json())

'''
The json package is part of the standard Python library. It has two main functions:
    1. json.dumps() - takes in a Pytho object, and converts('dumps') it to a string
    2. json.loads() - takes a JSON string, and converts('loads') it to a Python object

dumps() is useful when you want to print a formatted string, which makes the JSON output easier to understand, see example below
'''

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys = True, indent = 4)
    print(text)

# jprint(response.json())



'''
Part 2 - Using Parameters, with the endpoint ISS-Pass, which tells out when ISS will pass over a given location next. Need specify the lat and lon.
We can pass the arguments individually with requests., or store them in a dict and then pass the dict in, OR you can also pass them directly into the URL.
But, it is almost always preferable to pass the parameters in a dict, because requests properly format the parameters automatically
'''

# First, set up the parameters by storing them into a dict. (These are the coordinates for NYC))
parameters = {
    "lat": 40.71,
    "lon": -74
}

response = requests.get("http://api.open-notify.org/iss-pass.json", params = parameters)

#jprint(response.json())

## Extract the pass times
pass_times = response.json()['response']
#jprint(pass_times)

## Not use a fore loop to extract just the 5 risetime values
risetimes = []
for d in pass_times:
    time = d['risetime']
    risetimes.append(time)
#print(risetimes) # These are in epoch time stamp. Convert them to something more readble

from datetime import datetime
times = []
for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)


# Here's a list of free public APIs https://github.com/public-apis/public-apis
