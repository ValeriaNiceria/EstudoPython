# Declarando Funções: Comando DEF
# Funções são objetos de primeira classe (first class objects)
def soma(a, b):
    return a + b
c = soma(1, 2)
print('A soma dos valores é igual', c)

# Valores padronizados de argumentos
def salario_descontado_imposto(salario, imposto=27):
    return salario - (salario * imposto * 0.01)

print('Salario descontando imposto: ', salario_descontado_imposto(1500))