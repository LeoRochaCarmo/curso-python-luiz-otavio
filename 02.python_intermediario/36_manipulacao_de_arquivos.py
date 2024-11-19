# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

#%%
# CRIAÇÃO DE UM ARQUIVO

caminho_arquivo = '.\\dados\\manipulacao_de_arquivos.txt' # trocar para duas barras (WIN) para evitar confusão de escpape do python 

# arquivo = open(caminho_arquivo, 'w') # abre o arquvio
# arquivo.close() # fecha o arquivo para evitar problemas

#%%
# CONTEXT MANAGER (WITH)

# estrutura que gerencia o início e o fim de um bloco de código
# Evita a necessidade de chamar manualmente funções como close().

# ESCREVENDO E LENDO NO ARQUIVO
with open(caminho_arquivo, 'w+') as arquivo: # w+ -> escreve e le
    print(type(arquivo)) # visualizar o tipo de arquivo
    arquivo.write('Linha 1\n') # escrevendo e pulando linha
    arquivo.write('Linha 2\n')
    arquivo.writelines( # escreve várias linhas passando um iterável
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0,0) # move o cursor para o início
    print(arquivo.read())

    print('LENDO')
    arquivo.seek(0,0)
    print(arquivo.readline(), end='') # Ler linha por linha (como se fosse o next do iterador)
    print(arquivo.readline(), end='') # Remove a quebra de linha 
    print(arquivo.readline().strip()) # Remove a quebra de linha

    print('\nREADLINES')
    arquivo.seek(0,0)
    for linha in arquivo.readlines(): # gera uma lista de linhas
        print(linha.strip())
    
print('#' * 30, end='\n\n')

# LENDO ARQUIVO
with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

#%%
# MODOS DE ABERTURA

# a -> Escrita. Adiciona ao final do arquivo (append), sem sobrescrever
# encoding -> Especifica a codificação do arquivo (por exemplo, 'utf-8' ou 'latin-1'). É necessário para arquivos de texto.
with open(caminho_arquivo, 'a+', encoding='utf-8') as arquivo:
    arquivo.writelines(
        ('\nAPPEND\n', 'Atenção\n' 'Linha 5\n', 'Linha 6\n')
    )

#%%
# APAGAR ARQUIVO COM OS
import os

# os.remove(caminho_arquivo) # remove o arquivo
# os.unlink(caminho_arquivo) # remove o arquivo

#%%
# TROCAR NOME OU MOVER ARQUIVO

# os.rename(caminho_arquivo, 'arquivo_renomeado.txt')