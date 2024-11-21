
# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os

def imprimir(tarefas):
    print('Tarefas: ')
    for tarefa in tarefas:
        print(f'{tarefa}')
    print()

def listar(tarefas):
    print()
    if not tarefas:
        print('Nehuma tarefa para listar\n')
        return
    
    imprimir(tarefas)

def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nehuma tarefa para desfazer\n')
        return
    
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nehuma tarefa para refazer\n')
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)

def adicionar(tarefa, tarefas):
    print()
    if not tarefa.strip():
        print('Você não digitou nenhuma tarefa\n')
        return
    
    tarefas.append(tarefa)

lista_tarefas = []
tarefas_refazer = []
comandos = ['listar', 'desfazer', 'refazer', 'clear']

while True:
    print('Comandos: listar, desfazer, refazer, clear')
    entrada = input('Digite uma tarefa ou comando: ')
    entrada_formatada = entrada.lower()

    try:
        float(entrada)
        print('você digitou um número. Digite um comando.\n')
    
    except ValueError:
        pass

        if entrada_formatada == comandos[0]:
            listar(lista_tarefas)

        elif entrada_formatada == comandos[1]:
            desfazer(lista_tarefas, tarefas_refazer)
            imprimir(lista_tarefas)

        elif entrada_formatada == comandos[2]:
            refazer(lista_tarefas, tarefas_refazer)
            imprimir(lista_tarefas)

        elif entrada_formatada == comandos[3]:
            os.system('clear')

        else:
            adicionar(entrada, lista_tarefas)
            imprimir(lista_tarefas)
