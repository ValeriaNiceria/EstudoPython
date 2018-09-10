'''
Escreva um programa que faça o computador "pensar"
em um número inteiro entre 0 e 5 e peça para o usuário
tentar descobrir qual foi o escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu
'''
from random import randint

num = randint(0, 5)

numero = int(input('Digite um número inteiro entre 0 e 5: '))

if numero == num:
    print('Parabéns! Você acertou!')
else:
    print('Errou! Não foi dessa vez!')
