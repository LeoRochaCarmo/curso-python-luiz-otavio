import sys

argumentos = sys.argv
qtde_argumentos = len(argumentos)

print(argumentos)
print(qtde_argumentos)

if qtde_argumentos <= 1:
    print('Você não passou argumentos.')
else:
    try:
        print(f'Você passou os argumentos {argumentos[1:]}')
        print(f'Faça alguma coisa com {argumentos[1]}')
        print(f'Faça outra coisa com {argumentos[2]}')
    except IndexError:
        print('Faltam argumentos.')


