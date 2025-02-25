# importar modulo abc 

from abc import ABC, abstractmethod


class ControleRemoto(ABC):
    pass

    @abstractmethod # a marcacao abstractmethod obriga a implementacao nas classes filhas
    def ligar(self):
        print(f'ligando a partir de {self.marca}')

    @abstractmethod
    def desligar(self):
        print(f'Desligando a partir de {self.marca}')

    @property
    @abstractmethod # também obriga a criacao da propriedade na classe filho
    def marca(self, marca):
        self.marca = marca 
        return marca

class ControleTv(ControleRemoto):
    pass 

    def ligar(self):
        return super().ligar()  # posso implementar a partir do metodo da classe pai 
    
    def desligar(self): # ou posso implementar do zero um novo metodo
        print(f'Desligando COM o {self.marca}')

    @property
    def marca(self):
        self.marca_controle = 'MyTv'
        return self.marca_controle


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        return super().ligar()
    
    def desligar(self):
        return super().desligar()
    
    @property
    def marca(self):
        self.marca_ar = 'MyAir'
        return self.marca_ar


c1 = ControleTv()
c1.desligar()
c1.ligar()
print(c1.marca)

c2 = ControleArCondicionado()
print(c2.marca)
c2.ligar()
c2.desligar()
