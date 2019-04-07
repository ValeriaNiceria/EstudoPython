# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import pandas as pd
import io
import pyrebase


config = {
  "apiKey": "AIzaSyDbFkmBkwwL7ZY4ZIIzlBbuF_s4mvn-tiQ",
  "authDomain": "previdencia-projeto.firebaseapp.com",
  "databaseURL": "https://previdencia-projeto.firebaseio.com",
  "storageBucket": "previdencia-projeto.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()


links_lista = []
titulos_lista = []
for page in range(1, 7):
	url = "http://dadosabertos.dataprev.gov.br/dataset?tags=Previd%C3%AAncia+Social&page=" + str(page)
	req = requests.get(url)	

	soup = BeautifulSoup(req.text, 'lxml')
	
	for link in soup.find_all('h3', class_ = "dataset-heading"):
		links_lista.append(link.a['href'])
		titulos_lista.append(link.a.text)



for i in range(len(links_lista)):
	url = "http://dadosabertos.dataprev.gov.br" + links_lista[i]
	req = requests.get(url)

	titulo = titulos_lista[i]
	titulo = titulo.replace('.', '-')
	titulo = titulo.replace('/', '-')
	titulo = titulo.replace('$', '')
	titulo = titulo.replace('#', '')	
	titulo = titulo.replace('[', '')
	titulo = titulo.replace(']', '')
	print('Título:', titulo)

	soup = BeautifulSoup(req.text, 'lxml')

	descricacao = soup.find(class_ = "embedded-content").p.text
	info = soup.find_all("td", class_ = "dataset-details");
	
	informacoes = {
		'titulo': titulo,
		'descricacao': descricacao,
		'link': url,
		'info_adicional': {
			'autor': info[0].next_element,
			'mantenedor': info[1].next_element,
			'cobertura_geografica': info[2].next_element,
			'documentacao': info[3].next_element,
			'frequencia_de_atualizacao': info[4].next_element,
			'granularidade_geografica': info[5].next_element,
			'granularidade_temporal': info[6].next_element,
			'vcge': info[7].next_element
		}
	}

	# Enviando os dados para o Firebase
	db.child(titulo).set(informacoes)


	resource_item = soup.find("li", class_ = "resource-item")
	csv_url = resource_item.find(class_ = "resource-url-analytics")["href"]
	csv = requests.get(csv_url).content
	df = pd.read_csv(io.StringIO(csv.decode('latin1')), error_bad_lines=False, sep=',')

	colunas = df.columns.values

	for coluna in colunas:

		if (df[coluna].dtype == 'float64'):
			# Se o tipo da coluna for float
			# print('Describe:', df[coluna].describe().transpose().head())
			desc_index = df[coluna].describe().index
			desc_value = df[coluna].describe().tolist()

			data_coluna = {}
			for d_i in range(len(desc_index)):
				data_coluna[desc_index[d_i]] = desc_value[d_i]

			coluna = coluna.replace('.', '-')
			coluna = coluna.replace('/', '-')
			coluna = coluna.replace('$', 'S')
			coluna = coluna.replace('#', '')	
			coluna = coluna.replace('[', '')
			coluna = coluna.replace(']', '')
			dados_coluna = {
				'coluna': coluna,
				'tipo': 'float',
				'dados_coluna': data_coluna
			}

			# Enviando os dados para o Firebase
			db.child(titulo + '/variaveis/' + coluna).set(dados_coluna)
		elif (df[coluna].dtype == 'int64'):
			# Se o tipo da coluna for inteiro
			desc_index = df[coluna].describe().index
			desc_value = df[coluna].describe().tolist()

			data_coluna = {}
			for d_i in range(len(desc_index)):
				data_coluna[desc_index[d_i]] = desc_value[d_i]

			coluna = coluna.replace('.', '-')
			coluna = coluna.replace('/', '-')
			coluna = coluna.replace('$', 'S')
			coluna = coluna.replace('#', '')	
			coluna = coluna.replace('[', '')
			coluna = coluna.replace(']', '')
			dados_coluna = {
				'coluna': coluna,
				'tipo': 'int',
				'dados_coluna': data_coluna
			}

			# Enviando os dados para o Firebase
			db.child(titulo + '/variaveis/' + coluna).set(dados_coluna)
		elif (df[coluna].dtype == 'object'):

			coluna_em_lista = df[coluna].tolist();
			
			try:
				coluna_tratada = list(map(lambda x: x.replace('-', ''), coluna_em_lista))
			except AttributeError:
				coluna_tratada = coluna_tratada

			try:
				coluna_tratada = list(map(lambda x: x.replace('R$', ''), coluna_tratada))
			except AttributeError:
				coluna_tratada = coluna_tratada

			try:
				coluna_tratada = list(map(lambda x: x.replace('nan', ''), coluna_tratada))
			except AttributeError:
				coluna_tratada = coluna_tratada 

			try:
				coluna_tratada = list(map(float, coluna_tratada))
				teste = pd.DataFrame(coluna_tratada)
				print('Float:', teste)
			except ValueError:

				try:
					value_counts_index = list(map(lambda x: x.replace('.', ' '), df[coluna].value_counts().index))
				except AttributeError:
					value_counts_index = df[coluna].value_counts().index

				try:
					value_counts_value = list(map(lambda x: x.replace('.', ' '), df[coluna].value_counts().tolist()))
				except AttributeError:
					value_counts_value = df[coluna].value_counts().tolist()
				
				data_coluna = {}
				for v_i in range(len(value_counts_index)):
					data_coluna[value_counts_index[v_i]] = value_counts_value[v_i]

				print('data_coluna:', data_coluna)

				coluna = coluna.replace('.', '-')
				coluna = coluna.replace('/', '-')
				coluna = coluna.replace('$', 'S')
				coluna = coluna.replace('#', '')	
				coluna = coluna.replace('[', '')
				coluna = coluna.replace(']', '')
				dados_coluna = {
					'coluna': coluna,
					'tipo': 'string',
					'dados_coluna': data_coluna
				}

				# Enviando os dados para o Firebase
				db.child(titulo + '/variaveis/' + coluna).set(dados_coluna)

			#print('*** # object # ***')
			# valores = df[coluna].astype('float64', errors='ignore')
			# print('Index:', valores.value_counts().index)
			# print('Valor', valores.describe().tolist())

#print(links_lista)
#print(titulos_lista)



# http://dadosabertos.dataprev.gov.br/
# http://dados.gov.br/organization/previdencia
# http://www.previdencia.gov.br/dados-abertos/
