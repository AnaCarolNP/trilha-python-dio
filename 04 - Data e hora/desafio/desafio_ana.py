import datetime

menu = """
Seja bem vindo(a) ao Banco DIO!
Digite a transação que deseja fazer:

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>  """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
transacao = 0
LIMITE_TRANSACAO = 2

while True:

    opcao = input(menu).strip().lower()

    if transacao < LIMITE_TRANSACAO:
    
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            if valor > 0:
                saldo += valor
                data = datetime.datetime.now()          

                extrato += f"Depósito: R$ {valor:.2f}\n Data/Horário: {data.strftime("%d/%m/%Y %H:%M")}\n"

                #if data - datetime.timedelta(days=1) == 0:
                transacao += 1

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            excedeu_saldo = valor > saldo

            excedeu_limite = valor > limite

            excedeu_saques = numero_saques >= LIMITE_SAQUES

            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")

            elif excedeu_limite:
                print("Operação falhou! O valor do saque excede o limite.")

            elif excedeu_saques:
                print("Operação falhou! Número máximo de saques excedido.")

            elif valor > 0:
                saldo -= valor
                data = datetime.datetime.now()
                extrato += f"Saque: R$ {valor:.2f}\n Data/Horário: {data.strftime("%d/%m/%Y %H:%M")}\n"
                numero_saques += 1

            else:
                print("Operação falhou! O valor informado é inválido.")

        elif opcao == "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("==========================================")

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
    
    else:
        print(f"Você excedeu o número de transações diárias, pois já efetuou {transacao} transações.")