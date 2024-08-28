frase = 'O Python é uma linguagem de programação'\
    'multiparadigma. '\
    'Python foi criado pro Guido van Rossum.'

# print(frase.count('Python'))

i = 0
apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while i < len(frase):
    letra_atual = frase[i]
    qtd_atual = frase.count(letra_atual)
    i += 1

    if letra_atual == ' ':
        continue

    if apareceu_mais_vezes < qtd_atual:
        apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual


print('A letra que apareceu mais vezes foi ' 
    f'{letra_apareceu_mais_vezes.upper()}.Ela apareceu '
    f'{apareceu_mais_vezes}x'
)
  
