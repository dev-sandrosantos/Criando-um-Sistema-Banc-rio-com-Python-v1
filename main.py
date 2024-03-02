class ContaBancaria:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []
        self.saques_diarios = 0

    def deposito(self, valor):        
# Este método permite realizar um depósito na conta. Ele recebe o valor do depósito como argumento:
# Verifica se o valor é positivo.
# Se for, adiciona o valor ao saldo e registra o depósito na lista self.depositos
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def saque(self, valor):
# Esse método de saque permite retirar dinheiro da conta:
# Verifica se o valor é positivo e não ultrapassa o limite de R$ 500,00.
# Verifica se o saldo é suficiente para o saque.
# Se todas as condições forem atendidas, subtrai o valor do saldo, registra o saque na lista self.saques e incrementa o contador de saques diários.
# Caso contrário, exibe mensagens apropriadas.
        if valor > 0 and valor <= 500:
            if self.saldo >= valor:
                if self.saques_diarios < 3:
                    self.saldo -= valor
                    self.saques.append(valor)
                    self.saques_diarios += 1
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                else:
                    print("Limite diário de saques atingido.")
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("Valor inválido para saque.")

    def extrato(self):
# Esse método de extrato lista todas as movimentações (depósitos e saques) realizadas na conta:
# Se não houver movimentações, exibe a mensagem “Não foram realizadas movimentações.”
# Caso contrário, mostra os detalhes de cada depósito e saque, bem como o saldo atual.
        if not self.depositos and not self.saques:
            print("Não foram realizadas movimentações.")
        else:
            print("Extrato:")
            for dep in self.depositos:
                print(f"Depósito: R$ {dep:.2f}")
            for saq in self.saques:
                print(f"Saque: R$ {saq:.2f}")
            print(f"Saldo atual: R$ {self.saldo:.2f}")

# Função para exibir o menu
def exibir_menu():
    print("\nMENU:")
    print("[D] - Depositar")
    print("[S] - Sacar")
    print("[E] - Extrato")
    print("[Q] - Sair")

# Programa principal
conta = ContaBancaria()

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ").upper()

    if opcao == "D":
        valor_deposito = float(input("Digite o valor do depósito: "))
        conta.deposito(valor_deposito)
    elif opcao == "S":
        valor_saque = float(input("Digite o valor do saque: "))
        conta.saque(valor_saque)
    elif opcao == "E":
        conta.extrato()
    elif opcao == "Q":
        print("Programa finalizado.")
        break
    else:
        print("Opção inválida. Escolha D, S, E ou Q.")