'''
Crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome 'Santo'.
'''

city = input('Digite o nome de uma cidade: ').strip()

i = city[:5]

print('A cidade começa com o nome "SANTO"? {}'.format('santo' in i.lower()))
