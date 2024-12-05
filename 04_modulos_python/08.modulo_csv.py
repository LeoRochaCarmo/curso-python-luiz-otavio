#%%
# CSV (Comma Separated Values - Valores separados por vírgulas)
# É um formato de arquivo que armazena dados em forma de tabela, onde cada
# linha representa uma linha da tabela e as colunas são separadas por vírgulas.
# Ele é amplamente utilizado para transferir dados entre sistemas de diferentes
# plataformas, como por exemplo, para importar ou exportar dados para uma
# planilha (Google Sheets, Excel, LibreOffice Calc) ou para uma base de dados.
# Um arquivo CSV geralmente tem a extensão ".csv" e pode ser aberto em um
# editor de texto ou em uma planilha eletrônica.
# Um exemplo de um arquivo CSV pode ser:
# Nome,Idade,Endereço
# Luiz Otávio,32,"Av Brasil, 21, Centro"
# João da Silva,55,"Rua 22, 44, Nova Era"
# A primeira linha do arquivo define os nomes das colunas da, enquanto as
# linhas seguintes contêm os valores das linhas, separados por vírgulas.
# Regras simples do CSV
# 1 - Separe os valores das colunas com um delimitador único (,)
# 2 - Cada registro deve estar em uma linha
# 3 - Não deixar linhas ou espaços sobrando
# 4 - Use o caractere de escape (") quando o delimitador aparecer no valor.

#%%
from pathlib import Path
import csv

csv_path = Path(__file__).parent / '08_modulo_csv.csv'

with open(csv_path, 'r') as file:
    # ler um arquivo csv em formato de lista
    reader = csv.reader(file)

    for line in reader:
        print(line)

#%%
with open(csv_path, 'r') as file:
    # ler um arquivo csv em formato de dicionário
    reader = csv.DictReader(file)

    for line in reader:
        print(line)

#%%
# cria um arquivo CSV a partir de uma lista de dicionários
clients_csv_file = Path(__file__).parent / '08_clients.csv'

clients_list = [
    {'Nome': 'Luiz Otávio', 'Endereço': 'Av 1, 22'},
    {'Nome': 'João Silva', 'Endereço': 'R. 2, "1"'},
    {'Nome': 'Maria Sol', 'Endereço': 'Av B, 3A'},
]

with open(clients_csv_file, 'w') as file:
    columns = clients_list[0].keys()
    writer = csv.writer(file)
    writer.writerow(columns)

    for client in clients_list:
        writer.writerow(client.values())

#%%
# cria um arquivo CSV a partir de um dicionário
with open(clients_csv_file, 'w') as file:
    columns = clients_list[0].keys()
    writer = csv.DictWriter(
        file,
        fieldnames=columns
    )
    writer.writeheader()

    for client in clients_list:
        writer.writerow(client)

