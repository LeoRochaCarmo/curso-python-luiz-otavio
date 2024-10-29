# Exercícios com funções

#%% 
# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

multiplica(1,2,3)

#%%

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

# JEITO SIMPLES

def par_impar(numero):
    if numero % 2 == 0:
        return f'{numero} é par'
    return f'{numero} é par'

print(par_impar(2))
print(par_impar(13))
print(par_impar(28))

#%%

# JEITO DIFERENTE

def par_impar(*args):
    for numero in args:
        if numero % 2 == 0:
            print(f'{numero} é par')
        else: 
            print(f'{numero} é par') 

par_impar(1,2,3,4,5)

