# Introdução à List comprehension em Python
# List comprehension é uma forma rápida para criar listas
# a partir de iteráveis.

#%%
# gerando uma lista
print(list(range(10)))

#%%
#gerando lista com for

lista = []

for numero in range(10):
    lista.append(numero)

print(lista)

#%% gerando lista com list comprehension

lista = [
    numero * 2
    for numero in range(10)
]

print(lista)

#%%
# Mapeamento de dados