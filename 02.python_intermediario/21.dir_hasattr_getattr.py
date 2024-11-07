#%%
#dir, hasttr e getattr em Python

#dir -> Retorna uma lista de nomes de atributos e métodos de um objeto.
#hasttr -> Verifica se um objeto possui um determinado atributo.
#getattr -> Retorna o valor de um atributo de um objeto, se ele existir.

string = 'Leonardo'
metodo = 'upper'

if hasattr(string, metodo):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo) 

