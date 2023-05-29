from banco import *
from transacoes import *
from PessoaJuridica.clienteJuridico import *
from PessoaJuridica.contaJuridica import *
import sys

##Formulário de cadastro para ClienteJuridico
def cadastrar_cliente_juridico(banco):
    print("\n[ Dados do cliente ]")
    cnpj = input("\nDigite novamente o CNPJ: ")
    nome = input("Nome da empresa: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço completo (Rua Exemplo, nº12): ")
    cep = input("CEP: ")

    clientePJ = ClienteJuridico()
    clientePJ.cadastrar_informacoesPJ(banco.agencia, banco.numBanco, banco.gerente, cnpj, nome, telefone, endereco, cep)

    print("\nAperte ENTER para voltar ao menu")
    sys.stdin.readline()

    return clientePJ

##Formulario de cadastro para ContaJuridica
def cadastrar_conta_juridica(clientePJ):
    print("\n[ Digite os dados para abertura de conta ]")
    tipo_conta = input("Digite o tipo de conta (especial/corrente): ")
    saldo = float(input("Digite o saldo inicial: R$"))

    conta_juridica = ContaJuridica()
    conta_juridica.cadastrar_informacoesPJ(clientePJ, tipo_conta, saldo)

    return conta_juridica


def realizar_deposito_juridica(clientePJ):
    valor_deposito = float(input("Digite o valor do depósito: R$"))
    clientePJ.conta_juridica.depositarPJ(valor_deposito)

def realizar_saque_juridica(clientePJ):
    valor_saque = float(input("Digite o valor do saque: R$"))
    clientePJ.conta_juridica.sacarPJ(valor_saque)


def exibir_extrato_juridica(clientesPJ):
    if len(clientesPJ) > 0:
        cnpj_clientePJ = input("\nDigite o CNPJ do cliente: ")
        clientePJ_encontrado = None
        for clientePJ in clientesPJ:
            if clientePJ.cnpj == cnpj_clientePJ:
                clientePJ_encontrado = clientePJ
                break

        if clientePJ_encontrado is not None:
            clientePJ_encontrado.conta_juridica.exibir_extratoPJ()
        else:
            print("Erro: CNPJ do cliente não encontrado.")
    else:
        print("Erro: É necessário cadastrar um Cliente Jurídico primeiro.")

def alterar_cadastro_cliente_juridico(clientesPJ):
    cnpj_clientePJ = input("\nDigite o cnpj do cliente que deseja realizar alterações de cadastro:: ")
    clientePJ_encontrado = None

    for clientePJ in clientesPJ:
        if clientePJ.cnpj == cnpj_clientePJ:
            clientePJ_encontrado = clientePJ
            break

    if clientePJ_encontrado is not None:
        novo_nome = input("Digite o novo NOME da empresa (deixe em branco para manter o valor atual): ")
        novo_telefone = input("Digite o novo TELEFONE do cliente (deixe em branco para manter o valor atual): ")
        novo_endereco = input("Digite o novo ENDEREÇO do cliente (deixe em branco para manter o valor atual): ")
        novo_cep = input("Digite o novo CEP do cliente (deixe em branco para manter o valor atual): ")
        novo_agencia = input("Digite a nova AGÊNCIA do cliente (deixe em branco para manter o valor atual): ")
        novo_numBanco = input("Digite o novo BANCO do cliente (deixe em branco para manter o valor atual): ")
        novo_gerente = input("Digite o novo GERENTE do cliente (deixe em branco para manter o valor atual): ")
        novo_tipo_contaJuridica = input("Digite o novo TIPO DE CONTA (especial/corrente) (deixe em branco para manter o valor atual): ")

        if novo_nome:
            clientePJ_encontrado.nome = novo_nome
            
        if novo_telefone:
            clientePJ_encontrado.telefone = novo_telefone
        
        if novo_endereco:
            clientePJ_encontrado.endereco = novo_endereco
        
        if novo_cep:
            clientePJ_encontrado.cep = novo_cep
        
        if novo_agencia:
            clientePJ_encontrado.agencia = novo_agencia
        
        if novo_numBanco:
            clientePJ_encontrado.numBanco = novo_numBanco

        if novo_gerente:
            clientePJ_encontrado.gerente = novo_gerente

        if novo_tipo_contaJuridica:
            clientePJ_encontrado.conta_juridica.tipoConta = novo_tipo_contaJuridica

        print("[ Cadastro do cliente atualizado com sucesso.]\n")
        print("--> Novas informações do cliente: ")
        clientePJ_encontrado.exibir_informacoesPJ()
    else:
        print("Erro: CNPJ do cliente não encontrado.")
    
    print("\nAperte ENTER para voltar ao menu")
    sys.stdin.readline()


def consultar_cliente_por_cnpj(clientesPJ, cnpj):
    clientePJ_encontrado = None

    for clientePJ in clientesPJ:
        if clientePJ.cnpj == cnpj:
            clientePJ_encontrado = clientePJ
            break

    if clientePJ_encontrado is not None:
        print("-----> Cliente encontrado <-----")

        print("\n-----------")
        print(f"Nome: {clientePJ.nome}")
        print(f"CNPJ: {clientePJ.cnpj}")
        print("-----------")

        print("\n-----------")
        print(f"Número da conta: {clientePJ.conta_juridica.numConta}")
        print(f"Banco: {clientePJ.conta_juridica.numBanco}")
        print(f"Agencia: {clientePJ.conta_juridica.agencia}")
        print(f"Gerente: {clientePJ.conta_juridica.gerente}")
        print("-----------")

        print("\n-----------")
        print(f"Telefone: {clientePJ.telefone}")
        print(f"Endereco: {clientePJ.endereco}")
        print(f"CEP: {clientePJ.cep}")
        print("-----------")
    else:
        print("Cliente não encontrado.")
        
    print("\nAperte ENTER para voltar ao menu")
    sys.stdin.readline()
