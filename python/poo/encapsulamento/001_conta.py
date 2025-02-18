class Conta:
    def __init__(self, agencia, saldo):
        self.agencia = agencia
        self._saldo = saldo # para indicar que o atributo é privado, usa-se o underline 

        # nao se acessa o atributo privado diretamente, utiliza-se um metodo para acessar

    def depositar(self):
        #...
        pass

    def sacar(self):
        #...
        pass

    def ver_saldo(self):
        return self._saldo

conta1 = Conta('0001', 50.27)   # instancia da classe.

saldo = conta1.ver_saldo()  # atribuindo o saldo a um objeto. 
print(saldo)    # imprimir o objeto que guardou o saldo.

print(conta1.ver_saldo())   # imprimir o saldo sem guardar em um objeto.