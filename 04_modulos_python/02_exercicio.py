# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2022 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
#%%
# MINHA SOLUÇÃO
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

data_inicio = datetime.strptime('20/12/2022', '%d/%m/%Y')

data_final = datetime.strptime(
    ((data_inicio + relativedelta(years=5)).strftime('%d/%m/%Y')),
     '%d/%m/%Y'
)

diferenca = relativedelta(data_final, data_inicio)

qtde_parcelas = diferenca.years * 12 + diferenca.months

valor_emprestimo = 1000000

for parcela in range(1, qtde_parcelas + 1):
    print(f'\nParcela {parcela}:')
    print(f'Data da parcela: {data_inicio.strftime('%d/%m/%Y')}')
    print(f'Valor da parcela: R${(round(valor_emprestimo / qtde_parcelas, 2))}')
    data_inicio += relativedelta(months=1)

#%%
# SOLUÇÃO DO PROFESSOR + MINHAS MELHORIAS
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

data_inicio = datetime(2022, 12, 20)
data_final = data_inicio + relativedelta(years=5)
valor_emprestimo = 1000000

data_parcela = data_inicio
datas_parcelas = []
while data_parcela < data_final:
    datas_parcelas.append(data_parcela)
    data_parcela += relativedelta(months=1)

valor_pago = 0
qtde_parcelas = len(datas_parcelas)
for parcela, data in enumerate(datas_parcelas, start=1): # eu escolhi usar enumerate
    print(f'\nParcela {parcela}:')
    print(f'Data de Pagamento: {data.strftime('%d/%m/%Y')}')
    print(f'Valor da Parcela: R$ {valor_emprestimo / qtde_parcelas:,.2f}')
    valor_pago += valor_emprestimo / qtde_parcelas
    print(f'Valor pago até o momento: R$ {valor_pago:,.2f}') # adicionei como extra