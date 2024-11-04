#%%
# Definindo funções para comparar com lambda

def executa(funcao, *args):
    return funcao(*args)

def soma(x, y):
    return x + y

def criar_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica


#%%
#formas diferentes da funcão soma

print(
    executa(
        lambda x, y: x + y, # função soma em uma linha
        2, 3
    ),
    executa(soma, 2, 3),
    soma(2, 3)
)

#%%
# função multiplicador com lambda

duplica = criar_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m,
    2
)

print(duplica(2))

#%%

print(
    executa(
        lambda *args: sum(args),
        1,2,3,4,5
    )
)