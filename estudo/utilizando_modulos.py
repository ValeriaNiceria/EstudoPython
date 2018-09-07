# importa todas as funções do módulo
# import math
# raiz = math.sqrt(num)

# importa uma função específica
from math import sqrt

num = int(input('Digite um número: '))

raiz = sqrt(num)
print('A raiz quadrada de {} é igual a {:.2f}'.format(num, raiz))
