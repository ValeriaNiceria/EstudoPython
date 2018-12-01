'''
Faça um programa que leia três números e 
mostre qual é maior e qual é o menor.
'''

primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
terceiro = int(input('Terceiro valor: '))

menor = primeiro

if ( segundo < primeiro and segundo < terceiro ):
	menor = segundo
if ( terceiro < primeiro and terceiro < segundo ):
	menor = terceiro

maior = primeiro

if ( segundo > primeiro and segundo > terceiro ):
	maior = segundo
if ( terceiro > primeiro and terceiro > segundo ):
	maior = terceiro


print('O maior número é {} e o menor número é {}.'.format(maior, menor))