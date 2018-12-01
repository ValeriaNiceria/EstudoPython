print('{:*^20}'.format('Média'))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6:
	print('Sua média é boa! Parabéns!')
else:
	print('Sua média foi ruim! Estude mais!')

# print('Parabéns' if m >= 6 else 'estude mais')
