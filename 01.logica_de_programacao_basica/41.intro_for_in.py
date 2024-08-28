# texto = 'Python'

# i = 0
# tamanho_texto = len(texto)

# while i < tamanho_texto:
#     print(texto[i])
#     # i += 1

texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto)
