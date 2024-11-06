#%%
# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b)

#%%
# Desempacotamento em dicionários
pessoa = {
    'nome': 'Leonardo',
    'sobrenome': 'Rocha'
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.6
}

a, b = pessoa # desempacota as chaves
print(a, b)

c, d = pessoa.values() # desempacota os valores
print(c, d)

e, f = pessoa.items() # desempacota pares de chave e valor
print(e, f)

(e1, e2), f = pessoa.items() # desempacotamento interno
print(e1, e2, f)

#%%
# Desempacotamento com for
for chave, valor in pessoa.items():
    print(chave, valor)

#%%
# ** -> para desempacotar o conteúdo de um dicionário
pessoa_completa = {
    **pessoa,
    **dados_pessoa,
    'chave': 'valor'
    }
print(pessoa_completa) 

#%%
# args (já vimos) e kwargs
# kwargs - keyword arguments (argumentos nomeados)

def mostra_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)

mostra_argumentos_nomeados(2, 3, 'teste', nome= 'Joana', qlq= 123)

#%%
# desempacotar um dicionário com ** em uma função
mostra_argumentos_nomeados( **pessoa_completa)




