#%%
# listas dentro de uma lista
salas = [
    ['Leo1', 'Leo2'],
    ['Leo3', 'Leo4'],
    ['Leo5', 'Leo6', (0, 10, 20, 30, 40)],
]

print(salas)

#%%
# acessando o primeiro valor da lista 2
print(salas[1][0])

# acessando o número 20 que está na tupla
print(salas[2][2][2])

#%%
# usando for para pegar valores
for sala in salas:
    print(f'A sala é: {sala}')
    for aluno in sala:
        print(aluno)
