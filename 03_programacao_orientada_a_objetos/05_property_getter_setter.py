# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

#%%
# EXEMPLO DE GETTER FEITO NA MÃO

class Caneta:
    def __init__(self, cor):
        self.cor = cor
    
    # getter hard coded
    def get_cor(self):
        return self.cor

caneta = Caneta('Azul')
print(caneta.get_cor())

#%%

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    # método que se comporta como um atributo
    @property 
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return 123

caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor_tampa)

#%%
# SETTER E GETTER

class Caneta:
    def __init__(self, cor):
        # private (__) protected (_)
        self.cor = cor

    @property
    def cor(self):
        print('ESTOU NO GETTER')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('ESTOU NO SETTER')
        if valor == 'Preto':
            raise ValueError('Essa cor não pode.')
        self._cor = valor

caneta = Caneta('Azul')
caneta.cor = 'Roxo'
print(caneta.cor)

#%%