# Criando datas com módulo datetime
# datetime(ano, mês, dia)

# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

#%%
# INTRO DATETIME
from datetime import datetime, timedelta
from pytz import timezone
from dateutil.relativedelta import relativedelta

# ano, mês, dia, horas, minutos, segundos
data = datetime(2024, 12, 2, 23, 1, 21)
print(data)

#%%
#convertendo string para formato datetime
data_string = '02-12-2024'
data_strptime = datetime.strptime(data_string, '%d-%m-%Y')
print(data_strptime)

#%%
# hora atual + time zones (pytz)
print(datetime.now(timezone('America/Sao_Paulo')))
print(datetime.now(timezone('Asia/Tokyo')))
data_tz = datetime(
    2024, 12, 2, 23, 1, 21, 
    tzinfo=timezone('Asia/Tokyo')
)
print(data_tz)

#%%
# Timestamp
# Contagem de segundos desde 1 de janeiro de 1970 até agora
timestamp = data.timestamp()
print(timestamp)

#%%
# Criando data usando timestamp
print(datetime.fromtimestamp(timestamp))

#%%
# datetime.timedelta e dateutil.relativetimedelta (calculando datas)
# Docs:
# https://dateutil.readthedocs.io/en/stable/relativedelta.html
# https://docs.python.org/3/library/datetime.html#timedelta-objects

fmt = '%d/%m/%Y %H:%M:%S'
data_inicio = datetime.strptime('20/04/1987 09:30:30', fmt)
data_fim = datetime.strptime('12/12/2022 08:20:20', fmt)

# comparando datas
print(data_fim > data_inicio)

# diferença entre duas datas (timedelta)
delta = data_fim - data_inicio
print(delta.days)
print(delta.total_seconds())

#%%
# Criando um timedelta
delta = timedelta(days=10, hours=2)
print(data_fim + delta)

#%%
# relativedelta
print(data_fim)
print(data_fim + relativedelta(seconds=60, minute=10))

#%%
# obtendo diferença entre duas dats
delta_relative = relativedelta(data_fim, data_inicio)
print(delta_relative)
print(delta_relative.days, delta_relative.years)

#%%
# Formatando datas do datetime
# datetime.strftime('DATA', 'FORMATO')
# https://docs.python.org/3/library/datetime.html

data_agora = datetime.now()
data_strftime = datetime.strftime(data_agora, '%d-%m-%Y')
print(data_strftime)
print(data_agora.strftime('%d-%m-%Y'))


