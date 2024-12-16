# requests para requisições HTTP

# + Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4

import requests
import re
from bs4 import BeautifulSoup

# http:// -> 80
# https:// -> 443

url = 'http://127.0.0.1:3333/'
response = requests.get(url)
# Detecta e define o encoding correto
bytes_html = response.content
parsed_html = BeautifulSoup(bytes_html, 'html.parser')

# if parsed_html.title is not None:
    # print(parsed_html.title.text)

top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
# print(top_jobs_heading.text)

if top_jobs_heading is not None:
    article = top_jobs_heading.parent

    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text))


