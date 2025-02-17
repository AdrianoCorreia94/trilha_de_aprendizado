class Instrumento:
    def __init__(self, marca: str, cor: str, cordas: int):
        self.marca = marca
        self.cor = cor 
        self.cordas = cordas 

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"
    

i1 = Instrumento('Fender', 'WoodStock', 4)

print(i1)