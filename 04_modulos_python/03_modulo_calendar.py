# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo

#%%
import calendar

# calendário de 2024
print(calendar.calendar(2024))

#%%
# calendário de um mês específico
print(calendar.month(2024, 12 ))

#%%
# obter o último dia do mês
numero_primeiro_dia, ultimo_dia = calendar.monthrange(2024, 12)

#%%
# obter os nomes dos dias e a ordem
print(list(enumerate(calendar.day_name)))

#%%
# checando qual dia da semana que começa o mês
print(calendar.day_name[numero_primeiro_dia])

#%%
# obter último dia do mês
print(calendar.weekday(2024, 12, ultimo_dia))
print(calendar.day_name[calendar.weekday(2024, 12, ultimo_dia)])

#%%
# criar um calendário
print(calendar.monthcalendar(2024, 12))

#%%
# BRINCADEIRA QUE FIZ
mes = calendar.monthcalendar(2024, 12)

print('DEZEMBRO/24')
for semana in mes:
    for dia, numero in enumerate(semana):
        if numero != 0:
            print(numero, calendar.day_name[dia])

#%%
# locale para internacionalização (tradução)
# https://docs.python.org/3/library/locale.html
# https://learn.microsoft.com/fr-fr/powershell/module/international/get-winsystemlocale?view=windowsserver2022-ps&viewFallbackFrom=win10-ps

import locale

# trocando os nomes para a localização do sistema
locale.setlocale(locale.LC_ALL, '')
print(calendar.calendar(2024))

# obter a localização do sistema
print(locale.getlocale())