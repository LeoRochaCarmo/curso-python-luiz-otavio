"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# entrada = input('Digite um número: ')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto: 'par'
        
#     print(f'O número {entrada_int} é {par_impar_texto}')

# else:
#     print('Você não digitou um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# entrada = input('Digite a hora (Ex: 09:23): ')
# entrada_horas = entrada[:2]

# if entrada_horas.isdigit():
#     entrada_int = int(entrada_horas)
#     bom_dia = entrada_int >= 0 and entrada_int <= 11 
#     boa_tarde = entrada_int >= 12 and entrada_int <= 17
#     boa_noite = entrada_int >= 18 and entrada_int <= 23

#     if bom_dia:
#         print(f'Bom dia! São {entrada}')
#     elif boa_tarde:
#         print(f'Boa tarde! São {entrada}')
#     else:
#         print(f'Boa noite! São {entrada}')
# else:
#     print('Você não digitou um horário válido.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome: ')
nome_curto = len(nome) <= 4
nome_normal = len(nome) >= 5 and len(nome) <= 6
nome_grande = len(nome) > 6

if not nome:
    print('Nome inválido. Tente novamente.')
elif nome_curto:
    print('Seu nome é curto.')
elif nome_normal:
    print('Seu nome é normal.')
else:
    print('Seu nome é muito grande.')



