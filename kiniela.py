import requests
import datetime
from bs4 import BeautifulSoup

meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
# meses.index("Marzo") + 1



def get_kiniela(url):
	r = requests.get(url)
	soup = BeautifulSoup(r.content)
	data = soup.find_all("table", {"class":"results"})

	result = data[0].find_all("strong")
	header = data[0].find_all("th",{"class": "forecasttop"})

	txtinput = soup.findAll('input', {'type':'hidden', 'id':'systembets'})
	txt = txtinput[0]["value"]
	pronosticos = txt.split(",")
	
	text_array = header[0].string.split(" ")
	dia = int(text_array[3])
	mes = meses.index(text_array[5]) + 1
	year = int(datetime.datetime.today().year)

	data = datetime.datetime(year,mes,dia)
	dia_de_la_semana = data.weekday()

	hurrengoko_data = soup.find_all("a", {"class": "next_prev"})
	hurrengo_linka = "http://www.quiniela15.com" + hurrengoko_data[1]["href"]

	emaitzak = []
	for res in result:
		emaitzak.append(res.string)

	print header[0].string

	i=0
	kinielak = []
	while(i<30):
		kinielak.append(str(i/2+1) + ' - ' + emaitzak[i] + ' - ' + emaitzak[i+1])
		#print str(i/2+1) + ' - ' + emaitzak[i] + ' - ' + emaitzak[i+1]
		i = i+2

	emaitza = {}
	emaitza["kinielak"] = kinielak
	emaitza["hurrengo_linka"] = hurrengo_linka
	emaitza["asteko_eguna"] = dia_de_la_semana
	emaitza["data"] = data
	emaitza["pronostikuak"] = pronosticos
	return emaitza

url = "http://www.quiniela15.com/pronostico-quiniela"
emaitza = get_kiniela(url)
print emaitza