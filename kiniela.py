import requests
from bs4 import BeautifulSoup

url = "http://www.quiniela15.com/pronostico-quiniela"
r = requests.get(url)

soup = BeautifulSoup(r.content)
data = soup.find_all("table", {"class":"results"})

for item in data:
	result = item.find_all("strong")
	header = item.find_all("th",{"class":"forecasttop"})

emaitzak = []
for res in result:
	emaitzak.append(res.string)

print header[0].string


i=0
while(i<30):
	print emaitzak[i] + ' - ' + emaitzak[i+1]
	i = i+2
