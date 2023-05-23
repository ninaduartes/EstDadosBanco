from PessoaJuridica.clienteJuridico import *
from transacoes import *
import sys

class ContaJuridica(ClienteJuridico):
    contador_contas = 0  # contador de contas cadastradas

    def __init__(self):
        super().__init__()
        self.numConta = None
        self.tipoConta = None
        self.saldo = None
        self.extrato = []

    def cadastrar_informacoesPJ(self, clientePJ, tipo_conta, saldo):
        if isinstance(clientePJ, ClienteJuridico):
            super().cadastrar_informacoesPJ(clientePJ.agencia, clientePJ.numBanco, clientePJ.gerente, clientePJ.cnpj, clientePJ.nome, clientePJ.telefone, clientePJ.endereco, clientePJ.cep)
            ContaJuridica.contador_contas += 1
            self.numConta = ContaJuridica.contador_contas
            self.tipoConta = tipo_conta
            self.saldo = saldo
        else:
            print("Erro: É necessário cadastrar um ClienteFisico antes de criar uma ContaFisica.")
        
        print("\nAperte ENTER para voltar ao menu")
        sys.stdin.readline()


    def exibir_informacoesPJ(self):
        super().exibir_informacoesPJ()
        print("Número da Conta:", self.numConta)
        print("Tipo de Conta:", self.tipoConta)
        print("Saldo:", self.saldo)
    
    def depositarPJ(self, valor):
        if self.tipoConta == "corrente" or self.tipoConta == "especial":
            self.saldo += valor
            transacao = Transacao("Depósito", valor)
            self.extrato.append(transacao)
            print("Depósito realizado com sucesso.")
            print("Novo saldo: R$", self.saldo)
        else:
            print("Ocorreu um erro, tente novamente")

        print("\nAperte ENTER para voltar ao menu")
        sys.stdin.readline()


    def sacarPJ(self, valor):
        if self.tipoConta == "corrente":
            if valor < self.saldo:
                self.saldo -= valor
                transacao = Transacao("Saque", valor)
                self.extrato.append(transacao)
                print("Saque realizado com sucesso.")
                print("Novo saldo: R$", self.saldo)
            else:
                print("Erro: Não é possível sacar o valor total da conta corrente.")
        elif self.tipoConta == "especial":
            if self.saldo > 0:
                if valor <= self.saldo:
                    self.saldo -= valor
                    transacao = Transacao("Saque", valor)
                    self.extrato.append(transacao)
                    print("Saque realizado com sucesso.")
                    print("Novo saldo: R$", self.saldo)
                else:
                    print("Saldo insuficiente.")
            else:
                print("Erro: Não é possível realizar saque em conta especial com saldo igual a zero.")
            
            print("\nAperte ENTER para voltar ao menu")
            sys.stdin.readline()

 
    def exibir_extratoPJ(self):
        print("Extrato:")
        print("\n-----------")
        print("Número da conta: ", self.numConta)
        print("Nome do cliente: ", self.nome)
        for transacao in self.extrato:
            data_formatada = transacao.data_hora.strftime("%d/%m/%Y")  # Formata a data no formato dia/mês/ano
            hora_formatada = transacao.data_hora.strftime("%H:%M")  # Formata a hora no formato hora:minuto
            print("-----------")
            print("Data: ", data_formatada)
            print("Hora: ", hora_formatada)
            print("Tipo: ", transacao.tipo)
            print("Valor: ", transacao.valor)
            print("-----------")
        print("Saldo atual: R$", self.saldo)
        
        print("\nAperte ENTER para voltar ao menu")
        sys.stdin.readline()

    