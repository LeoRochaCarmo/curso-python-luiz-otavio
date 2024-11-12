#%%
# Pacotes
'''
Um pacote é uma coleção de módulos organizados em uma estrutura de diretórios. 
Serve para organizar módulos relacionados em um único namespace.
'''
from sys import path

# Formas de importar
import aula_pacotes
from aula_pacotes import modulo
from aula_pacotes.modulo import soma_do_modulo
from aula_pacotes.modulo import *
import aula_pacotes.modulo # recomendável

print(*path, sep='\n')
print(__name__)

print(aula_pacotes.modulo.soma_do_modulo(1, 2))
print(modulo.soma_do_modulo(1, 2))
print(soma_do_modulo(1, 2)) # código mais limpo
print(variavel)

#%%
# Ponto de vista do __main__

from aula_pacotes.modulo import soma_do_modulo, qualquer_coisa

qualquer_coisa()

#%%
# __init__.py
'''
O arquivo __init__.py é um arquivo especial em Python utilizado para indicar que o diretório 
em que ele se encontra deve ser tratado como um pacote Python. Ele pode ser vazio ou conter código 
de inicialização para o pacote. A principal função de __init__.py é sinalizar ao Python que o diretório 
é um pacote e que pode ser importado, seja como um pacote simples ou com funcionalidades específicas.
'''

import aula_pacotes

#função soma_do_modulo está no __init__.py
print(aula_pacotes.soma_do_modulo(2, 2))
aula_pacotes.qualquer_coisa()