'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas.
- O nome com todas minúsculas.
- Quantas letras ao todo (sem considerar espaços)
- Quantas letras tem o primeiro nome.
'''

nome = input('Digite o seu nome compĺeto: ')

print('O seu nome com todas as letras maiúsculas: {}'.format(nome.upper()))
print('O seu nome com todas as letras minúsculas: {}'.format(nome.lower()))

nomeJunto = nome.split()
nomeJunto = ''.join(nomeJunto)
print('O seu nome tem {} letras'.format(len(nomeJunto)))

primeiroNome = nome.split()
print('O seu primeiro nome tem {} letras'.format(len(primeiroNome[0])))
