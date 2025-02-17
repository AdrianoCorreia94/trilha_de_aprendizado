class Pessoa:

    # construtor/inicializador __init__
    def __init__(self, nome, altura, peso):
        self.nome = nome 
        self.altura = altura
        self.peso = peso 

    def __str__(self):
        return f"{self.__class__.__name__}: {(', ').join([f'{key} {value}' for key, value in self.__dict__.items()])}"
    

    # destrutores __del__
    def __del__(self):
        print('destruind0')

    # o metodo destrutor é executado automaticamente, sem necessidade de ser chamado.


p = Pessoa('Joao Pessoa', 1.76, 67.2)
print(p.__str__())
print(p.nome)