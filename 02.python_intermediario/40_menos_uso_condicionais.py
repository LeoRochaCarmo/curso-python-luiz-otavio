
# Exercício - Lista de tarefas com desfazer e refazer

import os

lista_tarefas = []
tarefas_refazer = []
comandos = ['listar', 'desfazer', 'refazer', 'clear']

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

    imprimir(tarefas)

def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nehuma tarefa para refazer\n')
        return
    
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)

    imprimir(tarefas)

def adicionar(tarefa, tarefas):
    print()
    if not tarefa.strip():
        print('Você não digitou nenhuma tarefa\n')
        return
    
    tarefas.append(tarefa)

    imprimir(tarefas)

while True:
    print('Comandos: listar, desfazer, refazer, clear')
    entrada = input('Digite uma tarefa ou comando: ')
    entrada_formatada = entrada.lower()

    comandos = {
        'listar': lambda: listar(lista_tarefas),
        'desfazer': lambda: desfazer(lista_tarefas, tarefas_refazer),
        'refazer': lambda: refazer(lista_tarefas, tarefas_refazer),
        'clear': lambda: os.system('cls'),
        'adicionar': lambda: adicionar (entrada, lista_tarefas)
    }

    comando = (
        comandos.get(entrada_formatada) 
        if comandos.get(entrada_formatada) is not None 
        else comandos['adicionar']
    )
    
    comando()
