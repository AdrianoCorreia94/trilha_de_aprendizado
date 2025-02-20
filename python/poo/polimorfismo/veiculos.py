class Veiculo:
    def __init__(self, marca, modelo, cor, ano):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor 
        self.ano = ano 

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"
    
    def andar(self):
        return f' {self.marca} {self.modelo} está andando'
    
# classe carro herdando de veiculos
class Carro(Veiculo):
    def __init__(self, marca, modelo, cor, ano, portas):
        super().__init__(marca, modelo, cor, ano)
        self.portas = portas

    # aqui a funcao andar ja esta implementada da classe pai Veiculos

# classe aviao herdando de Veiculo
class Aviao(Veiculo):

    # metodo inicializador
    def __init__(self, marca, modelo, cor, ano):
        super().__init__(marca, modelo, cor, ano)


    def decolar(self):
        return (f'{self.__class__.__name__} {self.marca} {self.modelo} Esta decolando...')

    # APLICACAO DE POLIMORFISMO
    # alteracao do metodo andar
    def andar(self):
        return (f'Este veículo não anda, somente voa')
    
# instancias de classes
carro = Carro('Chevrolet', 'Camaro 2020', 'Preto', 2019, 4)
print(carro)

aviao = Aviao('Azul', '3229', 'Branco', 2009)

print(aviao.andar())