'''
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta, pinta uma área de 2m².
'''

l = float(input('Digite uma largura: '))
a = float(input('Digite uma altura: '))

area = l * a

print('A largura informada é {:.1f}m e a altura é {:.1f}m'.format(l, a))
print('A área é {:.2f}m²'.format(area))
print('A quantidade de tinta necessária é {:.2f} litros.'.format(area / 2))
