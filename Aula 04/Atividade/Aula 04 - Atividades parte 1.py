# AULA 04
# ATIVIDADE 01
print("ATIVIDADE 1")

from Operacoes import calcular_total

print("Bem vindo!")
item = input("Digite o nome do item que quer calcular: ")
quantidade = int(input("Digite a quantidade que deseja calcular: "))
valor = float(input("Digite o valor do item que deseja calcular: "))

total = calcular_total(valor, quantidade)

print(f"O total do cálculo de {item} é {total}")

# ATIVIDADE 02
print("ATIVIDADE 2")
from Operacoes import somar, diminuir

a = float(input("Digite o primeiro valor para as ações: "))
b = float(input("Digite o segundo valor para as ações: "))

op = input(f"O quê deseja fazer com os valores {a} e {b}? S = somar/D = diminuir:")

if op.upper() == "S":
    resultado = somar(a,b)
elif op.upper() == "D":
    resultado = diminuir(a,b)
else:
    print(f"Opção inválida.")
    exit()

print(f"Resultado é {resultado}")

# ATIVIDADE 03
print("ATIVIDADE 3")
from Operacoes import calcular_media

aluno = input("Digite o nome do aluno: ")
n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))

media = calcular_media(n1,n2)

if media > 6.0:
    print(f"A média do aluno {aluno} é {media}. Aprovado.")
else:
    print(f"A média do aluno {aluno} é {media}. Reprovado.")

