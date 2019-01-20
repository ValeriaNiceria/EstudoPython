"""
* DESAFIO 35
- Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se eles podem ou
não formar um triângulo.
"""
lado1 = float(input("Primeiro lado: "))
lado2 = float(input("Segundo lado: "))
lado3 = float(input("Terceiro lado: "))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2 :
    print("Os lados informados PODEM formar um triângulo!")
else :
    print("Os lados informados NÃO PODEM formar um triângulo!")

    