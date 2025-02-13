class Musica:
    def __init__(self, titulo: str, compositor: str, ano: int, produtora: str):
        self.titulo = titulo
        self.compositor = compositor
        self.ano = ano
        self.produtora = produtora 
    
    def tocar(self):
        print(f'Tocando: {self.titulo}')

m1 = Musica('Depois de tudo','Ze Bruno', 2005, 'Resgate')

m1.tocar()