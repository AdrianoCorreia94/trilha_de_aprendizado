class Janela:
    def __init__(self, largura, altura, vidro, tipo):
        self.largura = largura
        self.altura = altura 
        self.vidro = vidro 
        self.tipo = tipo 
        self.status = False 

    def abrir(self):
        if self.status == False:
            print('Abrindo a janela')
            self.status = True 
        else:
            print('A janela já está aberta')

    def fechar(self):
        if self.status == False:
            print('A janela já está fechada')
        else:
            print('Fechando a janela')
            self.status == False

    def __str__(self):
        return f'{self.__class__.__name__} : {', '.join([f"{chave} : {valor}" for chave, valor in self.__dict__.items()])}'

j1 = Janela(150, 130, 3, 'correr')

j1.abrir()
print(j1)