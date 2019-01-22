# importando o módulo statistics
import statistics as stats
valores = [10, 3, 35, 25, 34, 98, 30, 45, 25, 34, 2]

# Média Aritmética
mediaArit = stats.mean(valores)
print('Média Aritmética: {:.2f}'.format(mediaArit))

# Média Geométrica
from functools import reduce
produtoLista = reduce(lambda x, y: x*y, valores)
tamanhoLista = len(valores)
mediaGeo = produtoLista ** (1 / tamanhoLista)
print('Média Geométrica: {:.2f}'.format(mediaGeo))