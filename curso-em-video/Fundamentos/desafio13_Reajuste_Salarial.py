'''
Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento.
'''

s = float(input('Informe o salário de um funcionário R$ '))
print('O salário informado é R$ {:.2f}'.format(s))
print('O salário atual com "15%" de aumento é R$ {:.2f}'.format(s * 1.15))
