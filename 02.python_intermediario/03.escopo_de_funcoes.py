#%%
"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.

"""

x = 1

def escopo():
    print(x)

escopo()

#%%
# Escopo global X local
x = 1

def escopo():
    x = 10 # este x não é o mesmo do escopo global
    def outra_funcao():
        x = 11 # x que está apenas nesse escopo
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)

#%% 
# Manipulando o x que está fora das funções
x = 1

def escopo():
    global x # altera o valor de x que está no escopo global (MÁ PRÁTICA)
    x = 10 
    def outra_funcao():
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)

print(x)
escopo()
print(x)
