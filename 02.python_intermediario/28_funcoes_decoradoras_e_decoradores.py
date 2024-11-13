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
