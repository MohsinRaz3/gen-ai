import requests

url = "https://httpbin.org/status/200"
response = requests.get(url)

print(response.status_code)


print(" \n conditional status \n")



url = "https://httpbin.org/status/500"
response = requests.get(url)

if response.status_code == 200: 
    print("success")   
else:
    print(f"HTTP Error: {response.status_code}")

    