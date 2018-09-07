'''
Um professor quer sortear um dos seus quadro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
'''

from random import sample

a1 = input('Primeiro Aluno: ')
a2 = input('Segundo Aluno: ')
a3 = input('Terceiro Aluno: ')
a4 = input('Quarto Aluno: ')

print('A ordem de apresentação é {}'.format(sample([a1, a2, a3, a4], k=4)))
