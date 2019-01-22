# importando o modulo statistics
import statistics as stats
valores = [10, 3, 35, 25, 34, 98, 30, 45, 25, 34, 2]

# Media Aritmetica
mediaArit = stats.mean(valores)
print('Media Aritmetica: {:.2f}'.format(mediaArit))

# Media Geometrica
from functools import reduce
produtoLista = reduce(lambda x, y: x*y, valores)
tamanhoLista = len(valores)
mediaGeo = produtoLista ** (1 / tamanhoLista)
print('Media Geometrica: {:.2f}'.format(mediaGeo))


# Media Harmonica
mediaHarm = stats.harmonic_mean(valores)
print('Media Harmonica: {:.2f}'.format(mediaHarm))