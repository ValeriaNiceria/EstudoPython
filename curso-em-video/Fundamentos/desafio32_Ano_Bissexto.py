'''
Faça um programa que leia um ano qualquer
e mostre se ele é BISSEXTO.
'''

from datetime import date

anoAnalisar = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))

if ( anoAnalisar == 0 ) :
	anoAnalisar = date.today().year

if ( anoAnalisar % 4 == 0 and anoAnalisar % 100 != 0 or anoAnalisar % 400 == 0 ):
	print('O ano {} é BISSEXTO.'.format(anoAnalisar))
else:
	print('O ano {} NÃO é BISSEXTO.'.format(anoAnalisar))