#%%

# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}

s1 = set() # criando set vazio

s1 = set('Leonardo')
print(s1, type(s1))

s2 = {'Leonardo', 1, 2, 3}
print(s2, type(s2))

#%%
# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

s3 = {1, 2, 3, 3, 3, 3, 1}
print(s3) # sets eliminam valores duplicados

#%%
# Removendo duplicatas de forma mais simples
l1 = [1, 2, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = list(s1)
print(l2)

#%%
s1 = {1, 2, 3, [4, 5, 6]} # Erro -> lista é mutável

#%%

s1 = {1, 2, 3}
print(3 in s1)

#%%
# Brincadeira para remover duplicatas usando for 
l1 = [1, 2, 3, 3, 3, 3, 1]
l1_sem_duplicatas = []

for i in l1:
    if not l1[i] in l1_sem_duplicatas:
        l1_sem_duplicatas.append(i)

print(l1_sem_duplicatas)

#%% 
# Métodos úteis:
# add, update, clear, discard

s1 = set()
s1.add('Leo')
s1.add(1)
s1.update('Rocha') # adiciona letra por letra
s1.clear() # limpa o seta
s1.update(('Leo','Rocha', 1, 2, 3, 4)) # passando iterável
s1.discard('Leo') # elimina um valor
print(s1)

#%%
# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2 # unindo
print(s3)
s4 = s1 & s2 # intersecção
print(s4) 
s5 = s1 - s2 # apenas itens no set da esquerda
print(s5)
s6 = s1 ^ s2
print(s6) # itens que não estão em ambos

#%%
# Exemplo de uso dos sets (validação feita por mim)
letras = set()

while len(letras) < 5:

    letra = input('Digite uma letra:')

    if not letra.isdigit():
        if len(letra) == 1:
            letras.add(letra.lower())
            print(f'Letra {letra} adicionada.')
        else:
            print(f'Você digitou {len(letra)} letras. '
                  'Digite apenas uma.')
    else:
        print('Você não digitou uma letra.')
    


print(letras)



# %%