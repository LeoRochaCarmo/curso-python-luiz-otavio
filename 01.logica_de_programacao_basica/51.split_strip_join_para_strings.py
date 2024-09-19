#%%
# split -> divide uma string
frase = '  Olha só que, coisa interessante'
lista_frase = frase.split()
print(lista_frase)

#%%
# divindo pela vírgula
lista_frase = frase.split(',')
print(lista_frase)

#%%
# usando for
# removendo espaços e adicionando elementos em uma outra lista
lista_frase_fixed = []
for i, frase in enumerate(lista_frase):
    lista_frase_fixed.append(lista_frase[i].strip()) # strip -> corta os espaços do começo ou fim de uma str
    
print(lista_frase_fixed)
print(lista_frase)

#%%
# join -> une strings
frases_unidas = ', '.join(lista_frase_fixed)
print(frases_unidas)
