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
# Mapeamento de dados em list comprehension

# Em termos simples, mapeamento de dados com list comprehension é quando
#  você percorre uma lista (ou outro iterável), aplica uma transformação 
# a cada item dessa lista e cria uma nova lista com os resultados dessa transformação.

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05}
    for produto in produtos
]

print(*novos_produtos, sep= '\n')

#%%
# Aumentar o preço do produto apenas se for maior que R$20,00

novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
]

print(*novos_produtos, sep= '\n')

#%%
# Filtro de mapeamentos (if que vem DEPOIS do for)
import pprint # módulo pretty-print

def p(v): # função para imprimir
    pprint.pprint(v, sort_dicts=False, width=40)

lista = [n for n in range(10) if n < 5] # filtro (if depois do for)

p(lista)

#%%
# Filtrando produtos com preço maior que R$10,00
novos_produtos = [
    {**produto, 'preco': produto['preco'] * 1.05} 
    if produto['preco'] > 20 else {**produto}
    for produto in produtos
    if produto['preco'] > 10
]

p(novos_produtos)

#%%
# List comprehension com mais de um for

# Sem list comprehension
lista = []

for x in range(3):
    for y in range (3):
        lista.append((x,y))

# Com list comprehension
lista = [
    (x,y) 
    for x in range(3)
    for y in range(3)
]

#%%
# Usando uma compreensão de lista aninhada. 
lista = [
    [(x, letra) for letra in 'Leonardo']
    for x in range(3)
]

p(lista)

lista = [[x * y for y in range(1, 4)] for x in range(1, 4)]

p(lista)
        