class Instrumento:
    def __init__(self, marca: str, cor: str, cordas: int):
        self.marca = marca
        self.cor = cor 
        self.cordas = cordas 

class EletricBass(Instrumento):
    def __init__(self, marca, cor, cordas, captadores):
        super().__init__(marca, cor, cordas, captadores)
        self.captadores = captadores