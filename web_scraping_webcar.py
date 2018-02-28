import requests
import re
from bs4 import BeautifulSoup

for pag in range(1,6121):
	file = open("webmotors.csv", "a")
	print(pag)
	try:
		page = requests.get("https://www.webmotors.com.br/carros/estoque?tipoveiculo=carros&anunciante=concession%C3%A1ria%7Cloja&estadocidade=estoque&p="+str(pag)+"&o=1&qt=36")
	except:
		print("Error page:"+str(pag))
		continue
	#print("https://www.webmotors.com.br/carros/estoque?tipoveiculo=carros&estadocidade=estoque&p="+str(pag))
	soup = BeautifulSoup(page.content, 'html.parser')
	filtred = soup.find_all('a', class_="nn tipo1 c-after")
	output = ''
	for i in range(len(filtred)):
		try:
			link = re.search('href="(.+?)"', str(filtred[i]))
			pageCar = requests.get(link.group(1))
			soupCar = str(BeautifulSoup(pageCar.content, 'html.parser'))
			cidade = re.search("'nmCidade':'(.+?)'", soupCar)
			estado = re.search("'nmEstado':'(.+?)'", soupCar)
			cod = re.search("'codAnunciante':'(.+?)'", soupCar)
			nVendedor = re.search("<p class=\"txt-nome-vendedor-pj(.+?)\">\n<strong>(.+?)</strong>", soupCar)
			output += cod.group(1)+","+estado.group(1)+","+cidade.group(1)+","+nVendedor.group(2)+"\n"
			#print(cod.group(1)+","+estado.group(1)+","+cidade.group(1)+","+nVendedor.group(2))
		except Exception as e:
			print("Error pageCAR:"+str(pag))
			continue
	file.write(output)
	file.close()