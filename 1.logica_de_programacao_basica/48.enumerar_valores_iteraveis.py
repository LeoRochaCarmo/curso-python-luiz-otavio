#%%

lista = ['Leo', 'Luana', 'Max']
lista_enumerada = enumerate(lista)
print(lista_enumerada)

# %%
for i in lista_enumerada:
    print(i)

# %%

print(list(lista_enumerada))

# %%
for item in enumerate(lista):
    indice, nome = item
    print(indice, nome)

# %%
for indice, nome in enumerate(lista):
    print(indice, nome)
# %%
