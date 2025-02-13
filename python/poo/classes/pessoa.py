# criar a classe
class Pessoa:
    # metodo de inicializacao da classe
    def __init__(self, nome: str, peso: float, altura:float, ano_nascimento: int):
        self.nome = nome
        self.peso = peso
        self.altura = altura/100 
        self.ano_nascimento = ano_nascimento
        self.imc = self.imc()  # posso criar um atributo atraves da chamada de um metodo dentro da classe, atencao: o metodo deve estar dentro da classe
    
    
    # metodos da classe
    def falar(self):
        print(f'{self.nome} está falando')
        
    def cozinhar(self):
        print(f'{self.nome} esta cozinhando')

    def andar(self):
        print(f'{self.nome} esta andando')

    def apresentar(self):
        print(f'{self.nome} está com {self.peso} kg e {self.altura} cm')

    # criar um metodo para calcular imc. 
    def imc(self):
        return (self.peso / (self.altura*self.altura))

    # criar um get para calcular a idade
    # a idade nao será um atributo, apenas um metodo, por isso devera ser acessada como metodo.
    def get_idade(self):
        return 2025 - self.ano_nascimento 

    
    # metodo str para retornar uma string compreensivel sobre o objeto
    #def __str__(self):
    #    return f'{self.nome} {self.altura}m {self.peso} kg nascido em {self.ano_nascimento}'
    
    # para nao precisar fazer manual como acima, usar a funcao abaixo
    def __str__(self):
        return f"{self.__class__.__name__} : {[f'{chave} = {valor}' for chave, valor in self.__dict__.items()]}"


# instanciar um objeto da classe pessoa
p1 = Pessoa('Carol', 75.5, 165, 1994)

# acessando aos atributos da classe
print(p1.nome)
print(p1.peso)
print(p1.altura)
print(p1.imc)

# acessando aos metodos da classe
p1.apresentar()
p1.andar()
p1.falar()
p1.cozinhar()

# acessando a idade; como foi definido como metodo deve ser acessada como metodo.
print(p1.get_idade())

# imprimindo a def str
print(p1)