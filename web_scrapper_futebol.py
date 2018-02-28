import mechanize
import cookielib
from BeautifulSoup import BeautifulSoup
import html2text
import re
import json 

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-agent', 'Chrome')]

# The site we will navigate into, handling it's session
br.open('https://www.academiadasapostasbrasil.com/users/login')

#View available forms
#for f in br.forms():
#    print f

# Select the second (index one) form (the first form is a search query box)
br.select_form(nr=1)

# User credentials
br.form['user'] = '' #Set your user
br.form['passwrd'] = '' #Set your password
# Login
br.submit()

result = br.open('https://www.academiadasapostasbrasil.com/stats/match/brasil-stats/brasileirao-serie-a/flamengo/avai/2419207/1/odds').read()
data = re.search("var graphOddsSeries = JSON.parse\((.+?)\)", result)
json_data = json.loads(data.group(1)[1:len(data.group(1))-1])

output = ""
for res in range(3):
	color = json_data[res]['color']
	time = re.search("<span style=\"background-color:"+color+";\"></span>(.+?)</span>", result).group(1)
	data = json_data[res]['data']
	for n in range(len(data)):
		print(time, data[n]['y'])