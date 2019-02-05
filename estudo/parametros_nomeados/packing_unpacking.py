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
