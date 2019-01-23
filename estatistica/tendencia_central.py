# importando o modulo statistics
import statistics as stats
valores = [10, 3, 35, 25, 34, 98, 30, 45]

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

# Moda
# stats.mode(valores)
idades = [10, 20, 12, 4, 54, 12, 10]
# Verificando a quantidade de vezes que cada elemento do conjunto aparece
idadeCount = [[x, idades.count(x)] for x in set(idades)]
print('idadeCount:', idadeCount)
# Removendo valores que apareceram somente uma vez
moda = [x for x in set(idades) if idades.count(x) > 1]
print('Moda:', moda)


# Mediana
lista = [4, 5, 20, 1, 6, 12, 8, 14]
mediana = stats.median(lista)
print('Mediana:', mediana)

