#%%

"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma (x, y, z):
    print(f'{x=} {y=} {z=}', '|' , 'x + y + z =', x + y + z)

soma(1, 2, 3) # argumentos não nomeados
soma(x=2, y=1, z=5) # argumentos nomeados
soma(1, y=2, z=4) # se nomeio um argumento, os próximos precisam ser nomeados também

#%%

"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

def soma(x, y, z=None): 
    if z is not None: # checa se z foi enviado (mesmo sendo 0)
        print(f'{x=} {y=} {z=}', '|', 'x + y + z =', x + y + z)
    else:
        print(f'{x=} {y=}', '|', 'x + y =', x + y)
        print('Você não passou o z')

soma(100, 200) # função sem o z
soma(100, 200, 0) # zero como z é considerado falsy
soma(100, 200, 2) # função com o z