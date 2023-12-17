import requests

url = "https://httpbin.org/headers"
auth_token = "XXXXXXXX"
header = {"Authorization": f"Bearer{auth_token}"}

response = requests.get(url, headers=header)
print(response.json())