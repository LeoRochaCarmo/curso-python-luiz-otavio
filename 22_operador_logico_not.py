# Operador lógico "not"
# Usado para inverter expressões
# not True = False
# not False = True

senha = input('Senha: ')

if not senha:
    print('Você não digitou nada')
elif senha != '123456':
    print('Senha incorreta')
else:
    print('Senha Correta')