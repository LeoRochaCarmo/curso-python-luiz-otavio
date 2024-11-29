# Herança simples - Relações entre classes
# Associação - usa
# Agregação - tem
# Composição - É dono de
# Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

#%%
# EXEMPLO DE HERANÇA 
class Pessoa:
    cpf = '1234'
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

    def falar_nome_classe(self):
        print(self.nome, self.__class__.__name__)

class Cliente(Pessoa):
    ...

class Aluno(Pessoa):
    ...

c1 = Cliente('Leo', 'Rocha')
c1.falar_nome_classe()

a1 = Aluno('Leandro', 'Pedra')
a1.falar_nome_classe()
a1.cpf

#%%
# FUNÇÃO HELP
help(Cliente)

# %%
# super() e a sobreposição de membros - Python Orientado a Objetos
# super() -> retorna temporariamente a super classe
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class
class MinhaString(str):
    def upper(self):
        print('CHAMOU UPPER')
        retorno = super(MinhaString, self).upper()
        print('DEPOIS DO UPPER')
        return retorno

string = MinhaString('Luiz')
print(string.upper())

#%%
# EXEMPLO COM SUPER() E SOBREPOSIÇÃO DE MÉTODOS E ATRIBUTOS
# Method resolution order
class A:
    atributo_a = 'valor a'

    def __init__(self, atributo): # init é repassado para B e C
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo) # retornando init do A
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('EI! Burlei o sistema')

    def metodo(self):
        super(C, self).metodo() # retorna o método em B
        super(B, self).metodo() # retorna o método em A
        print('C')

c = C('atributo', 'outra coisa qualquer')
print(c.atributo)
print(c.outra_coisa)
print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()