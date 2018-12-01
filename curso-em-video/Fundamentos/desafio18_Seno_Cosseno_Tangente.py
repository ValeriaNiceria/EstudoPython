'''
Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo.
'''
import math

angulo = float(input('Informe o valor de um ângulo: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print('O seno de {} é igual a {:.2f}'.format(angulo, seno))
print('O cosseno de {} é igual a {:.2f}'.format(angulo, cosseno))
print('A tangente de {} é igual a {:.2f}'.format(angulo, tangente))
