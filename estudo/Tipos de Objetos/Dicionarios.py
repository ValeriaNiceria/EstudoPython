aurelio = {
    'denominação': 'ilha solteira',
    'população': 23000,
    'renda': 1500
}

print('aurelio =>', aurelio)

aurelio['vocação'] = 'turismo'
print('aurelio =>', aurelio)

print('aurelio["renda"] =>', aurelio["renda"])
print('aurelio["renda"] + 500 =>', aurelio["renda"]  + 500)

# Verificando quais chaves o dicionário possui
print('aurelio.keys() =>', aurelio.keys())
# aurelio.has_key("idade")


# Retorna uma lista de tuplas contendo o par (chave, valor)
print('aurelio.items() =>', aurelio.items())