"""
Iterando strings com while
"""

# print(nome)
# print(tamanho_nome)

# print(nome[3])

nome = 'Leonardo Rocha'
tamanho_nome = len(nome)
contador = 0
novo_nome = ''

while contador < tamanho_nome:
    letra = nome[contador]
    novo_nome += f'*{letra}'
    contador += 1


novo_nome += '*'
print(novo_nome)
