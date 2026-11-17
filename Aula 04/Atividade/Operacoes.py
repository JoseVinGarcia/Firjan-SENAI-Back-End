# ATIVIDADE AULA 04 - FUNÇÕES

# ATIVIDADE 01
def calcular_total(preco, quantidade):
    return preco * quantidade

# ATIVIDADE 02
def somar(a,b):
    return a + b

def diminuir(a,b):
    return a - b

# ATIVIDADE 03
def calcular_media(nota1, nota2):
    return ((nota1 + nota2)/2)

# Atividade 06
def atualizar_nota(aluno,nota):
    aluno.append(nota)
    aluno.pop(2)

# Atividade 10
def situacao(nota):
    if nota >= 6.0:
        return "Aprovado"
    else:
        return "Reprovado"
