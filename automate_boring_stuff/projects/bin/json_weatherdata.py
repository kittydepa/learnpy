''' 
Project @ end of Ch. 14 of Automate the Boring Stuff
Fetching the current weather data with weather API/ JSON data

This program will do the following:
- Read the requested location from the command line
- Download JSON weather data from OpenWeatherMap.org
- Convert the string of JSON data to a Python data structure
- Print the weather for today and the next two days

There, the code will need to do the following:
- Join strings in sys.argv to get the location
- Call requests.get() to download the weather
- Call json.loads() to convert the JSON data to a Python data structure
- Print the weather forecast

 '''
#! python 3
#! json_weatherdata.py - Prints the weather for a location from the command line
import json, requests, sys


## Step 1: Get Location from the Comman Line Argument
if len(sys.argv) < 2: # sys.argv is how Python stores command line arguments. There will always be sys.argv[0], aka 1 input, which is the file name entered on the command line, e.g. 'python filename.py'
    print('Usage: json_weatherdata.py location')
    sys.exit()
location = ' '.join(sys.argv[1:])  # We want the user to put in the location after the file name, if not, they will get the text from the first chunk of code 
                                   # Here, we are storing the user command-line input to a variable called 'location'


## Step 2: Download the JSON Data, using OpenWeatherData API: https://openweathermap.org/ 
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=d1d9afb79400a358bbd15097f1657bfb' % (location) # %s is a 'place holder', where the user input from the command line can be pasted 
                                                                                                                  # Note!: You need to register for an API key and past here. It can take a few hours after registration until you can use it successfully
response = requests.get(url)
response.raise_for_status() # raise_for_status() checks for errors. If no exception is raised, the downloaded text will be in 'response.text'



## Step 3: Load JSON Data and Print Weather
''' 
The 'response.text' variables holds a large string of JSON-formatted data. 
To convert this into a Python value, you need to call the json.loads() function.
To make the data print in a pretty way, do the following:
'''
weatherData = json.loads(response.text)
#print(weatherData)

# Print weather descriptions:
w = weatherData['weather']

'''
Note that for the next section, the book provides this code
# print(w[0]['weather'][0]['weather.main'], '-', w[0]['weather'][0]['weather.description']) # this is obtain dicts of the weather, and the description
HOWEVER, this does NOT work. See below for what does work!
'''
print()
print('Current weather in %s:' % (location))
print(w[0]['main'], '-', w[0]['description'])
print()

# Note also, the current API used is only for CURRENT weather, not 2.5 days