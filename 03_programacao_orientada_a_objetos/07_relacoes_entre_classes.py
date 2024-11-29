# Relações entre classes: associação, agregação e composição\

#%%
# ASSOCIAÇÃO
# É um tipo de relação onde os objetos estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla o ciclo de vida de outro objeto.
class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta

class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'
    
escritor = Escritor('Leonardo')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina de escrever')

# associação entre dois objetos
escritor.ferramenta = caneta
print(escritor.ferramenta.escrever())

escritor.ferramenta = maquina_de_escrever
print(escritor.ferramenta.escrever ())

#%%
# AGREGAÇÃO
# Agregação é uma forma mais especializada de associação entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente. Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos. Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class Carrinho:
    def __init__(self):
        self._produtos = []

    def inserir_produtos(self, *produtos):
        self._produtos += produtos
        
    def preco_total(self):
        return sum([produto.preco for produto in self._produtos])
    
    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.nome, produto.preco)
        print()


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1, p2 = Produto('Pão', 2.5), Produto('Detergente', 5.49)

carrinho.inserir_produtos(p1, p2)

carrinho.listar_produtos()

carrinho.preco_total()

#%%
# COMPOSIÇÃO
# Composição é uma especialização da agregação. Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_enderecos(self, rua, numero):
        # Criando instância dentro da classe Cliente.
        # Instância deixa de existir se cliente for apagado.
        self.enderecos.append(Endereco(rua, numero))

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)
    
    def __del__(self):
        print('APAGANDO', self.nome)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('APAGANDO', self.rua, self.numero)


cliente1 = Cliente('Maria')
cliente1.inserir_enderecos('Rua Dolores', 172)
cliente1.inserir_enderecos('Rua Dorival', 271)
endereco_externo = Endereco('Rua externa', 342)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()

del cliente1

print(endereco_externo.rua)

print('AQUI TERMINA MEU CÓDIGO')



