'''
Crie um programa que leia quanto dinheiro uma
pessoa tem na carteira e mostre quantos dólares ela pode comprar.
Considere:
US$1,00 = R$3,27
'''

d = float(input('Quanto você tem em R$: '))
print('Você tem R$ {:.2f}'.format(d))
print('Você pode comprar US$: {:.2f}'.format(d / 3.27))
