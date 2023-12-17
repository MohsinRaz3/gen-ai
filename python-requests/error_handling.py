import requests

url = "https://httpbin.org/status/400"
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.HTTPError as err:  #this err handling won't crash our app
    
    print(err)