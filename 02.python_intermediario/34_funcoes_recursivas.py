#%%
# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm

def recursiva(inicio=0, fim=5):
    # Caso recursivo - contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)

# recursiva() # Gera um Stack Overflow
# erro que ocorre em programação e sistemas de computador quando a pilha de execução (stack) 
# ultrapassa seu limite de capacidade, resultando em uma falha.

#%%
def recursiva(inicio=0, fim=5):
    print(inicio, fim)

    # Caso base
    if inicio >= fim:
        return fim
    
    # Caso recursivo - contar até chegar ao final
    inicio += 1
    return recursiva(inicio, fim)

print(recursiva())

#%%
# LIMITE DE RECURSÃO E CUIDADOS
import sys 

sys.setrecursionlimit(1004)

print(recursiva(0, 1001)) # Código ainda quebra

#%%
# FUNÇÃO RECURSIVA PARA CALCULAR FATORIAL

def factorial(n):
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

print(factorial(4))


