'''
Practicing using 'requests' module 
From 'Automate the Boring Stuff' - No Starch Press, pg 237
'''

import requests
res = requests.get('ttp://www.gutenberg.org/cache/epub/1112/pg1112.txt')
type(res)

res.status_code == requests.codes.ok # This helps you know if it was successful, it should return True if it was. 

len(res.text) # Check the length

print(res.text[:250]) # This displays only the first 250 characters