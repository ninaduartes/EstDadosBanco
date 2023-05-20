from PessoaFisica.clienteFisico import *
from transacoes import *


class ContaFisica(ClienteFisico):
    contador_contas = 0  # contador de contas cadastradas

    def __init__(self):
        super().__init__()
        self.numConta = None
        self.tipoConta = None
        self.saldo = None
        self.extrato = []

    def cadastrar_informacoes(self, cliente, tipo_conta, saldo):
        if isinstance(cliente, ClienteFisico):
            super().cadastrar_informacoes(cliente.agencia, cliente.numBanco, cliente.gerente, cliente.cpf, cliente.nome)
            ContaFisica.contador_contas += 1
            self.numConta = ContaFisica.contador_contas
            self.tipoConta = tipo_conta
            self.saldo = saldo
        else:
            print("Erro: É necessário cadastrar um ClienteFisico antes de criar uma ContaFisica.")

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print("Número da Conta:", self.numConta)
        print("Tipo de Conta:", self.tipoConta)
        print("Saldo:", self.saldo)
    
    def depositar(self, valor):
        if self.tipoConta == "corrente" or self.tipoConta == "especial":
            self.saldo += valor
            transacao = Transacao("Depósito", valor)
            self.extrato.append(transacao)
            print("Depósito realizado com sucesso.")
            print("Novo saldo:", self.saldo)
        else:
            print("Ocorreu um erro, tente novamente")

    def sacar(self, valor):
        if self.tipoConta == "corrente":
            if valor < self.saldo:
                self.saldo -= valor
                transacao = Transacao("Saque", valor)
                self.extrato.append(transacao)
                print("Saque realizado com sucesso.")
                print("Novo saldo:", self.saldo)
            else:
                print("Erro: Não é possível sacar o valor total da conta corrente.")
        elif self.tipoConta == "especial":
            if self.saldo > 0:
                if valor <= self.saldo:
                    self.saldo -= valor
                    transacao = Transacao("Saque", valor)
                    self.extrato.append(transacao)
                    print("Saque realizado com sucesso.")
                    print("Novo saldo:", self.saldo)
                else:
                    print("Saldo insuficiente.")
            else:
                print("Erro: Não é possível realizar saque em conta especial com saldo igual a zero.")
 
    def exibir_extrato(self):
        print("Extrato:")
        for transacao in self.extrato:
            data_formatada = transacao.data_hora.strftime("%d/%m/%Y")  # Formata a data no formato dia/mês/ano
            hora_formatada = transacao.data_hora.strftime("%H:%M")  # Formata a hora no formato hora:minuto
            print("\nNúmero da conta: ", self.numConta)
            print("Nome do cliente: ", self.nome)
            print("-----------")
            print("Data: ", data_formatada)
            print("Hora: ", hora_formatada)
            print("Tipo: ", transacao.tipo)
            print("Valor: ", transacao.valor)
            print("-----------")
        print("Saldo atual: R$", self.saldo)

    