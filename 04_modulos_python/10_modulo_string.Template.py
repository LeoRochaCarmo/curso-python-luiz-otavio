# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings

#%%
import locale
from datetime import datetime

locale.setlocale(locale.LC_ALL, '')

# função que converte um valor para a moeda local
def convert_to_brl(numero: float) -> str:
    brl = 'R$' + locale.currency(val=numero, symbol=False, grouping=True)
    return brl

date = datetime(2024, 12, 6)
data = dict(
    name='João',
    value=convert_to_brl(123456),
    date=date.strftime('%d/%m/%Y'),
    company='O.M.',
    telephone='+55 (11) 4343-4343'
)
# ver o dicionário de uma forma mais clara
import json
print(json.dumps(data, indent= 2, ensure_ascii=False))

#%%
# Substituindo variáveis em texto
from string import Template

text = '''
Prezado(a) $name,
Informamos que sua mensalidade será cobrada no valor de $value no dia $date. Caso deseje cancelar o serviço, entre em contato com a $company pelo telefone $telephone.
Atenciosamente,
$company, 
'''

template = Template(text)

# substitute: substitui mas gera erros se faltar chaves
print(template.substitute(data))
# safe_substitute: substitui sem gerar erros
print(template.safe_substitute(data))

#%%
# visualizando a alteração nas variáveis
from pathlib import Path

file_path = Path(__file__).parent / '10_mensagem.txt'

with open(file_path, 'r') as file:
    text = file.read()
    template = Template(text)
    print(template.substitute(data))

#%%
# como usar outro delimitador
from string import Template

# criando uma subclasse de template.
class MyTemplate(Template):
    delimiter = '%'

data2 = dict(
    name='Leonardo',
    age=31
)

text2 = 'Olá %name. Você tem %age anos'

template = MyTemplate(text2)

print(template.substitute(data2))