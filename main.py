import csv
from operacoes import deposito, saque, extrato

def main():
    nome = input("Bem vindo ao Banco Dio! Por favor, informe seu nome de cadastro: ")
    nome = nome.casefold()
    senha = ""
    saldo = 0
    operacao = ""
    nome_esta_no_csv = 0
    senha_esta_no_csv = 0

    with open("usuarios.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader) #Pula o header do csv file

        for row in csv_reader:
            if nome in row:
                nome_esta_no_csv = 1
                senha = input("Agora, digite sua senha de cadastro: ")
                break

        if nome_esta_no_csv == 0:
            print("Parece que voce ainda nao esta registrado...")
            novo_nome = input("Por favor, digite o nome do novo cadastro: ")
            nova_senha = input("Agora digite a nova senha, por favor: ")

            with open("usuarios.csv", "a", newline = "\n") as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow([novo_nome, nova_senha, 0.0])
                nome = novo_nome
                senha = nova_senha
            
    with open("usuarios.csv", "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)

        for row in csv_reader:
            if senha in row and row[0] == nome:
                print(f"Bem vindo de volta {nome}!")
                saldo = float(row[2])
                operacao = input("Selecione uma operação (D = deposito; S = saque; E = extrato; Q = sair): ")
                senha_esta_no_csv = 1
                break
        
    if senha_esta_no_csv == 0:
        print("Parece que vc errou sua senha... Por favor, tente novamente")
    else:
        extrato = [] #Armazena os logs do extrato
        operacao = operacao.casefold()
        saque_diario = 0 #Armazena a quantidade de saques diários do usuário

        while operacao != "q":
            match operacao:
                case "d":
                    quantidade = float(input("Digite a quantidade de dinheiro que quer depositar: "))
                    
                    if quantidade > 0:
                        #Adiciona o log de depósito no extrato
                        extrato.append(deposito(nome, saldo, quantidade))
                        
                        #Atualiza o saldo do usuário
                        with open("usuarios.csv", "r") as csv_file:
                            csv_reader = csv.reader(csv_file)
                            for row in csv_reader:
                                if nome in row:
                                    saldo = float(row[2])
                    else: 
                        print("Valor de deposito deve ser positivo. Por favor, tente novamente.")
                case "s":
                    quantidade = float(input("Digite a quantidade de dinheiro que quer sacar da conta: "))

                    if quantidade <= 0:
                        print("Valor de saque inválido. Por favor, tente novamente.")     
                    elif saldo < quantidade:
                        print("Saldo insuficiente para saque.")
                    elif quantidade > 500:
                        print("Valor para saque inválido. Por favor, tente novamente.")
                    elif saque_diario > 2:
                        print("Limite de saque diario alcancado.")
                    else:
                        #Adiciona o log de saque no extrato
                        extrato.append(saque(nome, saldo, quantidade))

                        #Atualiza o saldo do usuário
                        with open("usuarios.csv", "r") as csv_file:
                            csv_reader = csv.reader(csv_file)
                            for row in csv_reader:
                                if nome in row:
                                    saldo = float(row[2])
                        #Atualiza a quantidade de saques diários do usuário
                        saque_diario += 1 
                case "e":
                    for log in extrato:
                        print(log)
                    print(f"Seu saldo atual é de R${saldo: .2f}")
            
            operacao = input("Selecione uma operação (D = deposito; S = saque; E = extrato; Q = sair): ").casefold()

if __name__ == "__main__":
    main()