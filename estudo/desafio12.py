'''
Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto.
'''
p = float(input('Informe o valor de um produto: '))
print('O valor do produto é R$ {:.2f}'.format(p))
print('O valor do produto com "5%" de desconto é R$ {:.2f}'.format(p * 0.95))
