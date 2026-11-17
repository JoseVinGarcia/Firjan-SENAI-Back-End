# AULA 04
# ATIVIDADE 10
print("ATIVIDADE 10")

from Operacoes import situacao

alunos = [
    ["João", 22, 3.5],
    ["Elisa", 19, 8],
    ["Sandro", 24, 6.7]
]

id = -1
opt = -1

while opt != 0:
    print("1 – Mostrar todos os participantes")
    print("2 – Consultar um participante pelo índice (0, 1 ou 2)")
    print("0 – Encerrar")

    opt = int(input("Digite sua opção: "))

    if opt == 1:
        for i in range(3):
            nome = alunos[i][0]
            idade = alunos[i][1]
            nota = alunos[i][2]
            situ = situacao(nota)
            print(f"ID: {i}, Nome: {nome}, Idade: {idade}, Nota: {nota}, Situação: {situ}")
    elif opt == 2:
        id = int(input("Digite o ID do aluno que deseja consultar: "))
        if id in (0, 1, 2): # IMPORTANTE - Anotar esse condicional ao invés de usar OR
            nome = alunos[id][0]
            idade = alunos[id][1]
            nota = alunos[id][2]
            situ = situacao(nota)
            print(f"ID: {id}, Nome: {nome}, Idade: {idade}, Nota: {nota}, Situação: {situ}")
        else:
            print('ID inválido')
    elif opt == 0:
        print("Tchau!")
    else:
        print("OPÇÃO INVÁLIDA")
