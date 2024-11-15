#%%
# Revisando mapeamento de dados com list comprehension

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

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

novos_produtos = [
    {**produto, 'preco': aumentar_porcentagem(produto['preco'], 1.1)} 
    for produto in produtos
]

print_iter(novos_produtos)

#%%
# partial -> permite que você pré-defina alguns dos argumentos que serão passados para a função, 
# criando uma função que já possui esses argumentos aplicados.

from functools import partial

aumentar_dez_porcento = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

novos_produtos = [
    {**produto, 'preco': aumentar_dez_porcento(produto['preco'])} 
    for produto in produtos
]

print_iter(novos_produtos)

#%%
# map -> para mapear dados

def mudar_preco_de_produtos(produto):
    return {
        **produto, 
        'preco': aumentar_dez_porcento(produto['preco'])
    }

novos_produtos = list(map(
    mudar_preco_de_produtos,
    produtos
))

print_iter(novos_produtos)
print(hasattr(novos_produtos, '__iter__')) # map é iterável
print(hasattr(novos_produtos, '__next__')) # map é iterator

#%%
# Checando se map é um generator
from types import GeneratorType

print(isinstance(novos_produtos, GeneratorType)) # False

#%%
# Usando lambda com função para o map
novos_produtos = list(map(
    lambda produto: {**produto, 'preco': aumentar_dez_porcento(produto['preco'])},
    produtos
))

print_iter(novos_produtos)