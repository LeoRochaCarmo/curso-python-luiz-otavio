# __init__.py
'''
O arquivo __init__.py é um arquivo especial em Python utilizado para indicar que o diretório 
em que ele se encontra deve ser tratado como um pacote Python. Ele pode ser vazio ou conter código 
de inicialização para o pacote. A principal função de __init__.py é sinalizar ao Python que o diretório 
é um pacote e que pode ser importado, seja como um pacote simples ou com funcionalidades específicas.
'''

print(
    'Você importou', __name__
)

def dobra(x):
    return x * 2

from .modulo import *
from .modulo_2 import *