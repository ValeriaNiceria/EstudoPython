# No Python as variáveis armazenam endereços de memória e não os valores.
x = [1, 2, 3]
y = x
x.append(4)
print(y)