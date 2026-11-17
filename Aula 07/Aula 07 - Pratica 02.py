# Uma escola precisa de um programa que registre as notas de três alunos e informe se cada um atingiu a média 7.
# Desenvolva um programa em Python que:
# 1.	Crie uma lista de listas contendo o nome e a nota de três alunos.
# 2.	Utilize um for para percorrer os registros.
# 3.	Exiba o nome e a nota de cada aluno.
# 4.	Utilize uma condição if/else para informar se o aluno foi aprovado ou se precisa melhorar a nota.
# 5.	Ao final, explique como o programa utiliza lista, repetição e condição.
# Você pode utilizar os nomes e as notas abaixo como ponto de partida:
# •	Ana — 8.0
# •	Bruno — 6.5
# •	Carla — 7.0

alunos = [
    ["João", 12, 8.7],
    ["Ana", 12, 8.0],
    ["Elisa", 14, 6],
    ["Bruno", 13, 6.5],
    ["Kelly", 11, 5.4],
    ["Carla", 13, 7.0]
]

for aluno in alunos:
    nome = aluno[0]
    nota = aluno[2]

    print(f"Nome: {nome}, Nota: {nota}")

    if nota >= 6:
        print("Situação: Aprovado")
    else:
        print("Situação: Reprovado")
    