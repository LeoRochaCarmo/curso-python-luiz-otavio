

"""
Faça um lista de compras.
O usuário dever ter a possibilidadede inserir,
apagar e listar valores da sua lista.
Não permita que o programa quebre com  erros de
índices inexistentes na lista.
"""
import os

lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar [s]air:')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        os.system('cls')
        indice_str = input('Escolha o índice para apagar: ')

        try: 
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Digite um número inteiro')
        except IndexError:
            print('Índice não existe na lista')
         
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar.')
        
        for i, valor in enumerate(lista):
            print(i, valor)

    elif opcao == 's':
       os.system('cls')
       break
    

    else:
        os.system('cls')
        print('Tente digitar uma das opções disponíveis.')


