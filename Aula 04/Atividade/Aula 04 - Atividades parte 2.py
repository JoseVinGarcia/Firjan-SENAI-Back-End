# AULA 04
# ATIVIDADE 04
print("ATIVIDADE 4")
alunos = [
    ["Maria", 23, 8.0],
    ["João", 40, 7.8],
    ["Ana", 27, 6.5]
]

print(f"Bem vindo! Alunos disponíveis:")
for i in range(3):
    print(alunos[i][0])

nome = input(f"Digite o aluno que deseja verificar a nota e a idade:")

if nome.upper() == "MARIA":
    id_aluno = 0
elif nome.upper() == "JOÃO":
    id_aluno = 1
elif nome.upper() == "ANA":
    id_aluno = 2
else:
    print("Comando inválido!")
    exit()

idade_aluno = alunos[id_aluno][1]
media_aluno = alunos[id_aluno][2]
print(f"A idade do aluno {nome} é {idade_aluno}, e a média foi de {media_aluno}")

# ATIVIDADE 05
print("ATIVIDADE 5")
alunos = [
    ["Steven", 10, 9],
    ["Lorrana", 6, 8],
    ["Sabrina", 7, 5]
]

for i in range(3):
    nome = alunos[i][0]
    n1 = alunos[i][1]
    n2 = alunos[i][2]
    print(f"Nome: {nome}, Nota 1: {n1}, Nota 2: {n2}")

# ATIVIDADE 06
print("ATIVIDADE 6")

from Operacoes import atualizar_nota

alunos = [
    ["Maria", 23, 8.0],
    ["João", 40, 7.8],
    ["Ana", 27, 6.5]
]

notanova = float(input(f"Digite a nota nova da média de {alunos[1][0]}: "))

atualizar_nota(alunos[1],notanova)

print(f"A nova média de {alunos[1][0]} agora é {alunos[1][2]}")
