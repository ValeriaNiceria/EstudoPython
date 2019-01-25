# Atribuição
imposto = 0.27
salario = 5000
print('Valor real: {}'.format( salario - ( salario * imposto ) ) )


# Pegando dados no terminal
salario = int(input('Salario? '))
imposto = float(input('Imposto em % (ex.: 27.5)? '))
print('Valor real: {0}'.format(salario - (salario * imposto * 0.01)))


# Comparações: maior, menor, igual e outros
'''
(<) - menor que
(<=) - menor ou igual que
(>) - maior
(>=) - maior ou igual
(==) - igual
(!=) - não igual
'''

# Condicionaios: IF, ELIF & ELSE
salario = int(input('Salario? '))
imposto = input('Imposto em % (ex.: 27.5)? ')
if imposto == '':
    imposto = 27.5
else:
    imposto = float(imposto)
print('Valor real: {0}'.format(salario - (salario * imposto * 0.01)))


# Indentação dos blocos de código
imposto = float(input('Imposto: '))
if imposto < 10:
    print('Médio')
elif imposto < 28:
    print('Alto')
else:
    print('Muito alto')
    

# Operadores ternários
imposto = float(input('Imposto: '))
'Alto' if imposto > 27 else 'Baixo'
valor_imposto = 'Alto' if imposto > 27 else 'Baixo'
valor_imposto
    


# Operadores lógicos
imposto = float(input('Imposto: '))
if imposto < 10:
    print('Baixo')
elif imposto >= 10 and imposto <= 27:
    print('Médio')
elif imposto > 27 and imposto < 100:
    print('Alto')
else:
    print('Imposto inválido')


