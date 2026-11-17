# AULA 05 - Atividade

# ATIVIDADE 01
print('ATIVIDADE 01')

pessoas = {}

pessoas["Nome"] = input("Insira seu nome: ")
pessoas["Idade"] = input("Digite sua idade: ")

print(pessoas)

# ATIVIDADE 02
print('ATIVIDADE 02')

alunos = {}

alunos["Nome"] = input("Insira seu nome: ")
alunos["Nota"] = float(input("Digite sua nota: "))

print(alunos)

# ATIVIDADE 03
print('ATIVIDADE 03')

produto = {
    "Nome" : "Banana",
    "Descrição" : "Fruta",
    "Preço" : 15
}

print(produto)

# ATIVIDADE 04
print('ATIVIDADE 04')

alunos = []

for i in range(3):
    nome = input(f"Digite o nome do {i+1} aluno: ")
    idade = int(input(f"Digite a idade do {i+1} aluno: "))
    nota = float(input(f"Digite a média do {i+1} aluno: "))

    registro = {"nome": nome, "idade": idade, "nota": nota}
    alunos.append(registro)

print(alunos)
