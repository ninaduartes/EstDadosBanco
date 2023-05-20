import datetime

class Transacao:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor
        self.data_hora = datetime.datetime.now()  # Obtém a data e hora atual

