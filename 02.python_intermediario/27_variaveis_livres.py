#%%
# Variáveis livres + nonlocal (locals, globals)

def fora(x):
    a = x

    def dentro():
        #print(locals())
        print(dentro.__code__.co_freevars)
        return a
    return dentro

dentro1 = fora(10)
dentro2 = fora(10)

print(dentro1())
print(dentro2())

#%%

print(*globals(),sep='\n')

#%%

# Variável Livre
# variável livre é aquela que não é local à função em que é usada, mas está disponível em um escopo mais amplo.

def criador_de_mensagem(mensagem):
    def exibir_mensagem():
        print(mensagem)  # 'mensagem' é uma variável livre aqui
    return exibir_mensagem

nova_funcao = criador_de_mensagem("Olá, mundo!")
nova_funcao() 

#%%

# nonlocal
'''
Definição: A palavra-chave nonlocal é usada em funções aninhadas (uma função dentro de outra). 
Ela permite que uma variável de um escopo externo não global seja acessada e modificada. 
Ou seja, nonlocal se refere a variáveis definidas em um escopo de função que não é o local e nem o global.
'''

# Diferença entre nonlocal e global
'''
global -> permite modificar uma variável global (definida fora de todas as funções) dentro de uma função.
nonlocal -> é usado para modificar variáveis que não são locais nem globais, mas que estão em um escopo intermediário.
'''

def concatenar(string_inicial):
    valor_final = string_inicial

    def interna(valor_a_concatenar = ''):
        nonlocal valor_final
        valor_final += valor_a_concatenar
        return valor_final
    return interna

c = concatenar('a')
print(c('b'))
print(c('c'))
print(c('d'))
final = c()
print('Resultado final:', final)
