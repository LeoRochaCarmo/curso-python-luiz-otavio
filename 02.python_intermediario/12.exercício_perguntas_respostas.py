#%%
# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

#%%

print(perguntas[0]['Opções'][2])
    
#%%
qtde_acertos = 0
qtde_perguntas = len(perguntas)


for pergunta in perguntas:
    print(f'Pergunta: {pergunta["Pergunta"]}', end='\n\n')

    opcoes = pergunta['Opções']
    qtde_opcoes = len(opcoes)
    for i, opcao in enumerate(opcoes, start= 1):
        print(f'{i}) {opcao}')
    print('--------------------------------')
    
    resposta_certa = pergunta['Resposta']
    escolha_valida = False

    while not escolha_valida:
    
        escolha = input('Digite uma opção:')

        if escolha.isdigit():
            escolha_int = int(escolha)
            if escolha_int > 0 and escolha_int <= qtde_opcoes:
                escolha_valida = True
                if opcoes[escolha_int - 1] == resposta_certa:
                    print('Você acertou!')
                    print('--------------------------------')
                    qtde_acertos += 1
                else:
                    print('Você errou!')
                    print('--------------------------------')
            else:
                print(f'A opção {escolha_int} não está disponível.')
        else:
            print('Você não digitou um número.')

print(f'Você acertou {qtde_acertos} de {qtde_perguntas} perguntas!')



# %%
