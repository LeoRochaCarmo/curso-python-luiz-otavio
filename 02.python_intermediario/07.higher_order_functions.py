"""
Higher Order Functions
Funções que podem receber e/ou retornar outras funções

First-Class Functions
Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc...)
"""

#%%

def saudacao(msg):
    return msg

def executa(funcao, texto): # função que chama outra funcão
    return funcao(texto)

saudacao_2 = saudacao # aponta para a função (sem executar)

v = executa(saudacao_2, 'Bom dia')
print(v)

#%%

# Usando *args para deixar o código mais dinâmico

def saudacao(msg, nome):
    return f'{msg}, {nome}!'

def executa(funcao, *args): # função que chama outra funcão
    return funcao(*args)

saudacao_2 = saudacao # aponta para a função (sem executar)

v = executa(saudacao_2, 'Bom dia', 'Luiz')
print(v)

