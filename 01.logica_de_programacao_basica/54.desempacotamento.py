#%%
# Desempacotamento

# Pegando o primeiro e último item
string = 'ABCD'
lista = ['Leo', 'Rocha', 1, 2, 3, 'Carmo']
tupla = 'Python', 'é', 'legal'


p, b, *_, u = lista

print(p, u)

#%%
# Desempacotamento em chamadas de funções
# FORMA 1 -> Usando for
for nome in lista:
    print(nome, end = ' ')

#%%
# Desempacotamento em chamadas de funções
# FORMA 1 -> Usando * dentro do print
print(*lista)
print(*string)
print(*tupla)

#%%
# Pulando linhas com \n
print(*tupla, sep = '\n')
