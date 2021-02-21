# Starting with creating mappings

airports = {
    'Stockholm': 'ARL',
    'Detroit': 'DTW',
    'Bucharest': 'OTP',
    'Tokyo': 'TYO',
    'Reykjavik': 'KEF'
}

countries = {
    'ARL': 'Sweden',
    'DTW': 'the United States',
    'OTP': 'Romania',
    'TYO': 'Japan',
    'KEF': 'Iceland'
}

# Adding some more
countries['BCL'] = 'Spain'
countries ['AMS'] = 'Netherlands'


# Printing out some airports based on state
print('-' * 10)
print('Names of airports and their codes')
print('The main airport in Stockholm is: ', airports['Stockholm'])
print('The main airport in Bucharest is: ', airports['Bucharest'])

# Printing some  + airports
print('-' * 10)
print('Names of airports and their countries')
print('ARL airport is located in the country of: ', countries['ARL'])
print('KEF airport is in: ', countries['KEF'])

# Printing out every airport in the dic, and their city + country
print('-' * 10)
print("All the info we have on airport codes and their location")
for city, code in list(airports.items()):
    print(f"{city}'s airport has the code {code}") # Needs to follow the order they appear in the dict?
    print(f"and it is located in {countries[code]}.")
    print("  ")
