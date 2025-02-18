class Funcionario:
    def __init__(self, nome):
        self.nome = nome 
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

# classe filha pessoa fisica
class PF(Funcionario):
    def __init__(self, cpf, **kargs):
        self.cpf = cpf
        super().__init__(**kargs)

    def __str__(self):
        return f'esse é fisica'

# classe filha pessoa juridica
class PJ(Funcionario):
    def __init__(self, cnpj, **kargs):
        self.cnpj = cnpj
        super().__init__(**kargs)

    def __str__(self):
        return f'esse é juridica'

# classe "neta" funcionario de empresa terceirizada
class Terceirizado(PJ, PF):
    def __init__(self, **kargs):
        super().__init__(**kargs)

    def __str__(self):
        return f'esse é terceirizada'

# instancia do objeto
t1 = Terceirizado(cpf= 123456789, nome='Terc1', cnpj='1234')

print(t1)