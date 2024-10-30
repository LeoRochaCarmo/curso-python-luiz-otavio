# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro.

#%%

def multiplicar(multiplicador):
    def numero(numero):
        return numero * multiplicador
    return numero

duplicar = multiplicar(2)
triplicar = multiplicar(3)
quadruplicar = multiplicar(4)

for numero in [2, 4, 6, 8]:
    print(f'CONTAS COM O NÚMERO {numero}')
    print(f'{numero} X 2 é igual a:', duplicar(numero))
    print(f'{numero} X 3 é igual a:', triplicar(numero))
    print(f'{numero} X 4 é igual a:', quadruplicar(numero))