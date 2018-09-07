'''
Faça um programa que leia o comprimento do cateto
oposto e do cateto adjacente de um triângulo retângulo.
Calcule o comprimento da hipotenusa.
'''

import math

catOposto = float(input('Informe o comprimento do cateto oposto: '))
catAjacente = float(input('Informe o comprimento do cateto adjacente: '))

hipotenusa = math.sqrt(math.pow(catOposto, 2) + math.pow(catAjacente, 2))

print('O comprimento da hipotenusa é igual: {:.1f}'.format(hipotenusa))
