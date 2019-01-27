# -*- coding: utf-8 -*-
"""
* Exemplos de listas
- [1, 2, 3, 4, 5]
- ['salario', 'imposto']
- [1, 'salrio']
- [[1, 2, 3], 'salario', 10]
"""
lista = ['imposto', 'salario', 'altos', 'baixos']
lista
lista[0]
lista[-1]
lista[2:4] # utilizando slice notation

# Realizando atribuições em índices
lista[2] = 'Altos'
lista[3] = 'Baixos'
lista
lista[0:2] = ["Impostos", "Salarios"]
lista

# ifs e listas
# lista vazia é igual a falso
lista1 = []
if lista1:
    print('Nunca sou executado')
else:
    print('Sempre sou executado')
