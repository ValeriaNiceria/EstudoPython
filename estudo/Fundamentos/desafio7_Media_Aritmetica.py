'''
Desenvolva um programa que leia as duas notas
de um aluno, calcule e mostre a sua média.
'''
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print('A primeira nota do aluno é {} e a segunda é {}'.format(n1, n2))
print('A média é {:.2f}'.format(media))
