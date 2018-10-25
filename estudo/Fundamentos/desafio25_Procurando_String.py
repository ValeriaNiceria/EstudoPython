'''
Crie um programa que leia o nome de uma pessoa
e diga se elea tem 'silva' no nome
'''

nome = str(input('Digite seu nome completo: ')).strip().lower()
print('O seu nome tem "SILVA"? {}'.format('silva' in nome))
