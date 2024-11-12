#%%
# # # Módulos padrão do Python (import, from, as e *)
# https://docs.python.org/3/py-modindex.html
# inteiro - import nome_modulo
# Vantagens: você tem o namespace do módulo
# Desvantagens: nomes grandes

import importlib.readers
import sys

platform = 'A MINHA'
print(sys.platform)
print(platform)

#%%
# partes - from nome_modulo import objeto1, objeto2
# Vantagens: nomes pequenos
# Desvantagens: Sem o namespace do módulo

from sys import platform

print(platform)

#%%
# alias 1 - import nome_modulo as apelido

import sys as s

sys = 'alguma coisa'
print(s.platform)
print(sys)

#%%
# alias 2 - from nome_modulo import objeto as apelido

from sys import platform as pf, exit as ex

print(pf)

# Vantagens: você pode reservar nomes para seu código
# Desvantagens: pode ficar fora do padrão da linguagem

# má prática - from nome_modulo import *
# Vantagens: importa tudo de um módulo
# Desvantagens: importa tudo de um módulo

#%%
# Modularização - Entendendo os seus próprios módulos Python
# O primeiro módulo executado chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está e as pastas
# abaixo dele.
# Ele não reconhece pastas e módulos acima do __main__ por
# padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos de sys.path
try:
    import sys
    sys.path.append('/home')
except ModuleNotFoundError:
    ...
import modulo_import

print('Este módulo se chama', __name__)
print(sys.path, sep='\n')

#%%
# Usando variável e função que estão em outro módulo

import modulo_import as m

print(m.variavel_modulo)
print(m.soma(2, 3))

#%%
# Importando apenas a variável

from modulo_import import variavel_modulo

print(variavel_modulo)

#%%
# Singleton

'''
O singleton é um padrão de projeto de software que garante que uma classe tenha apenas uma 
única instância  em todo o ciclo de vida da aplicação e fornece um ponto global de acesso a essa instância.
Reduz o uso desnecessário de memória ao garantir uma única instância
'''

import modulo_import

for i in range(10):
    print(i)
    import modulo_import # não mostra nada porque já foi carregado anteriormente

print('FIM')

#%%
# Recarregar módulo usando importlib

import importlib
import modulo_import

for i in range(10):
    importlib.reload(modulo_import)
    print(i)





