#%% 

"""
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""

def imprimir(a, b, c): # parâmetros
    print('exibindo função')

imprimir(1, 2, 3) # argumentos
imprimir(4, 5, 6)

#%%
def saudacao(nome):
    print(f'Olá {nome}!')

saudacao('Leo')
saudacao('Luana')
