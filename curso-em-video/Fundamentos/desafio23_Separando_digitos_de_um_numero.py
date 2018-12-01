'''
Faça um programa que leia um número de 0 a 9999 e monstre na tela
cada um dos dígitos separados.
'''
n = int(input('Digite um número de "0" até "9999": '))

un = n // 1 % 10
dez = n // 10 % 10
cent = n // 100 % 10
mil = n // 1000 % 10

print('Unidade: {}'.format(un))
print('Dezena: {}'.format(dez))
print('Centena: {}'.format(cent))
print('Milhar: {}'.format(mil))
