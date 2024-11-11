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
        n += 1

        if n >= maximum:
            return
        
gen = generator_2(n=5, maximum=8)

for n in gen:
    print(n)

#%% 
# Yield From

def gen1():
    print('COMEÇOU G1')
    yield 1
    yield 2
    yield 3
    print('ACABOU G1')

def gen3():
    print('COMEÇOU G3')
    yield 10
    yield 20
    yield 30
    print('ACABOU G3')

def gen2(gen=None):
    print('COMEÇOU G2')
    if gen is not None:
        yield from gen()
    yield 4
    yield 5
    yield 6
    print('ACABOU G2')

g1 = gen2(gen1)
g2 = gen2(gen3)
g3 = gen2()

for numero in g1:
    print(numero)
print()

for numero in g2:
    print(numero)
print()

for numero in g3:
    print(numero)
print()