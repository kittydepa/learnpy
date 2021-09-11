import requests

response = requests.get("http://quotesondesign.com/wp-json/wp/v2/posts/?orderby=rand")
print(response.status_code)
print(response.json())