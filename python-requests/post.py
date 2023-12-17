import requests

data = {"name": "mohsin", "profession": "web developer"}
url = "https://www.httpbin.org/post"

response = requests.post(url, json=data)
print(response)
print(response.content)