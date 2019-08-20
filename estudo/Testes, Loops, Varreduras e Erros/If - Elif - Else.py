x = int(input('Informe um número: '))

if x < 0:
    print('O número %i é menor que zero.' %(x))
elif x > 0:
    print('O número %i é maior que zero.' %(x))


b = 1
while b < 5:
    if b == 1:
        print('%i dólar vale %.2f reais' %(b, b*4.06))
    else:
        print('%i dólares valem %.2f reais' %(b, b*4.06))
    b += 1