class Usuario:
    usuarios = []
    def __init__(self, cpf):
        for usuario in Usuario.usuarios:
            if usuario.cpf == cpf:
                raise ValueError("CPF já cadastrado.")
        self.cpf = cpf
        self.nome = input("Digite o nome do usuário: ")
        self.data_nascimento = input("Digite a data de nascimento do usuário (dd/mm/aaaa): ")
        self.endereco = input("Digite o endereço do usuário (logradouro, número, bairro, cidade/estado): ")
        Usuario.usuarios.append(self)

class ContaBancaria:
    contas = []
    numero_conta_atual = 1  # Atributo de classe para rastrear o número da próxima conta a ser criada
    limite_saque_diario = 3  # Limite de saques diários
    limite_valor_saque = 500  # Limite de valor de saque por transação
    
    def __init__(self, usuario, agencia="0001"):
        self.usuario = usuario
        self.agencia = agencia
        self.numero_conta = ContaBancaria.numero_conta_atual
        ContaBancaria.numero_conta_atual += 1  # Atualiza o número da próxima conta a ser criada
        self.saldo = 0.00
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0  # Inicializa o número de saques diários realizados
        self.saldo_diario_saque = 0.00  # Inicializa o saldo diário de saques
        ContaBancaria.contas.append(self)

    def deposito(self, valor, numero_conta):
        conta = self.encontrar_conta(numero_conta)
        if conta:
            if valor > 0:
                conta.saldo += valor
                conta.depositos.append(valor)
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso na conta {conta.numero_conta}.")
                return conta.saldo, conta.depositos
            else:
                print("Valor inválido para depósito.")
                return conta.saldo, conta.depositos
        else:
            print("Conta destino não encontrada.")
            return None, None

    def saque(self, valor, numero_conta):
        conta = self.encontrar_conta(numero_conta)
        if conta:
            if valor > 0 and valor <= self.limite_valor_saque:  
                if conta.saques_diarios < self.limite_saque_diario:
                    if conta.saldo_diario_saque + valor <= self.limite_valor_saque * self.limite_saque_diario:
                        if conta.saldo >= valor:
                            conta.saldo -= valor
                            conta.saques.append(valor)
                            conta.saques_diarios += 1
                            conta.saldo_diario_saque += valor
                            print(f"Saque de R$ {valor:.2f} realizado com sucesso na conta {conta.numero_conta}.")
                            return conta.saldo, conta.saques
                        else:
                            print("Saldo insuficiente para saque.")
                            return conta.saldo, conta.saques
                    else:
                        print("Limite diário de valor de saque excedido.")
                        return conta.saldo, conta.saques
                else:
                    print("Limite diário de saques atingido.")
                    return conta.saldo, conta.saques
            else:
                print("Valor inválido para saque.")
                return conta.saldo, conta.saques
        else:
            print("Conta origem não encontrada.")
            return None, None

    def extrato(self, numero_conta):
        conta = self.encontrar_conta(numero_conta)
        if conta:
            if not conta.depositos and not conta.saques:
                print("\n=========== Extrato ===========\n Não foram realizadas movimentações.\n=================================")
            else:
                print("\n=========== Extrato ===========")
                for dep in conta.depositos:
                    print(f"Depósito: R$ {dep:.2f}")
                for saq in conta.saques:
                    print(f"Saque: R$ {saq:.2f}")
                print(f"Saldo atual: R$ {conta.saldo:.2f}")
                print("=================================")
                return conta.saldo, conta.saques
        else:
            print("Conta não encontrada.")
            return None, None

    def encontrar_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                return conta
        return None

def listar_contas():
    if ContaBancaria.contas:
        for conta in ContaBancaria.contas:
            print(f"Agência: {conta.agencia}, Número da Conta: {conta.numero_conta}, Usuário: {conta.usuario.nome}")
    else:
        print("Nenhuma conta foi criada ainda.")

def criar_usuario():
    cpf = input("Digite o CPF do usuário (apenas números): ")
    try:
        usuario = Usuario(cpf)
        return usuario
    except ValueError as e:
        print(e)

def exibir_menu():
    print("\nMENU:")
    print("[C] - Criar Usuário")
    print("[D] - Depositar")
    print("[S] - Sacar")
    print("[E] - Extrato")
    print("[L] - Listar Contas")
    print("[Q] - Sair")

conta = None

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ").upper()

    if opcao == "C":
        usuario = criar_usuario()
        conta = ContaBancaria(usuario)
    elif opcao == "D":
        if conta:
            numero_conta_destino = int(input("Digite o número da conta para depositar: "))
            valor_deposito = float(input("Digite o valor do depósito: "))
            conta.deposito(valor_deposito, numero_conta_destino)
        else:
            print("Nenhuma conta selecionada. Crie um usuário e uma conta primeiro.")
    elif opcao == "S":
        if conta:
            valor_saque = float(input("Digite o valor do saque: "))
            numero_conta_origem = int(input("Digite o número da conta para sacar: "))
            conta.saque(valor_saque, numero_conta_origem)
        else:
            print("Nenhuma conta selecionada. Crie um usuário e uma conta primeiro.")
    elif opcao == "E":
        if conta:
            numero_conta_extrato = int(input("Digite o número da conta para ver o extrato: "))
            conta.extrato(numero_conta_extrato)
        else:
            print("Nenhuma conta selecionada. Crie um usuário e uma conta primeiro.")
    elif opcao == "L":
        listar_contas()
    elif opcao == "Q":
        print("Programa finalizado.")
        break
    else:
        print("Opção inválida. Escolha C, D, S, E, L ou Q.")
