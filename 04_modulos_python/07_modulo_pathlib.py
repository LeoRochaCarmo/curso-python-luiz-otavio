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

# deletando arquivo
new_file.unlink()


