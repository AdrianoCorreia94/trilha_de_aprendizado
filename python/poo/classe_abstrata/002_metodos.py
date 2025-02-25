# metodos de classe e metodos estáticos

# metodo de classe: ligado a classe, apontanto para a classe e nao para o objeto
# utilizado para criar metodos de fabrica (metodo que retornam instancias)

# metodo estatico: nao recebe argumento explicito, nao pode acessar ou modificar um atributo da classe
# usado para criar funcoes utilitarias.


class Pessoa:
    def __init__(self, nome = None, idade= None):
        self.nome = nome 
        self.idade = idade

    #criando o metodo de classe
    @classmethod
    def criar_com_data_nascimento(cls, nome, ano, mes, dia):
        idade = 2025 - ano
        return cls(nome, idade)
    

    # criando metodo estatico
    @staticmethod 
    def maior(idade):
        return idade > 17

# criar uma instancia de pessoas atraves do metodo de classe
p = Pessoa.criar_com_data_nascimento('Abelardo', 1994, 1, 15)
print(p.idade)

# acessando o metodo estatico da classe pessoa
print(Pessoa.maior(p.idade))    # passando a idade da instancia 
print(Pessoa.maior(17)) # acessando o metodo estatico com um arg qualquer


