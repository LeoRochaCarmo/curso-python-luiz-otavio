# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.

#%%
from functools import partial

class Foo:
    def __init__(self):
        self.public = "isso é público"
        self._protected = 'isso é protegido'
        self.__privado = 'isso é privado'

    def metodo_publico(self):
        return 'metodo_publico'
    
    def _metodo_protected(self):
        return '_metodo_protected'
    
    def __metodo_privado(self):
        return '__metodo_privado'

f = Foo()
print(f.public)
print(f._protected)
print(f.__privado)


