#%%
# Revisando filtro de dados com list comprehension

def print_iter(iterator):
    print(*iterator, sep='\n')
    print()

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00, 'categoria': 'Esportes'},
    {'nome': 'Produto 1', 'preco': 22.32, 'categoria': 'Esportes'},
    {'nome': 'Produto 3', 'preco': 10.11, 'categoria': 'Beleza'},
    {'nome': 'Produto 2', 'preco': 105.87, 'categoria': 'Higiene'},
    {'nome': 'Produto 4', 'preco': 69.90, 'categoria': 'Higiene'},
]

novos_produtos = [
    p for p in produtos
    if p['preco'] > 20
]

print_iter(novos_produtos)

#%%
# filtro de dados usando filter(func, iterable)

novos_produtos = list(filter(
    lambda p: p['preco'] > 20,
    produtos
))

print_iter(novos_produtos)

#%%
# Redução de um iterável em um valor (Forma Tradicional)

from functools import reduce

total = 0

for p in produtos:
    total += p['preco']

print(total)

#%% 
# Redução com list compreehension

total_precos = sum([p['preco'] for p in produtos])

print(total_precos)

#%% Redução com função reduce

total_precos = reduce(
    lambda acumulador, produto: acumulador + produto['preco'],
    produtos,
    0
)

print(total_precos)
