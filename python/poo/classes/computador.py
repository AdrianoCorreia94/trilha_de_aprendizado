class Computador:
    def __init__(self, marca: str, cor: str, mem: float, proc: str):
        self.marca = marca
        self.cor = cor 
        self.memoria = mem
        self.processador = proc 
        
    
    def __str__(self):
        return f"{self.__class__.__name__}: {'; '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"
    

pc1 = Computador('Macbook', 'Prata', 8.0, 'I5200')

print(pc1)