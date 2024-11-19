#%%
# PROBLEMA DOS PARÂMETROS MUTÁVEIS EM FUNÇÕES PYTHON
# O parâmetro lista=None é usado para evitar o comportamento problemático de listas mutáveis como valor padrão em Python. 
# Se a lista fosse inicializada diretamente como uma lista vazia (ou seja, lista=[]), ela seria compartilhada entre todas 
# as chamadas subsequentes da função, o que causaria efeitos colaterais inesperados (todos os clientes sendo adicionados a uma única lista).

def adiciona_clientes(nome, lista=None):
    if  lista is None:
        lista = []
    lista.append(nome)
    return lista

cliente1 = adiciona_clientes('Leo')
adiciona_clientes('Joana', cliente1)
adiciona_clientes('Fernando', cliente1)
print(cliente1)

cliente2 = adiciona_clientes('Leonardo')
adiciona_clientes('João', cliente2)
print(cliente2)

# %%
