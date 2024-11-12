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

