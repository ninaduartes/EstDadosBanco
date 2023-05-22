import os
from banco import *
from PessoaFisica.cadastroCliente import *
from PessoaFisica.contaFisica import *
from transacoes import *
from PessoaJuridica.contaJuridica import *
from PessoaJuridica.cadastroJuridica import *
# --------------------------------------

# Formulário de cadastro para Banco
def cadastrar_banco():
    print("----- Bem vindo ao sistema bancário criado pela Marina e pela Gabriela -----\n")
    print("----- Gerente, por favor se identifique: -----\n")

    agencia = input("Digite o número da agência: ")
    numBanco = input("Digite o número do banco: ")
    gerente = input("Digite o seu nome completo: ")

    banco = Banco()
    banco.cadastrar_informacoes(agencia, numBanco, gerente)

    return banco

##Cadastra o banco
banco_cadastrado = cadastrar_banco()
print("\nInformações do Banco:")
banco_cadastrado.exibir_informacoes()
clientes = []
clientesPJ = []

##Limpa a tela antes do próximo processo
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

##Menu
def menu_inicial():
    print(f"--> Gerente {banco_cadastrado.gerente}, você está no banco {banco_cadastrado.numBanco} e agência {banco_cadastrado.agencia} <---\n")
    print("[ Escolha em qual tipo conta quer realizar operações ]")
    print("1. Pessoa Física")
    print("2. Pessoa Jurídica")
    print("3. Sair")

#Menu Fisica
def menu_principal():
    print(f"[ Gerente {banco_cadastrado.gerente}, você está no banco {banco_cadastrado.numBanco} e agência {banco_cadastrado.agencia} ]\n")
    print("----- OPÇÕES PARA PESSOA FÍSICA -----")
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Conta")
    print("3. Realizar Depósito")
    print("4. Realizar Saque")
    print("5. Alterar Cadastro do Cliente")
    print("6. Consultar cliente por CPF")
    print("7. Exibir Extrato")
    print("8. Retornar ao menu principal")

#Menu Juridica
def menu_juridica():
    print(f"[ Gerente {banco_cadastrado.gerente}, você está no banco {banco_cadastrado.numBanco} e agência {banco_cadastrado.agencia} ]\n")
    print("----- OPÇÕES PARA PESSOA JURÍDICA -----")
    print("1. Cadastrar Cliente")
    print("2. Cadastrar Conta")
    print("3. Realizar Depósito")
    print("4. Realizar Saque")
    print("5. Alterar Cadastro do Cliente")
    print("6. Consultar cliente por CNPJ")
    print("7. Exibir Extrato")
    print("8. Retornar ao menu principal")

