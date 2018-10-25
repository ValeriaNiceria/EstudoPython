'''
Faça um programa que leia o nome completo
de uma pessoa, mostrando em seguida o primeiro
e o último nome separadamente.
'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Primeiro: {}'.format(nome.split()[0]))
print('último: {}'.format(nome.split()[int(len(nome.split()) - 1)]))
