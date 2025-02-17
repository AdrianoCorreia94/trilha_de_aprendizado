class Automovel:
    def __init__(self, marca, modelo, aro, ano, cor, combustivel):
        self.marca = marca
        self.modelo = modelo
        self.aro = aro 
        self.ano = ano 
        self.cor = cor
        self.combustivel = combustivel
        self.estado = False

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

    def andar(self):
        if self.estado:
            print(f'{self.marca} {self.modelo} já está em movimento')

        else:
            print(f'Iniciando movimento de {self.marca} {self.modelo}')

    def parar(self):
        if not self.estado:
            print(f'{self.__class__.__name__} {self.marca} {self.modelo} já está parado')
        else:
            print(f'Parando {self.__class__.__name__} {self.marca} {self.modelo}')

# herancas da classe Automovel
class Motocicleta(Automovel):
    def __init__(self, marca, modelo, aro, ano, cor, combustivel, cilindradas):
        super().__init__(marca, modelo, aro, ano, cor, combustivel)
        self.cilindradas = cilindradas
        self.estado = True

motocicleta1 = Motocicleta('honda', 'biz', 17, 2004, 'black', 'Gasolina', 150)

print(motocicleta1)


class Carro(Automovel):
    def __init__(self, marca, modelo, aro, ano, cor, combustivel, portas):
        super().__init__(marca, modelo, aro, ano, cor, combustivel)
        self.portas = portas

carro1 = Carro('Honda', 'Fit', 15, 2007, 'Verde', 'Flex', 4)
print(carro1)

carro1.andar()
motocicleta1.andar()
carro1.parar()
motocicleta1.parar()