# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

#%%
class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor

class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome

# Carro 1
carro1 = Carro('Renegade')
fabricante1 = Fabricante('Jeep')
motor1 = Motor('V4')
carro1.motor = motor1
carro1.fabricante = fabricante1
print(carro1.nome, carro1.fabricante.nome, carro1.motor.nome)

# Carro 2
carro2 = Carro('Fusion')
fabricante2 = Fabricante('Ford')
carro2.motor = motor1
carro2.fabricante = fabricante2
print(carro2.nome, carro2.fabricante.nome, carro2.motor.nome)

