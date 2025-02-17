class Conta:
    def __init__(self, conta, titular):
        self.conta = conta 
        self.titular = titular
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"
    
c1 = Conta(1001, 'Francisco Alves Silva')

print(c1)
