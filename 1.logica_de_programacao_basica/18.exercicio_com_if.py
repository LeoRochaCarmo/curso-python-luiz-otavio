primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

# if primeiro_valor > segundo_valor:
#     print('{} é maior do que o {}'.format(primeiro_valor,segundo_valor ))
# else:
#     print('{} é maior do que o {}'.format(segundo_valor, primeiro_valor))

if primeiro_valor > segundo_valor:
    print(f'{primeiro_valor=} é maior do que o {segundo_valor=}')
elif primeiro_valor == segundo_valor:
    print(f'{primeiro_valor=} é igual ao {segundo_valor=}')
else:
    print(f'{segundo_valor=} é maior do que o {primeiro_valor=}')
