# O que é JSON - JavaScript Object Notation
# JSON - JavaScript Object Notation (extensão .json)
# É uma estrutura de dados que permite a serialização
# de objetos em texto simples para facilitar a transmissão de
# dados através da rede, APIs web ou outros meios de comunicação.
# O JSON suporta os seguintes tipos de dados:
# Números: podem ser inteiros ou com ponto flutuante, como 42 ou 3.14
# Strings: são cadeias de caracteres, como "Olá, mundo!" ou "12345"
#   As strings devem ser envolvidas por aspas duplas
# Booleanos: são os valores verdadeiro (true) ou falso (false)
# Arrays: são listas ordenadas de valores, como [1, 2, 3] ou
#   ["Oi", "Olá", "Bom dia"]
# Objetos: são conjuntos de pares chave/valor -> {"nome": "João", "idade": 30}
# null: é um valor especial que representa ausência de valor
#
# Ao converter de Python para JSON:
# Python        JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

#%%
# json.dumps e json.loads com strings + typing.TypedDict
import json
from pprint import pprint
from typing import TypedDict

# tipando um dicionário para visualizar as chaves
class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None

# docstring
string_json = '''
{
  "title": "O Senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord of the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
'''

# convertendo string no formato json para o formato python
movie: Movie = json.loads(string_json)

pprint(movie, sort_dicts=False)

# agora é possível ver as chaves quando abrir os colchetes
print('\n', movie['year'], '\n')

# convertendo uma string para json
print(json.dumps(movie, ensure_ascii=False, indent=2))

#%%
# json.dump e json.load com arquivos
import os

# cria o caminho absoluto do novo arquivo
file_name = '06_modulo_json.json'
absolute_file_path = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        file_name
    )
)

# dicionário para ser inserido em um arquivo json
string_json_dict = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel', 
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring', 
    'is_movie': True, 
    'imdb_rating': 8.8, 
    'year': 2001, 
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'], 
    'budget': None
}

# criando arquivo json
with open(absolute_file_path, 'w') as arquivo:
    json.dump(
        string_json_dict,
        arquivo, 
        indent=2, 
        ensure_ascii=False
    )

#%%
# lendo arquivo json
with open(absolute_file_path, 'r') as arquivo:
    movie_json = json.load(arquivo)

print(movie_json)
