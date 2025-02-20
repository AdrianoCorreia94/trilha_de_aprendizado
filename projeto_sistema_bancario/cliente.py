class Cliente:
    def __init__(self, nome, cidade, estado, telefone, email):
        self.nome = nome
        self.cidade = cidade
        self.estado = estado
        self._telefone = telefone 
        self._email = email 

