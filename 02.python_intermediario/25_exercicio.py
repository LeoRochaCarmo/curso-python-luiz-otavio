#%%
# copy, sorted, produtos.sort
# Exercícios

#%%
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

import copy
from dados import produtos

novos_produtos = [
    {**produto, 'preco': round(produto['preco'] * 1.1, 2)}
    for produto in produtos
]

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')

#%%
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(novos_produtos), 
    key= lambda item: item['nome'],
    reverse=True
)
print(*produtos_ordenados_por_nome, sep='\n')


#%%
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(novos_produtos),
    key= lambda item: item['preco']
)
print(*produtos_ordenados_por_preco, sep='\n')