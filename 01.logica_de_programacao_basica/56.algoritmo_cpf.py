"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14

Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta

O segundo dígito do CPF é 0
"""   
#%%
#SOLUÇÃO 1 -> Usando .replace() para obter apenas os números

cpf_enviado = '746.824.890-70'
cpf_enviado = cpf_enviado.replace('.','').replace('-','')
print(cpf_enviado)

nove_digitos = cpf_enviado[:9]

contador_1 = 10
resultado_1 = 0

for digito in nove_digitos:
    resultado_1 += contador_1 * int(digito)
    contador_1 -= 1
    
digito_1 = (resultado_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_2 = 11
resultado_2 = 0

for digito in dez_digitos:
    resultado_2 += contador_2 * int(digito)
    contador_2 -= 1

digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_gerado == cpf_enviado:
    print(f'{cpf_enviado} é valido')
else:
    print('CPF inválido')
#%%
# SOLUÇÃO 2 -> Usando módulo re para obter apenas os números
# CPF: 746.824.890-70

import re
import sys

cpf_enviado = input('Digite o CPF: ')
cpf_enviado = ''.join(re.findall(r'\d+', cpf_enviado))

cpf_sequencial = cpf_enviado[0] * len(cpf_enviado) == cpf_enviado

if cpf_sequencial:
    print('Você enviou dados sequenciais')
    sys.exit()

nove_digitos = cpf_enviado[:9]
contador_1 = 10
resultado_1 = 0

for digito in nove_digitos:
    resultado_1 += contador_1 * int(digito)
    contador_1 -= 1
    
digito_1 = (resultado_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_2 = 11
resultado_2 = 0

for digito in dez_digitos:
    resultado_2 += contador_2 * int(digito)
    contador_2 -= 1

digito_2 = (resultado_2 * 10) % 11
digito_2 = digito_2 if digito_2 <= 9 else 0

cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_gerado == cpf_enviado:
    print(f'{cpf_enviado} é valido')
else:
    print('CPF inválido')

#%%

# Gerando 100 CPFs automaticamente
import random

for i in range(100):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0,9))

    contador_1 = 10
    resultado_1 = 0

    for digito in nove_digitos:
        resultado_1 += contador_1 * int(digito)
        contador_1 -= 1

    digito_1 = (resultado_1 * 10) % 11
    digito_1 = digito_1 if digito_1 <= 9 else 0

    dez_digitos = nove_digitos + str(digito_1)
    contador_2 = 11
    resultado_2 = 0

    for digito in dez_digitos:
        resultado_2 += contador_2 * int(digito)
        contador_2 -= 1

    digito_2 = (resultado_2 * 10) % 11
    digito_2 = digito_2 if digito_2 <= 9 else 0
    
    numero_formatado = "{:,}".format(int(nove_digitos)).replace(",", ".")
    
    cpf_gerado = f'{numero_formatado}-{digito_1}{digito_2}'
    print(cpf_gerado)
