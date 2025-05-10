import pandas as pd

def deposito(nome, saldo, quantidade):
    reader = pd.read_csv("usuarios.csv")
    reader.loc[reader["nome"] == nome, "saldo"] += quantidade
    reader.to_csv("usuarios.csv", index = False)

    log = extrato(saldo, quantidade)

    return log
    
def saque(nome, saldo, quantidade):
    reader = pd.read_csv("usuarios.csv")
    reader.loc[reader["nome"] == nome, "saldo"] -= quantidade
    reader.to_csv("usuarios.csv", index = False)

    log = extrato(saldo, quantidade)

    return log

def extrato(saldo, quantidade):
    log = ""
    if quantidade >= 0:
        log = f"No seu saldo de R${saldo: .2f}, foi depositado R${quantidade: .2f}" 
    else:
        log = f"No seu saldo de R${saldo: .2f}, foi sacado R${quantidade: .2f}"

    return log