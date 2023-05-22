from banco import *
import sys


class ClienteJuridico(Banco):
    def __init__(self):
        super().__init__()
        self.cnpj = None
        self.nome = None
        self.telefone = None
        self.endereco = None
        self.cep = None

    def cadastrar_informacoesPJ(self, agencia, numBanco, gerente, cnpj, nome, telefone, endereco, cep):
        super().cadastrar_informacoes(agencia, numBanco, gerente)
        self.cnpj = cnpj
        self.numBanco = numBanco
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.cep = cep


    def exibir_informacoesPJ(self):
        super().exibir_informacoes()
        print("CNPJ:", self.cnpj)
        print("Banco:", self.numBanco)
        print("Nome empresa:", self.nome)
        print("Telefone:", self.telefone)
        print("Endereco:", self.endereco)
        print("CEP:", self.cep)
    
    