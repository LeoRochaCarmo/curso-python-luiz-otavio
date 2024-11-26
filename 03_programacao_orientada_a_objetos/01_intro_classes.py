#%%
# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

class Pessoa:
    ...

p1 = Pessoa() # criação de um objeto
p1.nome = 'Leonardo'
p1.sobrenome = 'Rocha'

print(p1.nome)
print(p1.sobrenome)

#%%
# Introdução ao método __init__ (inicializador de atributos)
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome # criando atributo
        self.sobrenome = sobrenome 

p2 = Pessoa('Leonardo', 'Rocha')

print(p2.nome)
print(p2.sobrenome)

#%%
# Métodos em instâncias de classes Python
# Hard coded - É algo que foi escrito diretamente no código

class Carro:
    def __init__(self, nome):
        self.nome = nome
        # self.nome = 'Fusca' # Hard coded

    def acelerar(self): # criando um método
        print(f'{self.nome} está acelerando.')

fusca = Carro('Fusca')
print(fusca.nome)
fusca.acelerar()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()

#%%
# Entendendo self em classes Python
# Classe - Molde (geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

onix = Carro('Onix')
onix.acelerar()
Carro.acelerar(onix)

#%%
# Escopo da classe e de métodos da classe

class Animal:

    def __init__(self, nome):
        self.nome = nome

        # variavel = 'valor'
        # print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)

leao = Animal('Leão')
print(leao.nome)
print(leao.comendo('carne'))
print(leao.executar('carne'))

#%%
# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} não está filmando...')
            return
        
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False
            

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando...')
            return

        print(f'{self.nome} está filmando...')
        self.filmando = True

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando...')
            return
        
        print(f'{self.nome} está fotografando...')

c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar() # começou a filmar
c1.filmar() # manteve o estado
c1.fotografar()
c1.parar_filmar()
c1.fotografar()

print()

c2.filmar()
c2.filmar()
c2.parar_filmar()
c2.fotografar()
c2.fotografar()
