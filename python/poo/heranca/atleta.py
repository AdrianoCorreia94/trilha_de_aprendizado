class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Atleta(Pessoa):
    def __init__(self, **kw):
        super().__init__(**kw)

    def aquecer(self):
        return f'{self.nome} aquecendo'

class Corredor(Atleta):
    def __init__(self, **kw):
        super().__init__(**kw)

    def correr(self):
        return f'{self.nome} correndo'
    
class Nadador(Atleta):
    def __init__(self, **kw):
        super().__init__(**kw)

    def nadar(self):
        return f'{self.nome} nadando'
    
class Ciclista(Atleta):
    def __init__(self, **kw):
        super().__init__(**kw)

    @property # torna a funcao um atributo da classe
    def pedalar(self):
        return f'{self.nome} pedalando'
    

class Triatleta(Ciclista, Nadador, Corredor):
    def __init__(self, **kw):
        super().__init__(**kw)


t = Triatleta(nome='Josivaldo')

print(t.correr(), t.pedalar, t.aquecer())   # chamando as funcoes da classe

print(t.pedalar) # como foi inserido a notacao @property, a funcao pedalar se tornou um atributo, entao deve ser chamada como atributo.
print(t.nome)