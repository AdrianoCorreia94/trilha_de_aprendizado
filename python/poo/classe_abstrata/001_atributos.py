class Estudante:
    escola = 'X Genius' # atributos de classe

    def __init__(self, nome, matricula):
        # atributos de instancia
        self.nome = nome 
        self.matricula = matricula

    def __str__(self):
        return f"{self.__class__.__name__} : {','.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"
    
estudante1 = Estudante('Aluno 1', 1)
estudante2 = Estudante('Aluno 2', 2)

print(estudante2.escola)