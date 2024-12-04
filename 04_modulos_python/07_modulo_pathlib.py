#%%
from pathlib import Path

# criando instância de Path para usar métodos e propriedades dela
project_path = Path()
# retorna o caminho absoluto do arquivo
print(project_path.absolute())

# retorna o caminho atual do arquivo
file_path = Path(__file__)
print(file_path)

# retorna o caminho da pasta acima
print(file_path.parent)

# retorna o caminho de 2 pastas acima
print(file_path.parent.parent)

# retorna o caminho da home 
print(Path.home())

#%%
# criando novo caminho e novo diretório
ideas_folder = file_path.parent.parent / 'ideas'

ideas_folder.mkdir(exist_ok=True)

#%%
# criando novo arquivo
new_file = ideas_folder / 'ideas.txt'
new_file.touch(exist_ok=True)

#%%
# escrevendo texto no arquivo
new_file.write_text('Escrevendo no arquivo')

# lendo o que foi escrito no arquivo
print(new_file.read_text())

#%%
# deletando arquivo
new_file.unlink()

#%%
# escrevendo múltiplas linhas no arquivo
new_file_path = ideas_folder / 'arquivo.txt'

# criando o arquivo já escrevendo nada nele
new_file_path.write_text('')

with new_file_path.open('a+') as arquivo: # outra forma de escrever
    arquivo.write('Uma linha\n')
    arquivo.write('Outra linha\n')

print(new_file_path.read_text())

# apagando arquivo 
new_file_path.unlink()

# deletando novo diretório
ideas_folder.rmdir()

#%%

# criando pasta
new_folder_path = Path(__file__).parent / 'new_folder'
new_folder_path.mkdir(exist_ok=True)

# criando sub pasta
new_sub_folder_path = new_folder_path / 'sub_folder'
new_sub_folder_path.mkdir(exist_ok=True)

# criando 10 arquivos dentro da sub pasta
for i in range(1, 11):
    file = new_sub_folder_path / f'file_{i}.txt'

    if file.exists():
        file.unlink()
    else:
        file.touch()

    # escrevendo dentro de cada um dos arquivos
    with file.open('a+') as text_file:
        text_file.write(f'FILE {i}\n')
        text_file.write(f'writing on file {i}')

#%%
# como apagar tudo recursivamente (HARD CODED)
# poderia ser feito com shutil.rmtree(new_folder_path)
def rmtree(root: Path, remove_root=True):

    for file in root.glob('*'):

        if file.is_dir():
            print('DIR:', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('FILE:', file)
            file.unlink()

        if remove_root:
            root.rmdir()

rmtree(new_folder_path)
