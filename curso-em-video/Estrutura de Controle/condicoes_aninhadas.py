# Condições Aninhadas
nome = input("Qual o seu nome? ")
if nome == "Valéria":
    print("Que nome bonito".format(nome))
elif nome == "Maria" or nome == "José" or nome == "João":
    print("Seu nome é bem popular no Brasil.".format(nome))
elif nome in "Ana Cláudia Jéssica Juliana":
    print("Que nome feminino bonito")
else:
    print("Seu nome é bem normal.")
print("Tenha um bom dia, {}!".format(nome))
