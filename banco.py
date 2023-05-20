
class Banco:
    def __init__(self):
        self.agencia = None
        self.numBanco = None
        self.gerente = None

    def cadastrar_informacoes(self, agencia, numBanco, gerente):
        self.agencia = agencia
        self.numBanco = numBanco
        self.gerente = gerente

    def exibir_informacoes(self):
        print("Agência: ", self.agencia)
        print("Banco: ", self.numBanco)
        print("Gerente: ", self.gerente)