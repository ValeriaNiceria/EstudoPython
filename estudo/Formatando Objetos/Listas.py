a = [1, 2, 3]
print('a =>', a)

# Adicionando valor ao final da lista
a.append('poncan')
print('a =>', a)

a.extend([0, 0, -2])
print('a =>', a)

# Inserindo um valor em um endereço específico
a.insert(0, 'start')
print('a =>', a)

# Removendo um valor
a.remove('start')
print('a =>', a)

a.pop(0)
print('a =>', a)

# Número de vezes que um elemento aparece
print('a.count(0) =>', a.count(0))


# Ordem decrescente
mohs = ['Talco', 'Gipsita', 'Calcita', 'Fluorita', 'Apatita', 'Ortoclásio', 'Quatzo', 'Topázio', 'Coríndon', 'Diamante']
print('mohs[::-1] =>', mohs[::-1])
