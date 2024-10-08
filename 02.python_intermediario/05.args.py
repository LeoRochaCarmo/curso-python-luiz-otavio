#%% 

"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembrete de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

#%%
# Criando uma função para somar argumentos 
def soma(*args):
    print(args, type(args))
    soma = 0
    for i in args:
        soma += i
    return soma
    
soma(1,2,3,4,5,6)

#%%
# Função SUM() no python
print(sum((1,2,3,4,5,6)))

#%%
# Desempacotamento de tuplas
numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9
outra_soma = soma(*numeros) # * -> desempacota os itens na tupla
print(outra_soma)
print(sum(numeros))



