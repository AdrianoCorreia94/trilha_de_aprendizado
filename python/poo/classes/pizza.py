class Pizza:
    def __init__(self, estabelecimento, sabor, tamanho, borda):
        self.estabelecimento = estabelecimento 
        self.sabor = sabor
        self.tamanho = tamanho 
        self.borda = borda

    def __str__(self):
        return f"{self.__class__.__name__}: {'/ '.join([f'{chave} : {valor}' for chave, valor in self.__dict__.items()])}"

p1 = Pizza('Mestre Pizza', 'Crocante', 'G', 'Normal')
print(p1)