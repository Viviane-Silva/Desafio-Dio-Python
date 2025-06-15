#sistema bancário simples

saldo = 0.0
saques_realizados = 0
limite_saques = 3           # Máximo de 3 saques por dia
limite_valor_saque = 500.0  # Máximo de R$ 500 por saque

def exibir_menu():
    print("\n===Banco Virtual===")
    print("1 - Consultar saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

def consultar_saldo(saldo):
    print(f"Seu saldo atual é: R$ {saldo:.2f}")

def depositar(saldo):
    try:
        valor = float(input("Digite o valor para depósito: R$ "))
        if valor <=0:
            print("! Valor inválido.")
        else:
            saldo += valor
            print(f"\n Depósito realizado com sucesso!")
            print(f"Saldo atual: R$ {saldo:.2f}")
    except ValueError:
        print("! Operação falhou.")
    return saldo

def sacar(saldo, saques_realizados, limite_saques, limite_valor_saque):
    if saques_realizados >= limite_saques:
        print("! Limite diário de saques atingido. Tente novamente amanhã.")
        return saldo, saques_realizados
    
    try:
        valor = float(input("Digite um valor para saque: R$ "))
        if valor <= 0:
            print(f"Valor inválido.")
        elif valor > limite_valor_saque:
            print(f"! Valor máximo permitido por saque é R$: {limite_valor_saque:.2f}")
        elif valor > saldo:
            print("! Saldo insuficiente.")
        else:
            saldo -= valor 
            saques_realizados +=1
            print("\n Saque realizado com sucesso")
            print(f"Saldo atual: R${saldo:.2f}")
    except ValueError:
        print("! Operação falhou.")
    return saldo, saques_realizados
    
def iniciar_banco():
    saldo = 0.0
    saques_realizados = 0
    limite_saques = 3           
    limite_valor_saque = 500.0  

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            consultar_saldo(saldo)
        elif opcao == "2":
            saldo = depositar(saldo)
        elif opcao == "3":
            saldo, saques_realizados = sacar(saldo, saques_realizados, limite_saques, limite_valor_saque)
        elif opcao == "4":
            print("Obrigado por utilizar nosso banco! ")
            break
        else:
            print("! Opção inválida. Tente novamente.")

# Iniciar o programa
iniciar_banco()