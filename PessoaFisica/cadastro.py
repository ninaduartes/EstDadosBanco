from PessoaFisica.clienteFisico import *
from banco import *
from PessoaFisica.contaFisica import *
from transacoes import *




# Formulário de cadastro para ClienteFisico
def cadastrar_cliente_fisico(banco):
    print("\n[ Dados do cliente ]")
    cpf = input("\nDigite novamente o CPF: ")
    nome = input("Nome completo: ")

    cliente = ClienteFisico()
    cliente.cadastrar_informacoes(banco.agencia, banco.numBanco, banco.gerente, cpf, nome)

    return cliente



# Formulário de cadastro para ContaFisica
def cadastrar_conta_fisica(cliente):
    print("\n[ Digite os dados para abertura de conta ]")
    tipo_conta = input("Digite o tipo de conta (especial/corrente): ")
    saldo = float(input("Digite o saldo inicial: R$"))

    conta_fisica = ContaFisica()
    conta_fisica.cadastrar_informacoes(cliente, tipo_conta, saldo)

    return conta_fisica


def realizar_deposito(cliente):
    valor_deposito = float(input("Digite o valor do depósito: "))
    cliente.conta_fisica.depositar(valor_deposito)

def realizar_saque(cliente):
    valor_saque = float(input("Digite o valor do saque: "))
    cliente.conta_fisica.sacar(valor_saque)


def exibir_extrato(clientes):
    if len(clientes) > 0:
        cpf_cliente = input("\nDigite o CPF do cliente: ")
        cliente_encontrado = None
        for cliente in clientes:
            if cliente.cpf == cpf_cliente:
                cliente_encontrado = cliente
                break

        if cliente_encontrado is not None:
            cliente_encontrado.conta_fisica.exibir_extrato()
        else:
            print("Erro: CPF do cliente não encontrado.")
    else:
        print("Erro: É necessário cadastrar um Cliente Físico primeiro.")

def alterar_cadastro_cliente(clientes):
    cpf_cliente = input("\nDigite o CPF do cliente a ser alterado: ")
    cliente_encontrado = None

    for cliente in clientes:
        if cliente.cpf == cpf_cliente:
            cliente_encontrado = cliente
            break

    if cliente_encontrado is not None:
        novo_nome = input("Digite o novo NOME do cliente (deixe em branco para manter o valor atual): ")
        novo_agencia = input("Digite a nova AGÊNCIA do cliente (deixe em branco para manter o valor atual): ")
        novo_numBanco = input("Digite o novo BANCO do cliente (deixe em branco para manter o valor atual): ")
        novo_gerente = input("Digite o novo GERENTE do cliente (deixe em branco para manter o valor atual): ")
        novo_tipo_conta = input("Digite o novo TIPO DE CONTA (especial/corrente) (deixe em branco para manter o valor atual): ")

        if novo_nome:
            cliente_encontrado.nome = novo_nome

        if novo_agencia:
            cliente_encontrado.agencia = novo_agencia
        
        if novo_numBanco:
            cliente_encontrado.numBanco = novo_numBanco

        if novo_gerente:
            cliente_encontrado.gerente = novo_gerente

        if novo_tipo_conta:
            cliente_encontrado.conta_fisica.tipoConta = novo_tipo_conta

        print("Cadastro do cliente atualizado com sucesso.")
        print("Novas informações do cliente:")
        cliente_encontrado.exibir_informacoes()
    else:
        print("Erro: CPF do cliente não encontrado.")

def consultar_cliente_por_cpf(clientes, cpf):
    cliente_encontrado = None

    for cliente in clientes:
        if cliente.cpf == cpf:
            cliente_encontrado = cliente
            break

    if cliente_encontrado is not None:
        print("Cliente encontrado:")
        cliente_encontrado.exibir_informacoes()
    else:
        print("Cliente não encontrado.")