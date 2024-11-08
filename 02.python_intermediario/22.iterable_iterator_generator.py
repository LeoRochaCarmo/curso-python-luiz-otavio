#%%
# Iterables e Iterators em Python
iterable = ['Eu', 'Tenho', '__iter__']
iterator = iter(iterable) # tem __iter__ e __next__

print(next(iterator))
print(next(iterator))
print(next(iterator))

# Se chamarmos next() novamente, receberemos a exceção StopIteration
# print(next(iterator))  # Lança StopIteration

#%%
# Generator Expression

''''
Uma generator expression em Python é uma construção semelhante às list comprehensions, 
mas em vez de criar uma lista, ela retorna um objeto do tipo generator, que gera os elementos sob demanda. 
Isso significa que os valores são produzidos de forma "preguiçosa" (ou seja, apenas quando necessários), 
economizando memória, especialmente ao lidar com grandes quantidades de dados.

Sintaxe
A sintaxe de uma generator expression é semelhante à de uma list comprehension, mas usa parênteses em vez de colchetes:
'''

import sys

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))

print(sys.getsizeof(lista), type(lista))
print(sys.getsizeof(generator), type(generator), end= '\n\n')

print('Valor do generator:')
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# Generator Expression X Iterator
'''
Em resumo, uma generator expression é uma maneira de criar rapidamente um gerador (um tipo de iterator). 
Ela é usada para criar iteradores de forma mais conveniente e em uma única linha de código. 
Já um iterator é uma interface mais ampla, que pode ser implementada por vários tipos de objetos para permitir a iteração.
'''
#%%
# Introdução às Generator Functions

def generator(n=0):
    yield 1 # Pausa 
    print('Continuando...')
    yield 2 # Pausa 
    print('Mais uma...')
    yield 3 # Pausa 
    print('Vou terminar...')
    return 'ACABOU' 

gen = generator(n=0)

for n in gen:
    print(n)

#%% 

def generator_2(n=0, maximum=10):
    while True:
        yield n

        if n > maximum:
            return
        
        n += 1

gen = generator_2()

for n in gen:
    print(n)


