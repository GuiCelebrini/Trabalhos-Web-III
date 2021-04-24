class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

class Conta:
    
    def __init__(self, numero, clientes, valor_saldo):
        self.numero = numero
        self.clientes = clientes
        self.saldo = 0
        self.lista_operacoes = []

        self.depositar(valor_saldo)

    def resumir_informacoes(self):
        print('Proprietário(s):')
        for cliente in self.clientes:
            print(cliente.nome)
        print('Conta número %s | Saldo: %10.2f' %(self.numero, self.saldo))
        

    def exibir_extrato(self):
        print('Operações realizadas recentemente:')
        for operacao in self.lista_operacoes:
            print(operacao)

    def sacar(self, valor_saque):
        if valor_saque > self.saldo:
            return False
        self.saldo -= valor_saque
        self.lista_operacoes.append('Saque no valor %10.2f | Saldo: %10.2f' %(valor_saque, self.saldo))

    def depositar(self, valor_deposito):
        self.saldo += valor_deposito
        self.lista_operacoes.append('Deposito no valor %10.2f | Saldo: %10.2f' %(valor_deposito, self.saldo))

class ContaEspecial(Conta):
    def __init__(self, numero, clientes, valor_saldo, valor_limite):
        self.numero = numero
        self.clientes = clientes
        self.saldo = 0
        self.limite = valor_limite
        self.lista_operacoes = []

        self.depositar(valor_saldo)

    def sacar(self, valor_saque):
        if valor_saque > self.saldo + self.limite:
            return False
        self.saldo -= valor_saque
        self.lista_operacoes.append('Saque no valor %10.2f | Saldo: %10.2f' %(valor_saque, self.saldo))