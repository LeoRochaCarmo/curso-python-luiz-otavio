# O módulo os para interação com o sistema
# Doc: https://docs.python.org/3/library/os.html
# O módulo `os` fornece funções para interagir com o sistema operacional.
# Por exemplo, o módulo os.path contém funções para trabalhar com caminhos de
# arquivos e a função os.listdir() pode ser usada para listar os arquivos em um
# diretório. O método os.system() permite executar comandos do sistema
# operacional a partir do seu código Python.
# Windows 11 (PowerShell), Linux, Mac = clear
# Windows (antigo, cmd) = cls
# limpando o terminal
# os.system -> executar comandos do sistema operacional diretamente a partir de um script Python.

#%%
# NÃO FUNCIONA NO JUPYTER
import os

os.system('cls')
os.system('echo "Hello World"')
print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)
print('a' * 80)

#%%# 
# os.path trabalha com caminhos em Windows, Linux e Mac
# Doc: https://docs.python.org/3/library/os.path.html#module-os.path
# os.path é um módulo que fornece funções para trabalhar com caminhos de
# arquivos em Windows, Mac ou Linux sem precisar se preocupar com as diferenças
# entre esses sistemas.
# Exemplos do os.path:
# os.path.join: junta strings em um único caminho. Desse modo,
# os.path.join('pasta1', 'pasta2', 'arquivo.txt') retornaria
# 'pasta1/pasta2/arquivo.txt' no Linux ou Mac, e
# 'pasta1\pasta2\arquivo.txt' no Windows.
# os.path.split: divide um caminho uma tupla (diretório, arquivo).
# Por exemplo, os.path.split('/home/user/arquivo.txt')
# retornaria ('/home/user', 'arquivo.txt').
# os.path.exists: verifica se um caminho especificado existe.
# os.path só trabalha com caminhos de arquivos e não faz nenhuma
# operação de entrada/saída (I/O) com arquivos em si.

# Trabalhando com caminho de arquivos
import os

caminho = os.path.join('/home/users', 'Desktop', 'curso', 'arquivo.txt')
print(caminho)

# Dividir o arquivo do diretório
diretorio, arquivo = os.path.split(caminho)

# Dividir o caminho da extensão
caminho_arquivo, extensao_arquivo = os.path.splitext(caminho)

# Dividir o arquivo da extensão
nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)

# Retorna se caminho existe
print(os.path.exists(caminho))

# Retorna o caminho absoluto
print(os.path.abspath('.'))

# Retorna o último componente do caminho
print(os.path.basename(caminho))

# Retorna o diretório sem o nome do arquivo
print(os.path.dirname(caminho))

#%%
# os.listdir para navegar em caminhos

caminho = os.path.join('/home', 'leonardorocha', 'Imagens')
print(caminho)

# listando itens que estão dentro desse diretório
for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta.upper())

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for imagem in os.listdir(caminho_completo_pasta):
        print('     ', os.path.join(caminho_completo_pasta, imagem))

#%%
# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).

import os
from itertools import count

caminho2 = '/home/leonardorocha/anaconda3/plugins'
counter = count()

for root, dirs, files in os.walk(caminho2):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir', dir_)

    for file in files:
        caminho_completo = os.path.join(root, file)
        print('  ', the_counter, 'File', caminho_completo)

        # os.unlink() -> apaga os arquivos. CUIDADO!!!
# %%
