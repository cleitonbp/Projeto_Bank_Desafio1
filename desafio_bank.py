

#Sistema Bank com Python

print("Bem Vindo ao Bank Python! Sua jornada inicia aqui!" )

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
==>
"""
saldo = 0
limite = 500
extrato = ""
num_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informar o valor do Depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"{valor:.2f}"
            print(f"Relizado o depósito de R$ {valor}")
        else:
            print("Operação Falhou!!!")

    elif opcao == "s":

        valor = float(input("Informar o valor de saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = num_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Sem saldo o suficiente")
        elif excedeu_limite:
            print("Sem limite o suficiente")
        elif excedeu_saque:
            print("Execedeu o saque diario")
        elif valor > 0:

            saldo -= valor
            num_saques = 1
            extrato += f"{valor:.2f}"
            print(f"Relizado o Saque de R$ {valor}")
        else:
            print("Operacao Falhou")
            break

    elif opcao == "e":
      
            print(f"Extrao da conta de R$ {saldo:.2f}")

    elif opcao == "q":
        print("Sair")
        break
    else:
        print("Operacao inválida, por favor selecione novamente a operaão desejada.")