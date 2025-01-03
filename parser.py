from bs4 import BeautifulSoup
import requests


url = "https://www.tutorialspoint.com/index.htm"
req = requests.get(url)

soup = BeautifulSoup(req.content, "lxml")

for link in soup.find_all('a'):
    print(link.get('href'))