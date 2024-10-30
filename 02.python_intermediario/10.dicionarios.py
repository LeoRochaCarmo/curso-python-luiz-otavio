# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Luiz Otávio', sobrenome='Miranda')

#%%
#Forma menos usada
pessoa = dict(nome='Leonardo', sobrenome='Rocha') 

# Forma mais usada
pessoa = { 
    'nome': 'Leonardo',
    'sobrenome': 'Rocha',
    'idade': 31,
    'altura': 1.74,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'tel tel', 'número': 321},
    ],

}

#%%
# Visualizando o dado de alguma chave

print(pessoa['nome'])

#%%
#Visualizando as chaves e os valores do meu dicionário

for chave in pessoa:
    print(f'{chave}: {pessoa[chave]}')

#%%
# Manipulando chaves e valores em dicionários

pessoa = {}
pessoa['nome'] = 'Leonardo' #criando uma chave com valor

print(pessoa['nome'])

#%%
# Chaves dinâmicas

chave = 'nome'
pessoa[chave] = 'Leonardo' #alterando valor da chave
print(pessoa[chave])

#%%
# Apagando chave

pessoa['sobrenome'] = 'Rocha'
del pessoa['sobrenome'] # apaga a chave
print(pessoa)

#%% 
# Checar se chave existe ou não 

if pessoa.get('sobrenome') is None:
    print('Chave não existe')
else:
    print(pessoa['sobrenome'])



    