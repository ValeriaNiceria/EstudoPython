# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


links_lista = []
titulos_lista = []
for page in range(1, 7):
	url = "http://dadosabertos.dataprev.gov.br/dataset?tags=Previd%C3%AAncia+Social&page=" + str(page)
	req = requests.get(url)	


	soup = BeautifulSoup(req.text, 'lxml')

	
	for link in soup.find_all('h3', class_ = "dataset-heading"):
		links_lista.append(link.a['href'])
		titulos_lista.append(link.a.text)


print(links_lista)
print(titulos_lista)



# http://dadosabertos.dataprev.gov.br/
# http://dados.gov.br/organization/previdencia
# http://www.previdencia.gov.br/dados-abertos/
