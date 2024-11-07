# Dicitionary Comprehension e Set Comprehension

#%%
# Dicitionary Comprehension

produto = {
    'nome': 'caneta azul',
    'preco': 2.5,
    'categoria': 'escritório',
}

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor # IMPORTANTE
    for chave, valor 
    in produto.items()
    if chave != 'categoria'
}

print(dc)

lista = [
    ('a', 'valor a'),
    ('b', 'valor b'),
    ('c', 'valor c'),
]

dc_lista = {
    chave: valor 
    for chave, valor in lista
}

print(dc_lista)

#%%
# Set Comprehension

s1 = {2 ** i for i in range(10)}

print(s1, type(s1))

#%%
# isinstace -> para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]

for item in lista:
    if isinstance(item, set):
        item.add(5)
        print(item, isinstance(item, set))

    if isinstance(item, str):
        print(item.upper())

    if isinstance(item, (int,float)):
        print(item, item * 2)

    if isinstance(item, (list, tuple)):
        soma = 0
        for i in item:
            soma += i
        print(soma, '-> soma dos itens na lista ou tupla ')
