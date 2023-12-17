import requests
from bs4 import BeautifulSoup

url= "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
#print(soup)

title = soup.title.text
content = soup.find("p").text
links = [a["href"]for a in soup.find_all("a")]

print(f"Title: {title}",f"\n Content: {content}", f"\nLinks: {links}")