while True:
    print("\n")
    limpar_tela()
    menu_inicial()
    opcao_inicial = input("Escolha uma opção: ")

    ##Fisica
    if opcao_inicial == "1":
        while True:
            print("\n")
            limpar_tela() ##Limpa a tela antes de exibir menu inicial
            menu_principal()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                limpar_tela()
                cpf_cliente = input("Digite CPF para verificar se o cliente já possui uma conta: ")
                cliente_existente = False
                for cliente in clientes:
                    if cliente.cpf == cpf_cliente:
                        cliente_existente = True
                        break

                if cliente_existente:
                    print("Cliente já cadastrado.")
                else:
                    cliente_cadastrado = cadastrar_cliente_fisico(banco_cadastrado)
                    cliente_cadastrado.cpf = cpf_cliente
                    clientes.append(cliente_cadastrado)
                    print("\nInformações do Cliente Físico:")
                    cliente_cadastrado.exibir_informacoesPF()

            elif opcao == "2":
                if len(clientes) > 0:
                    cpf_cliente = input("\nDigite o CPF do cliente: ")
                    cliente_encontrado = None
                    for cliente in clientes:
                        if cliente.cpf == cpf_cliente:
                            cliente_encontrado = cliente
                            break

                    if cliente_encontrado is not None:
                        conta_cadastrada = cadastrar_conta_fisica(cliente_encontrado)
                        cliente_encontrado.conta_fisica = conta_cadastrada
                        print("\nInformações da Conta Física:")
                        conta_cadastrada.exibir_informacoesPF()
                    else:
                        print("Erro: CPF do cliente não encontrado.")
                else:
                    print("Erro: É necessário cadastrar um Cliente Físico primeiro.")
                    
            elif opcao == "3":
                limpar_tela()
                if len(clientes) > 0:
                    cpf_cliente = input("\nDigite o CPF do cliente: ")
                    cliente_encontrado = None
                    for cliente in clientes:
                        if cliente.cpf == cpf_cliente:
                            cliente_encontrado = cliente
                            break

                    if cliente_encontrado is not None:
                        realizar_deposito(cliente_encontrado)
                    else:
                        print("Erro: CPF do cliente não encontrado.")
                else:
                    print("Erro: É necessário cadastrar um Cliente Físico primeiro.")

            elif opcao == "4":
                limpar_tela()
                if len(clientes) > 0:
                    cpf_cliente = input("\nDigite o CPF do cliente: ")
                    cliente_encontrado = None
                    for cliente in clientes:
                        if cliente.cpf == cpf_cliente:
                            cliente_encontrado = cliente
                            break

                    if cliente_encontrado is not None:
                        realizar_saque(cliente_encontrado)
                    else:
                        print("Erro: CPF do cliente não encontrado.")
                else:
                    print("Erro: É necessário cadastrar um Cliente Físico primeiro.")

            elif opcao == "5":
                limpar_tela()
                alterar_cadastro_cliente(clientes)

            elif opcao == "6":
                limpar_tela()
                print("\n[ Consulta de cliente por CPF ]")
                cpf_consulta = input("\nDigite o CPF do cliente a ser consultado: ")
                consultar_cliente_por_cpf(clientes, cpf_consulta)

            elif opcao == "7":
                limpar_tela()
                exibir_extrato(clientes)


            elif opcao == "8":
                limpar_tela()
                break

            else:
                print("Opção inválida. Tente novamente.")
    
    ##Juridica
    elif opcao_inicial == "2":
        while True:
            print("\n")
            menu_juridica()
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                cnpj_clientePJ = input("Digite CNPJ para verificar se a empresa já possui uma conta: ")
                clientePJ_existente = False
                for clientePJ in clientesPJ:
                    if clientePJ.cnpj == cnpj_clientePJ:
                        clientePJ_existente = True
                        break

                if clientePJ_existente:
                    print("Cliente já cadastrado.")
                else:
                    clientePJ_cadastrado = cadastrar_cliente_juridico(banco_cadastrado)
                    clientePJ_cadastrado.cnpj = cnpj_clientePJ
                    clientesPJ.append(clientePJ_cadastrado)
                    print("\nInformações do Cliente Jurídico:")
                    clientePJ_cadastrado.exibir_informacoesPJ()

            elif opcao == "2":
                if len(clientesPJ) > 0:
                    cnpj_clientePJ = input("\nDigite o CNPJ do cliente: ")
                    clientePJ_encontrado = None
                    for clientePJ in clientesPJ:
                        if clientePJ.cnpj == cnpj_clientePJ:
                            clientePJ_encontrado = clientePJ
                            break

                    if clientePJ_encontrado is not None:
                        contaPJ_cadastrada = cadastrar_conta_juridica(clientePJ_encontrado)
                        clientePJ_encontrado.conta_juridica = contaPJ_cadastrada
                        print("\nInformações da Conta Física:")
                        contaPJ_cadastrada.exibir_informacoesPJ()
                    else:
                        print("Erro: CNPJ do cliente não encontrado.")
                else:
                    print("Erro: É necessário cadastrar um Cliente Jurídico primeiro.")

            elif opcao == "3":
                if len(clientesPJ) > 0:
                    cnpj_clientePJ = input("\nDigite o CNPJ do cliente: ")
                    clientePJ_encontrado = None
                    for clientePJ in clientesPJ:
                        if clientePJ.cnpj == cnpj_clientePJ:
                            clientePJ_encontrado = clientePJ
                            break

                    if clientePJ_encontrado is not None:
                        realizar_deposito_juridica(clientePJ_encontrado)
                    else:
                        print("Erro: CNPJ do cliente não encontrado.")
                else:
                    print("Erro: É necessário cadastrar um Cliente Físico primeiro.")

            elif opcao == "4":
                if len(clientesPJ) > 0:
                    cnpj_clientePJ = input("\nDigite o CNPJ do cliente: ")
                    clientePJ_encontrado = None
                    for clientePJ in clientesPJ:
                        if clientePJ.cnpj == cnpj_clientePJ:
                            clientePJ_encontrado = clientePJ
                            break

                    if clientePJ_encontrado is not None:
                        realizar_saque_juridica(clientePJ_encontrado)
                    else:
                        print("Erro: CNPJ do cliente não encontrado.")
                else:
                    print("Erro: É necessário cadastrar um Cliente Jurídico primeiro.")

            elif opcao == "5":
                alterar_cadastro_cliente_juridico(clientesPJ)

            elif opcao == "6":
                print("\n[ Consulta de cliente por CNPJ ]")
                cnpj_consulta = input("\nDigite o CNPJ do cliente a ser consultado: ")
                consultar_cliente_por_cnpj(clientesPJ, cnpj_consulta)

            elif opcao == "7":
                exibir_extrato_juridica(clientesPJ)


            elif opcao == "8":
                break

            else:
                print("Opção inválida. Tente novamente.")
    
    elif opcao_inicial =="3":
        print("Você saiu do sistema!")
        break

    else:
        print("Opção inválida. Tente novamente.")
