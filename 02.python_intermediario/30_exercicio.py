"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
#%%
# Forma tradicional

list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = [1, 2, 3, 4]
list_c = [7, 30, 24, 12, 32]

sum_list = []

for i in range(len(list_b)):
    sum_list.append(list_a[i] + list_b[i])

print(sum_list)


#%%
# Criando uma função
def lists_sum(list_a, list_b):
    max_range = min(len(list_a), len(list_b))
    return [
        list_a[i] + list_b[i] 
        for i in range(max_range)
    ]

print(lists_sum(list_a, list_b))

#%%
# Forma mais simples

sum_list = [x + y for x, y in zip(list_a, list_b)]

print(sum_list)

#%% 

# Função que soma diversas listas

def sum_lists(*args):
    return [sum(args) for args in zip(*args)]

print(sum_lists(list_a, list_b, list_c))