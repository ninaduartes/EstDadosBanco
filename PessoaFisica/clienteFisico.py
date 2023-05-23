from banco import *
class ClienteFisico(Banco):
    def __init__(self):
        super().__init__()
        self.cpf = None
        self.nome = None
        self.telefone = None
        self.endereco = None
        self.cep = None

    def cadastrar_informacoesPF(self, agencia, numBanco, gerente, cpf, nome, telefone, endereco, cep):
        super().cadastrar_informacoes(agencia, numBanco, gerente)
        self.cpf = cpf
        self.numBanco = numBanco
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.cep = cep

        
    def exibir_informacoesPF(self):
        super().exibir_informacoes()
        print("CPF:", self.cpf)
        print("Banco:", self.numBanco)
        print("Nome completo:", self.nome)
        print("Telefone:", self.telefone)
        print("Endereco:", self.endereco)
        print("CEP:", self.cep)

    
    