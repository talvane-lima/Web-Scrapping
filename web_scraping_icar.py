import requests
import re
from bs4 import BeautifulSoup

for pag in range(1,2):
	file = open("icar.csv", "a")
	print(pag)
	try:
		page = requests.get("http://www.icarros.com.br/ache/listaanuncios.jsp?bid=2&app=20&sop=tan_2.6_-nta_17|44|51.1_-esc_4.1_-sta_1.1_&pas=6&lis=0&pag="+str(pag)+"&ord=0")
	except:
		print("Error page:"+str(pag))
		continue
	#print("http://www.icarros.com.br/ache/listaanuncios.jsp?bid=2&app=20&sop=tan_2.6_-nta_17|44|51.1_-esc_4.1_-sta_1.1_&pas=6&lis=0&pag="+str(pag)+"&ord=0")
	soup = BeautifulSoup(page.content, 'html.parser')
	filtred = soup.find_all('div', class_="clearfix dados_anuncio")
	print(filtred)
	output = ''
	'''
	for i in range(len(filtred)):
		print(filtred[i])
		try:
			link = re.search('href="(.+?)"', str(filtred[i]))
			pageCar = requests.get("http://www.icarros.com.br"+link.group(1))
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
	file.close()'''