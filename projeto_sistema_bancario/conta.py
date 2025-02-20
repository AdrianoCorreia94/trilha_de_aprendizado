class Conta():
    _saldo = 0

    def __init__(self, conta, agencia, titular):
        self.conta = conta
        self.agencia = agencia
        self.titular = titular
        self.extrato = []

#-----------------------------------------------------------------------------------------

    # consultar saldo da conta
    def consulta_saldo(self):
        return print(f'{self._saldo}')
    
#------------------------------------------------------------------------------------------
    # realizar um deposito 
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor 
            self.extrato.append({'Deposito': f'{valor:.2f}'})
        else:
            print('Valor inválido para deposito')

#------------------------------------------------------------------------------------------
    # realizar um saque
    def sacar(self, valor):
        if valor <= 0:
            print('Valor incorreto para saque')
        elif valor <= self._saldo and self._saldo > 0 and valor > 0:
            self._saldo -= valor
            self.extrato.append({'Saque': f'{-valor:.2f}'})
        else:
            print('Saldo insuficiente para saque')

# ----------------------------------------------------------------------------------------
    
    # consultar extrato da conta 
    def ver_extrato(self):
        for item in self.extrato:
            print(item)

# -----------   FIM DA CLASSE -------------------------------

# instanciar uma conta
c1 = Conta('0001', '1234', 'Primeiro Cliente')

# consultar saldo incial
print('saldo inicial')
c1.consulta_saldo()
print(f"{'-'*30}\n")


# teste na funcao depositar válida
print('Tentativa de depositar 123 com sucesso ')
c1.depositar(123)
print('Saldo apos tentativa: ')
c1.consulta_saldo()
print(f"{'-'*30}\n")

# tentativa de saque maior que o saldo
print('Tentativa de sacar um valor maior que o saldo')
c1.sacar(750)
print('Saldo apos tentativa: ')
c1.consulta_saldo()
print(f"{'-'*30}\n")

# tentativa de depositar valor negativo
print('Tentativa de depositar valor negativo (-10)')
c1.depositar(-10)
print('Saldo apos tentativa: ')
c1.consulta_saldo()
print(f"{'-'*30}\n")

# tentativa de sacar valor negativo 
c1.sacar(-24)
c1.consulta_saldo()

# tentativa de saque valida 
c1.sacar(22)

c1.ver_extrato()

print(c1.conta)