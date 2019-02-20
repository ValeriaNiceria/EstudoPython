# -*- coding: utf-8 -*-
"""
Laboratório 
Desenvolvendo uma calculadora em Python
"""

print('**********************  Python Calculator *********************** \n')
print('Selecione o número da operação desejada: \n')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')

opNum = int(input('Digite sua opção (1/2/3/4): '))
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

def calculator(opNum, num1, num2):
    if opNum == 1 :
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
    elif opNum == 2:
        print('{} - {} = {}'.format(num1, num2, num1 - num2))
    elif opNum == 3:
        print('{} * {} = {}'.format(num1, num2, num1 * num2))
    elif opNum == 4:
        print('{} / {} = {}'.format(num1, num2, num1 / num2))
    else:
        print('\nOpção inválida!')
    
    
# Chamando a função
calculator(opNum, num1,num2)



