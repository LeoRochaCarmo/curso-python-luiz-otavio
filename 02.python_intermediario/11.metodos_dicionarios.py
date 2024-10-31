#%%

# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

pessoa = {
    'nome': 'Leonardo',
    'sobrenome': 'Rocha',
    'idade': 900,
}

#%%
# Saber quantas chaves tem
pessoa.__len__()
len(pessoa)

#%%
# Saber os nomes das chaves
print(pessoa.keys())
# Converter  dict_keys para uma lista
list(pessoa.keys())

#%%
# Saber os valores das chaves
print(pessoa.values())
# Converter dict_values para uma lista
list(pessoa.values())
# Iterar usando os valores
for valor in pessoa.values():
    print(valor)

#%%
# Saber as chaves e os valores
pessoa.items()
# Converter dict_items para uma lista
list(pessoa.items())
# Iterar usando as chaves e os valores
for chave, valor in pessoa.items():
    print(chave, valor)

#%%
# Adicionar valor se a chave não existe
pessoa.setdefault('cor', 'branco')

#%%
# Shallow Copy (Cópia Rasa)

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
}

# d2 = d1 # d2 aponta para d1
# d2['c1'] = 1000 #d2 muda o valor que está em d1
# print(d1)

d2 = d1.copy() #retorna uma cópia rasa

d2['c1'] = 1000
d2['l1'][1] = 9999999 # Muda o valor dos 2 dicionários
print(d1)
print(d2)

#%%
# Deep Copy (Cópia Profunda)
import copy

d3 = copy.deepcopy(d1) # cópia profunda
d3['l1'][1] = 1
print(d1)
print(d3)

#%%
# Obter o valor na chave
print(pessoa.get('nome'))
# Retorna None se chave não existe
print(pessoa.get('nacionalidade'))

#%%
# Apagar um item
nome = pessoa.pop('cor')
print(nome)
print(pessoa)

#%%
# Apagar o valor da última chave
ultima_chave = pessoa.popitem()
print(ultima_chave)
print(pessoa)

#%%
# Atualizar o dicionário
pessoa.update({
    'nome': 'Leo',
    'idade': 900,

})

# Outra forma de escrever
pessoa.update(nome='Leonardo', idade=300)

# Outra forma de atualizar -> usando iteráveis
tupla = ('nome', 'Leo'), ('idade', 400)
pessoa.update(tupla)

print(pessoa)

# %%
