'''
-------------------
****  Packing ****
-------------------
'''

# Primeiro exemplo
from datetime import date
d = (2019, 2, 5)
print(date(d[0], d[1], d[2]))

# Usando Packing
print(date(*d)) # usando a sintaxe do *tupla


# - Outro exemplo
def new_user(active=False, admin=False):
    print(active)
    print(admin)
    
config = {"active": False, "admin": True}
new_user(config.get('active'), config.get('admin'))

# Usado Packing
new_user(**config) # neste caso, a sintaxe é **dicionário


'''
---------------------------------
*********** Unpacking  **********
É um processo que é executado
dentro da função, e não na chamada
----------------------------------
'''
def unpacking_experiment(*args):
    arg1 = args[0]
    arg2 = args[1]
    others = args[2:]
    print(arg1)
    print(arg2)
    print(others)

# Usando
unpacking_experiment(1, 2, 3, 4, 5, 6, 7)


def unpacking_experiment2(**kwargs):
    print(kwargs)

# Usando
unpacking_experiment2(name="Teste", other="Other")