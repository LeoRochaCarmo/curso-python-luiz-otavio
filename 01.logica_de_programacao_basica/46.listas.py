#%%
# Listas em Python
# Tipo list - Mutável
# Suporta vários valores de qualquer tipo
# Conhecimentos reutilizáveis - índices e fatiamento
# Métodos úteis: append, insert, pop, del, clear, extend, +
#        +01234
#        -54321

lista = [123, True, 'Leo', 1.2]
lista[2] = 'Luana'
print(lista[2].upper(), type(lista[2]))

# %%
# Alterando uma lista com índices, del, append e pop
lista = [10, 20, 30, 40]
numero = lista[2]
print(numero)

# %%
# Alterando pelo índice
numero = lista[2] = 5
print(numero)

# %%
# Apagar índice (DEL)
del lista[2]
print(lista)

# %%
# Adicionando itens na lista (APPEND)
lista.append(50)
print(lista)

# %%
# Remover o último elemento da lista (POP)
ultimo_valor = lista.pop()
print(lista, 'removido', ultimo_valor)

# %%
# Remover um elemento da lista (POP)
lista.pop(3)
print(lista)

# %%
# Remover último item sem saber o tamanho da lista [-1]
del lista[-1]
print(lista)

# %%
# Adicionar um item no índice escolhido (INSERT)
lista.insert(0, 5)
print(lista)

# %%
# Adicionar um item no final da lista (INSERT + LEN)
lista.insert(len(lista), 5)
print(lista)

# %%
# Juntando (concatenando) listas com +
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
print(lista_c)

# %%
# Juntando listas com EXTEND
lista_a.extend(lista_b)
print(lista_a)

# %%
# Cuidados com dados mutáveis
# = - copiado o valor (imutáveis)
nome = 'Leonardo' 
outra_variavel = nome
nome = 'Leandro'
print(nome, outra_variavel)

# %%
# = - aponta para o mesmo valor na memória (mutável)
lista_a = ['Leonardo', 'Luana']
lista_b = lista_a
lista_a[0] = 'Qualquer coisa'
print(lista_b)

# %%
# Usando o método .COPY()
lista_c = ['Leo', 'Luana']
lista_d = lista_c.copy()
lista_c[0] = 'Leonardo'
print(lista_c, lista_d)

# %%
# FOR IN com listas
lista = ['Leo', 'Luana', 'Luccas', 'Maria']
lista_upper = []
for nome in lista:
    lista_upper.append(nome.upper())

print(lista_upper)
    
# %%
# EXERCÍCIO -> Exiba os índices da lista
lista = ['Leo', 'Luana', 'Max']
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice])

