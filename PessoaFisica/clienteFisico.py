from banco import *


class ClienteFisico(Banco):
    def __init__(self):
        super().__init__()
        self.cpf = None
        self.nome = None

    def cadastrar_informacoes(self, agencia, numBanco, gerente, cpf, nome):
        super().cadastrar_informacoes(agencia, numBanco, gerente)
        self.cpf = cpf
        self.numBanco = numBanco
        self.nome = nome

    def exibir_informacoes(self):
        super().exibir_informacoes()
        print("CPF:", self.cpf)
        print("Banco:", self.numBanco)
        print("Nome completo:", self.nome)
    
    