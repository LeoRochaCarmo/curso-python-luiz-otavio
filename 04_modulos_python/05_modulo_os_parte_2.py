#%%
# os.path.getsize e os.stat para dados dos arquivos (tamanho em bytes)
import os
import math
from itertools import count


def formata_tamanho(tamanho_em_bytes: int, base: int = 1000) -> str:
    """Formata um tamanho, de bytes para o tamanho apropriado"""

    # Original:
    # https://stackoverflow.com/questions/5194057/better-way-to-convert-file-sizes-in-python

    # Se o tamanho for menor ou igual a 0, 0B.
    if tamanho_em_bytes <= 0:
        return "0B"

    # Tupla com os tamanhos
    #                      0    1     2     3     4     5
    abreviacao_tamanhos = "B", "KB", "MB", "GB", "TB", "PB"
    # Logaritmo -> https://brasilescola.uol.com.br/matematica/logaritmo.htm
    # math.log vai retornar o logaritmo do tamanho_em_bytes
    # com a base (1000 por padrão), isso deve bater
    # com o nosso índice na abreviação dos tamanhos
    indice_abreviacao_tamanhos = int(math.log(tamanho_em_bytes, base))
    # Por quanto nosso tamanho deve ser dividido para
    # gerar o tamanho correto.
    potencia = base ** indice_abreviacao_tamanhos
    # Nosso tamanho final
    tamanho_final = tamanho_em_bytes / potencia
    # A abreviação que queremos
    abreviacao_tamanho = abreviacao_tamanhos[indice_abreviacao_tamanhos]
    return f'{tamanho_final:.2f} {abreviacao_tamanho}'


caminho = '/run/media/leonardorocha/Windows/Users/leona_xuct80p/Pictures'
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print('  ', the_counter, 'Dir', dir_)

    for file in files:
        caminho_completo = os.path.join(root, file)
        tamanho_arquivo_formatado = formata_tamanho(os.path.getsize(caminho_completo))
        print('  ', the_counter, 'File', file, tamanho_arquivo_formatado)

#%%
# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy

import os

# Retorna a home do sistema
home = os.path.expanduser('~')
print(home)

#%%
# Criando uma nova pasta e copiando arquivos e subpastas de outra pasta
import shutil

original_folder = 'C:\\Users\\leona\\Imagens\\exemplo'
new_folder = 'C:\\Users\\leona\\Imagens\\nova_pasta'

# cria uma nova pasta + checar se já existe
os.makedirs(new_folder, exist_ok=True)

for root, dirs, files in os.walk(original_folder):

    for dir in dirs:
        new_dir_path = os.path.join(new_folder, dir)
        # criando novas 
        os.makedirs(new_dir_path, exist_ok=True)
        
    for file in files:
        file_path = os.path.join(root, file)
        # usando .replace para criar o caminho da nova pasta
        new_file_path = os.path.join(root.replace(original_folder, new_folder), file)
        if not os.path.exists(new_file_path):
            shutil.copy(file_path, new_file_path)
            print('New file copied.')
        else:
            print('Path and file already existed.')

#%%
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename
original_folder = 'C:\\Users\\leona\\Imagens\\exemplo'
new_folder = 'C:\\Users\\leona\\Imagens\\nova_pasta'

shutil.copytree(original_folder, new_folder, dirs_exist_ok=True)

# renomear a pasta
shutil.move(new_folder, new_folder + '_renomeado')

# shutil.rmtree(new_folder)