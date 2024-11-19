#%%
# SALVANDO DADOS EM JSON
import json

pessoa = {
    'nome': 'Luiz Otávio 2',
    'sobrenome': 'Miranda',
    'enderecos': [
        {'rua': 'R1', 'numero': 32},
        {'rua': 'R2', 'numero': 55},
    ],
    'altura': 1.8,
    'numeros_preferidos': (2, 4, 6, 8, 10),
    'dev': True,
    'nada': None,
}

with open('.\\dados\\aula_sobre_json.json', 'w',encoding='utf-8') as arquivo_json:
    json.dump( # serializar objetos Python e escrevê-los em um arquivo no formato JSON.
        pessoa,
        arquivo_json,
        ensure_ascii= False,
        indent= True
    ) 

#%%
# ABRIR ARQUIVO JSON

with open('.\\dados\\aula_sobre_json.json', 'r', encoding='utf-8') as leitura_json:
    pessoa = json.load(leitura_json) # vira um dicionário
    print(pessoa, sep='\n')