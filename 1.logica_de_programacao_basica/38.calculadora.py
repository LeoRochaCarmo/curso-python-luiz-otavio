""" Calculadora com while """

while True:

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    numeros_validos = None

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permetidos = '+-/*'

    if operador not in operadores_permetidos:
        print('Operador Inválido.')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    if operador == '*':
        print(num_1_float * num_2_float)
    elif operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    else:
        print(num_1_float / num_2_float)

    
    sair = input('Quer sair [s]im: ')
    sair = sair.lower().startswith('s')
    print(sair)

    if sair:
        break

