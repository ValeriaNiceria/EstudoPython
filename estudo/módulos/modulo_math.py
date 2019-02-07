'''
O comando 'import' pode importar módulos ou objetos(classes e funções)
'''
import math
print(math.sqrt(9)) # 3.0

# Dando um apelido para o módulo
import math as matematica
print(matematica.sqrt(9)) # 3.0


'''
Pode-se importar apenas um objeto específicode um módulo.
Neste caso, utilizamos o comando 'from/import'
'''
from math import sqrt as raiz
print(raiz(81)) # 9.0