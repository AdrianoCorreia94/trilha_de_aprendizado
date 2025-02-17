class Musica:
    def __init__(self, titulo: str, compositor: str, ano: int, produtora: str):
        self.titulo = titulo
        self.compositor = compositor
        self.ano = ano
        self.produtora = produtora 
    
    def tocar(self):
        print(f'Tocando: {self.titulo}')

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} : {valor}' for chave, valor in self.__dict__.items()])}"

m1 = Musica('Depois de tudo','Ze Bruno', 2005, 'Resgate')

m1.tocar()

print(m1)