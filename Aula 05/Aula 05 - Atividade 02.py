# AULA 05 - Atividade

# ATIVIDADE 05
print('ATIVIDADE 05')

pessoas = []

for i in range(5):
    nome = input(f"Digite o nome da {i+1} pessoa: ")
    idade = int(input(f"Digite a idade da {i+1} pessoa: "))
    cidade = input(f"Digite a cidade da {i+1} pessoa: ")

    registro = {"nome": nome, "idade": idade, "cidade": cidade}
    pessoas.append(registro)

print(pessoas)

# ATIVIDADE 06
print('ATIVIDADE 06')

alunos = [
    {"Nome" : "João", "Idade" : "18", "Nota" : 10},
    {"Nome" : "Elisa", "Idade" : "19", "Nota" : 6},
    {"Nome" : "Thiago", "Idade" : "17", "Nota" : 8.5}
]

opt = -1

while opt!=0:
    print("1. Consultar aluno")
    print("0. Sair")

    opt = int(input("Escolha sua opção: "))

    if opt == 1:
        nome = input("Digite o nome que deseja buscar: ")

        for aluno in alunos: # vai iniciar do 0 ate onde estiver alunos registrados no dicionario alunos
            if aluno["Nome"].lower() == nome.lower():
                print(f"Nome: {aluno['Nome']}, Idade: {aluno['Idade']}, Nota: {aluno['Nota']}")

    elif opt == 0:
        print("Saindo")
        break
    else:
        print("Opção inválida")


# ATIVIDADE 07
print('ATIVIDADE 07')

produtos = []

for i in range(5):
    produto = {}
    produto["Nome"] = input("Digite o nome do produto: ")
    produto["Valor"] = float(input("Digite o valor do produto: "))
    produtos.append(produto)

# Calculo do maior produto
mais_caro = produtos[0] # Começamos do 0, assumindo que é o mais caro

for produto in produtos:
    if produto["Valor"] > mais_caro["Valor"]:
        mais_caro = produto

print(f"O produto mais caro é {mais_caro}")
