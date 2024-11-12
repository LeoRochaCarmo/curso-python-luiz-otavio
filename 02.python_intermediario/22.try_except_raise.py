# Try, except, else e finally

#%%
# Try / except
# Erro será silenciado

try:
    a = 18
    b = 0 #NameError
    print(b[0]) # TypeError
    print('Linha 1'[1000]) #IndexError
    c = a / b # erro de divisão por zero
    print('Linha 2') # linha não será executada
except ZeroDivisionError:
    print('Dividiu por zero.')
except NameError:
    print('b não foi definido.')
except (TypeError, IndexError) as error: # 2 erros em uma linha só
    print('TypeError + IndexError')
    print('MSG:', error)
    print('nome:', error.__class__.__name__)
except Exception:
    print('Erro desconhecido.')

print('CONTINUAR')

# %%
# Try / Finally
# Finally sempre será executado.
# Else executa se não existerem erros.

try:
    print('ABRIR ARQUIVO')
    8 / 0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError:
    print('DIVIDIU ZERO')
except (NameError, ImportError) as error:
    print('DIVIDIU ZERO')
else:
    print('NÃO DEU ERRO')
finally: # sempre será executado
    print('FECHAR ARQUIVO')

#%%

# raise - lançando exceções (erros)
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

# print(123)
# raise ValueError('Deu erro') # Lança um erro

def nao_aceito_zero(d):
    if d == 0:
        raise ZeroDivisionError('Tentativa de divisão por zero')
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float. '
            f'"{tipo_n.__name__}" enviado'
        )
    return True
    
def divide(n,d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    nao_aceito_zero(d)
    return n / d

print(divide(3,'0'))