# __all__ -> variável especial
# define explicitamente quais símbolos (funções, classes, variáveis, etc.) 
# serão exportados quando o módulo ou pacote for importado usando o comando from <modulo> import *.

__all__ = [
    'variavel',
    'soma_do_modulo'
]

variavel = 'alguma coisa'

def soma_do_modulo(x,y):
    return x + y