# Practice with JSON and the dumps() function - to convert Python style strings/data to JSON style

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zohpie', 'felineIQ': None}

import json
stringOfJsonData = json.dumps(pythonValue)

print(stringOfJsonData)
