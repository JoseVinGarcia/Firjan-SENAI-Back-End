# AULA 04
# ATIVIDADE 07
print("ATIVIDADE 7")

senha = ""
senha_correta = "123"

while senha!=senha_correta:
    senha = input("Senha inválida. Digite a senha correta: ")

print("PARABÉNS, ACESSO LIBERADO!")

# ATIVIDADE 08
print("ATIVIDADE 8")

PIN = ""
PIN_correto = "2026"

PIN = input("Bem vindo! Digite o PIN de acesso: ")

while PIN!=PIN_correto:
    PIN = input("PIN inválido. Digite o correto: ")

print("Cadastro liberado.")

# ATIVIDADE 09
print("ATIVIDADE 9")

opt = -1

# condição normal, só muda que vai ficar dentro do while (com condição definida) - importante
while opt != 0:
    print("Escolha uma das opções:")
    print("1 – Consultar saldo")
    print("2 – Fazer depósito")
    print("0 – Sair")

    opt = int(input("Digite sua opção: "))

    if opt == 1:
        print("Seu saldo é de R$ 0,00")
    elif opt == 2:
        print("Conta zerada para depósito!")
    elif opt == 0:
        print("Tchau!")
    else:
        print("Opção inválida.")

