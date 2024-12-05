#%%
# random tem geradores de números pseudoaleatórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html

import random

#%%
# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")
random.seed(0)

# dessa forma sempre vou obter o mesmo número
r_range = random.randrange(10, 100, 2)
print(r_range)

#%%
# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(10, 100, 2)
print(r_range)

#%%
# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_int = random.randint(10, 100)
print(r_int)

#%%
# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_float = random.uniform(10, 100)
print(r_float)

#%%
# random.shuffle(SequenciaMutável) -> Embaralha a lista original
list = ['Corinthians', 'Flamengo', 'Bahia', 'Vasco']
random.shuffle(list)
print(list)

#%%
# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
new_list = random.sample(list, k= 2)
print(new_list)
print(list)

#%%
# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
new_list = random.choices(list, k=2)
print(new_list)
print(list)

