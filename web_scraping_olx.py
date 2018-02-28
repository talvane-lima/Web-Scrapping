import requests
import re
from bs4 import BeautifulSoup
search = 'moto z play' #Set your search
file = open(search.replace(' ','_')+".csv", "w")
file.close()
search.replace('_', '+')
page = requests.get("http://pa.olx.com.br/regiao-de-belem/eletronicos-e-celulares?ot=1&q="+search)
soupPhone = str(BeautifulSoup(page.content, 'html.parser')).replace('\n', '').replace('\t', '')
numPag = int(re.search('<li class="item last"><a class="link" href="(.+?)o=(.+?)&(.+?)"', soupPhone).group(2)) + 1
for pag in range(1,numPag):
	file = open(search.replace(' ','_')+".csv", "a")
	print(pag)
	try:
		page = requests.get("http://pa.olx.com.br/regiao-de-belem/eletronicos-e-celulares?o="+str(pag)+"&ot=1&q="+search+"&sp=1")
	except:
		print("Error page:"+str(pag))
		continue
	soup = BeautifulSoup(page.content, 'html.parser')
	filtred = soup.find_all('a', class_="OLXad-list-link")
	output = ''
	for i in range(len(filtred)):
		try:
			link = re.search('href="(.+?)"', str(filtred[i])).group(1).replace('amp;', '')
			pagePhone = requests.get(link)
			soupPhone = str(BeautifulSoup(pagePhone.content, 'html.parser'))
			listID = re.search("'listID': '(.+?)'", soupPhone)
			vendedor = re.search("'sellerName': '(.+?)'", soupPhone)
			price = re.search("'price': '(.+?)'", soupPhone)
			cidade = re.search("'region': '(.+?)'", soupPhone)
			soupPhone = soupPhone.replace('\n', '').replace('\t', '')
			desc = re.search('<div class="OLXad-description mb30px"><p class="text">(.+?)</p>', soupPhone)
			date = re.search('<div class="OLXad-date mb5px"><p class="text">(.+?)</p>', soupPhone)
			output += listID.group(1)+";"+vendedor.group(1)+";"+price.group(1)+";"+cidade.group(1)+";"+desc.group(1).replace('<br>', '').replace('</br>', '').replace('amp;', '')+";"+date.group(1).replace('<br>', '').replace('</br>', '').replace('amp;', '')+"\n"
		except Exception as e:
			print("Error pagePhone:"+str(pag))
			continue
	file.write(output)
	file.close()