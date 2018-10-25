frase = 'Aprendendo Python'

print(frase)

# Fatiando a string
print(frase[3])
print(frase[3:10])
print(frase[2:])
print(frase[3::2])
print(frase[::3])

# Analisando
print(len(frase))
print(frase.count('e'))
print(frase.count('e', 6, 13))
print(frase.find('Python'))
print(frase.find('Estudando'))
print('Aprendendo' in frase)


# Transformação
print(frase.replace('Aprendendo', 'Estudando'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase.strip())
print(frase.rstrip())
print(frase.lstrip())


# Divisão
print(frase.split())
dividido = frase.split()
print(dividido[1])


# Junção
print('*'.join(frase))
frase = frase.split()
print('*'.join(frase))
