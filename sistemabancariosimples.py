menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if(opcao == "d"):
        print("Deposito")
        digite_valor = float(input("Digite o valor do deposito: R$ ").replace(",","."))
        
        if(digite_valor > 0):
            saldo = float(saldo) + digite_valor
            extrato = extrato+f"Deposito R$ {digite_valor:.2f}#"
        else:
            print("Valor inválido! Use valor positivo!")
    
    elif(opcao == "s"):
        saque_dia = float(input("Digite o valor do saque em R$ ").replace(",","."))
        
        if((numero_saques <= (LIMITE_SAQUES -1)) and (0 < saque_dia <= limite) and (saque_dia <= saldo)): # LIMITE_SAQUES -1 (0,1,2,3) para 4-1=3
            print(f"Saque R${saque_dia:.2f}")
            numero_saques +=1
            saldo = saldo - saque_dia
            extrato = extrato+f"Saque R$ {saque_dia:.2f}#"

        elif(saque_dia < 0):
            print("Valor inválido! Use valor positivo!")
        elif(saldo < saque_dia <= limite):
            print("Saldo insuficiente!")
        elif(numero_saques >= LIMITE_SAQUES):
            print("Operações de saque indisponivel!")
        else:
            print("Seu limite de Saque é R$500.00!")

    elif(opcao == "e"):
        print("==== Extrato ====")
        for i in extrato.split("#"):
            if(len(extrato) == 0):
                print("Conta sem operações financeiras!\n")
            else:
                print(i)
        print(f"Saldo R$ {saldo:.2f}\n=================")

    elif(opcao == "q"):
        print("Operação Finalizada!")
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
