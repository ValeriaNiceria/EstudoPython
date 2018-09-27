"""
Desenvolva um programa que pergunte a distância de uma viagem
em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para
viagens de até 200Km e R$0,45 para viagens mais longas.
"""

distancia = float(input('Qual a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
	total = distancia * 0.5
else:
	total = distancia * 0.45
print('E o preço da sua viagem será de R${:.2f}'.format(total))


'''
Fazendo o if simplificado:
preco = distancia * 0.5 if distancia <= 200 else distancia * 0.45
'''
