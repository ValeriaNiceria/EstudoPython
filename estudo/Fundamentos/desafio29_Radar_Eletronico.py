"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem
dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""
velocidade = int(input('Digite a velocidade do veículo: '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('\033[1;31;47mVocê excedeu o limite permitido de 80Km/h.\033[m')
    print('E foi multado em R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia!')
