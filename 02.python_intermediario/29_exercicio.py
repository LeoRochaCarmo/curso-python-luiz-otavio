# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

#%%
list_1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
list_2 = ['BA', 'SP', 'MG', 'RJ']

def zipper(list_1, list_2):
    max_range = (min(len(list_1), len(list_2)))
    return [
        (list_1[i], list_2[i])
        for i in range(max_range)
    ]

print(*zipper(list_1, list_2), sep='\n')

#%%
# Solução mais simples (zip)
print(*list(zip(list_1, list_2)), sep='\n')

#%%
# Usando zip_longest -> usa a lista maior

from itertools import zip_longest
print(*list(zip_longest(list_1, list_2, fillvalue= 'SEM CIDADE')), sep='\n')