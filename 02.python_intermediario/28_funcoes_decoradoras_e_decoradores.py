# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

#%%
# Função decoradora

def create_function(func):
    def intern(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print('Agora você foi decorada')
        return result
    return intern

def invert_string(string):
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Deve ser uma string')
    
invert_string_check_param = create_function(invert_string)
inverted = invert_string_check_param('123')
print(inverted)

#%%
# Decoradores @ (Sugar syntax)
'''
Um decorador é uma função que recebe uma função como argumento e retorna uma nova função que geralmente estende 
ou modifica o comportamento da função original. A sintaxe mais comum de decoradores em Python usa o símbolo @.
'''

def create_function(func):
    def intern(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            is_string(arg)
        result = func(*args, **kwargs)
        print('Agora você foi decorada')
        return result
    return intern

@create_function
def invert_string(string):
    print(f'{invert_string.__name__}')
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Deve ser uma string')
    
inverted = invert_string('123')
print(inverted)

#%%
# Exemplo CHATGPT

def meu_decorador(func):
    def wrapper(*args, **kwargs):
        print("Antes da execução da função")
        resultado = func(*args, **kwargs)
        print("Depois da execução da função")
        return resultado
    return wrapper

@meu_decorador
def minha_funcao():
    print("Função original em execução")

minha_funcao()

#%%
# Exemplo: Em quanto tempo a função executou

import time

def tictoc(func):
    def wrapper():
        t1 = time.time()
        func()
        t2 = time.time() - t1
        result = f'{func.__name__} ran in ' \
                 f'{t2} seconds'
        return result
    return wrapper

@tictoc
def do_this():
    time.sleep(1.5)

@tictoc
def do_that():
    time.sleep(.5)

print(do_this())
print(do_that())

#%%
# Decoradores com parâmetros

def decorators_factory(a=None, b=None, c=None):

    def func_factory(func):
        print('Decorator 1')

        def wrapper(*args, **kargs):
            print('Decorator parameters:', a, b, c)
            print('Wrapper')
            result = func(*args, **kargs)
            return result
        return wrapper
    return func_factory


@decorators_factory(1, 2, 3)
def sum(x,y):
    return x + y

multiplication = decorators_factory()(lambda x, y: x * y)

ten_plus_five = sum(10, 5)
ten_times_five = multiplication(10, 5)

print(ten_plus_five)
print(ten_times_five)

#%%
# Ordem dos decoradores
def decorators_param(name):

    def decorator(func):
        print('Decorator:', name)

        def new_func(*args, **kargs):
            result = func(*args, **kargs)
            final = f'{result} {name}'
            return final
        return new_func
    return decorator


@decorators_param(name='3')
@decorators_param(name='2')
@decorators_param(name='1')
def sum(x,y):
    return x + y

ten_plus_five = sum(10, 5)

print(ten_plus_five)
