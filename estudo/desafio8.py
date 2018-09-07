'''
Escreva um programa que leia um valor em metros
e o exiba convertendo em centímetros e milímetros
'''

m = int(input('Digite um valor em metros: '))
c = m * 100
mm = m * 1000

print('O valor de {} metros em centímetros é {}'.format(m, c), end=' ')
print('e em milímetros é {}'.format(mm))
