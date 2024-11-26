#%%
# Atributos de classe

class Pessoa:
    ano_atual = 2022 # atributo disponível para todas instâncias

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual  - self.idade
    
p1 = Pessoa('João', 35)
p2 = Pessoa('Helena', 12)

print(Pessoa.ano_atual)
print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

#%%
# __dict__ e vars para atributos de instâncias
print(p1.__dict__)
print(vars(p1))

#%%
# Alterando valores
p1.__dict__['Outra coisa'] = 'coisa'
print(p1.__dict__)

#%%
# Criando objeto através de um dicionário

dados = {'nome': 'Leonardo', 'idade': 31}
p3 = Pessoa(**dados)
print(p3.__dict__)