#%%
# Introdução à função lambda (função anônima de uma linha)
# A função lambda é uma função como qualquer
# outra em Python. Porém, são funções anônimas
# que contém apenas uma linha. Ou seja, tudo
# deve ser contido dentro de uma única
# expressão.

lista = [
    {'nome': 'Luiz', 'sobrenome': 'miranda'},
    {'nome': 'Maria', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniel', 'sobrenome': 'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'},
]

#%%
 # definindo uma função
def ordena(item):
    return item['nome']

#%%
#lambda -> expressão em uma linha só
#sorted() -> cria uma nova lista através de uma cópia rasa

def exibir(lista):
    for item in lista:
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome']) 
l2 = sorted(lista, key=lambda item: item['sobrenome']) 

exibir(l1)
exibir(l2)

#%%
# .sort() -> altera a lista original
lista.sort(key=lambda item: item['nome'])

for item in lista:
    print(item)

#%$

