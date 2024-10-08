#%%
"""
Retorno de valores das funções (return)
"""
def soma(x, y):
    print(x + y) # apenas para visualizar a operação
    return(x + y) # valor da operação pode ser utilizado e acaba a execução da função
    print(1+1) # nenhum comando funciona depois de return

soma_1 = soma(2, 2)
soma_2 = soma(3, 3)
print(soma_1, soma_2)

#%%
# return + condicionais

def soma_if(x, y):
    if x > 10:
        return 10, 20
    return x + y

soma_3 = soma_if(13,2)
soma_4 = soma_if(3,3)
print(soma_3, soma_4)