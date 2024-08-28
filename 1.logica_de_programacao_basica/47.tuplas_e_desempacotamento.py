#%%
# Intro ao desempacotamento + tuples (tuplas)

nomes = ['Leo', 'Luana', 'Max']
nome1, nome2, nome3 = nomes
print(nome2)

# %%
# Pegando apenas o primeiro valor (*)
nome1, *resto = nomes
print(nome1, resto)

# %%
# *_ -> Convenção para variável que não será utilizada
nome1, *_ = nomes
print(nome1, _)

# %%
# Pegando apenas o segundo valor (*)
_, nome2, *_ = nomes
print(nome2)

# %%
# Pegando apenas o terceiro valor (*)
_, _, nome3 = nomes
print(nome3)

# %%
# Tipo tupla -> Uma lista imutável
nomes = 'Leo', 'Luana', 'Max' # SEM OS COLCHETES OU
nomes = ('Leo', 'Luana', 'Max') # COM PARARENTESES
print(nomes[1])

# %%
# Converter lista para tupla
nomes = ['Leo', 'Luana', 'Max']
nomes = tuple(nomes)
print(nomes)

# %%
# Converter tupla para lista
nomes = 'Leo', 'Luana', 'Max'
nomes = list(nomes)
print(nomes)

# %%
