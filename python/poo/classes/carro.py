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

    def __str__(self):
        return f"{self.__class__.__name__} : {'; '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

carro1 = Carro(2015, 'Corsa', 'Vermelho')
carro1.parar()
carro1.andar()
carro1.parar()

print(carro1)