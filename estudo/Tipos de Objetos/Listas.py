lista = [1, 2, 3]
print(lista)

print('lista[0] =>', lista[0])
print('lista[0] + lista[2] =>', lista[0] + lista[2])

lista += [4]
print('lista', lista)

lista += [0, 0, 0]
print('lista', lista)

print('lista[-1] =>', lista[-1])
print('lista[2:-2] =>', lista[2:-2])

print('tamanho', len(lista))

lista[0] = 'zero'
print('lista =>', lista)

lista[3] = lista[0]
print('lista =>', lista)



linha1 = [1, 2, 3]
linha2 = [0, -1, 1]
linha3 = [3, 3, 3]
matriz = [linha1, linha2, linha3]
print('matriz =>', matriz)

print('matriz[1] =>', matriz[1])
print('matriz[1][2] =>', matriz[1][2])