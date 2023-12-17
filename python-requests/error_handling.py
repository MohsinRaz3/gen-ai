import requests

url = "https://httpbin.org/status/200"
try:
    response = requests.get(url)
    if response.status_code ==200:
        print("Data successfully retreived")
    else:
        response.raise_for_status()
except requests.exceptions.HTTPError as err:  #this err handling won't crash our app
    print(f'This is xception: {err}')