"""
* DESAFIO 34
- Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""
salario = float(input("Qual o salário do funcionário? R$"))

if salario <= 1250 :
    salarioFinal = salario * 1.15
else:
    salarioFinal = salario * 1.10

print("Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.".format(salario, salarioFinal))