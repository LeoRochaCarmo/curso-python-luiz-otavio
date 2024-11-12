
# __all__ -> variável especial
# define explicitamente quais símbolos (funções, classes, variáveis, etc.) 
# serão exportados quando o módulo ou pacote for importado usando o comando from <modulo> import *.
__all__ = [
    'variavel',
    'soma_do_modulo'
]

# . -> não preciso dar o nome da pasta raiz
# from aula_pacotes.modulo_2 import fala_oi -> é a mesma coisa 
from .modulo_2 import qualquer_coisa 

variavel = 'alguma coisa'

nova_variavel = 'outra coisa'

def soma_do_modulo(x,y):
    return x + y

