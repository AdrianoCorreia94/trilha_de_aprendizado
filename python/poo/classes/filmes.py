class Filme:
    def __init__(self, titulo, ano):
        self.titulo = titulo
        self.ano = ano 
        self.status = False
    
    def play(self):
        if not self.status:
            print('Iniciando o filme')
            self.status = True
        else:
            print('O filme já está em reproducao ')

    def pause(self):
        if self.status:
            print('Pausando o filme')
            self.status = False
        else:
            print('O filme nao está em reproducao ')

    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}:{valor}' for chave, valor in self.__dict__.items()])}"

f1 = Filme('Fly', 1930)

f1.play()
print(f1)