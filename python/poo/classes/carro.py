class Carro:
    def __init__(self, ano: int, marca: str, cor: str):
        self.marca = marca
        self.cor = cor
        self.ano = ano
        self.estado = False

    # metodos da funcao
    def andar(self):
        if  self.estado:
            print(f'{self.marca} {self.cor} {self.ano} ja esta em movimento')
        else:
            print(f'{self.marca} {self.ano} {self.cor} esta iniciando movimento')
            self.estado = True

    def parar(self):
        if self.estado:
            print(f'{self.marca} {self.ano} {self.cor} esta parando')
        else:    
            print(f'{self.marca} {self.ano} {self.cor} já está parado')


carro1 = Carro(2015, 'Corsa', 'Vermelho')
carro1.parar()
carro1.andar()
carro1.parar()
