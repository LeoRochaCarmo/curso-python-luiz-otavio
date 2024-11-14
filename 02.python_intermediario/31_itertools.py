#%%
# Count é um iterador sem fim

from itertools import count

c1 = count(16, 8) # começa do 10 e pula com múltiplos de 8
r1 = range(16, 100, 8)

print('c1', hasattr(c1, '__iter__')) # count é iterável
print('c1', hasattr(c1, '__next__')) # count é iterator
print('r1', hasattr(r1, '__iter__')) # range é iterável
print('r1', hasattr(r1, '__next__')) # range não é iterator

print()
print('COUNT')
for i in c1:
    if i >= 100:
        break

    print(i)

print()
print('RANGE')
for i in r1:
    print(i)

#%% 
# Combinations, Permutations e Product - Itertools
# Combinação - Ordem não importa - iterável + tamanho do grupo
# Permutação - Ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')

pessoas = [
    'João', 'Joana', 'Luiz', 'Letícia',
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliéster']
]

print_iter(combinations(pessoas, 2))
print()

print_iter(permutations(pessoas, 2))
print()

print_iter(product(pessoas, *camisetas))

#%%
# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

alunos.sort(key=ordena)

grupos = groupby(alunos, key=ordena)

def agrupar_notas(list):
    list.sort(key=lambda i: i['nota'])


for chave, grupo in grupos:
    print(chave)
    print(*list(grupo), sep='\n')

#%%

from itertools import groupby

# Lista de alunos
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
]

def ordena(aluno):
    return aluno['nota']

# Decorator para ordenar, agrupar e formatar a saída dos grupos
def formata_saida(func):
    def wrapper(alunos):
        # Ordenar os alunos pela nota
        alunos.sort(key=ordena)
        # Agrupar os alunos pela nota
        grupos = groupby(alunos, key=ordena)
        
        # Usando list comprehension para formatar a saída e retorná-la como lista
        return [
            f"Nota: {chave}\n{'-' * 20}\n" + "\n".join(
                [f"{aluno['nome']} - Nota: {aluno['nota']}" for aluno in grupo]
            ) + "\n"
            for chave, grupo in grupos
        ]
    return wrapper

# Função para exibir os alunos do grupo, decorada
@formata_saida
def exibe_grupo(alunos):
    return alunos  # Retorna os alunos para que o decorador faça o trabalho

# Chamar a função decorada e imprimir a saída formatada
saida_formatada = exibe_grupo(alunos)
print("\n".join(saida_formatada))
#%%
