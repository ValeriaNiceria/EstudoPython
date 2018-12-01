'''
Faça um programa que leia um número inteiro
e mostre na tela o seu sucessor e seu antecessor
'''

n = int(input('Digite um número: '))
suc = n + 1
ant = n - 1

print('O número digitado é {}'.format(n), end=' >>> ')
print('o seu sucessor é {}, e seu antecessor é {}'.format(suc, ant))
