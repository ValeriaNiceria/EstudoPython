'''
Faça um programa que leia uma
frase pelo teclado e mostre:
- Quantas vezes aparece a letra 'A'.
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.
'''

f = str(input('Digite uma frase: ')).strip().lower()

print('A letra "A" aparece {} vezes.'.format(f.count('a')))
print('A letra "A" aparece a primeira vez na posição {}'.format(f.find('a')))
print('A letra "A" aparece por último na posição {}'.format(f.rfind('a')))
