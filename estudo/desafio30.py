'''
Crie um programa que leia um número inteiro
e mostre na tela se ele é PAR ou ÍMPAR.
'''
num = int(input('Me diga um número qualquer: '))

resultado = num % 2

if resultado == 0:
	print('O número {} é \033[1;33;42mPAR.\033[m'.format(num))
else:
	print('O número {} é \033[1:35;40mÍMPAR.\033[m'.format(num))
