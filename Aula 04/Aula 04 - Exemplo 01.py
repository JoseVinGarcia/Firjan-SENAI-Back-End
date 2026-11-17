# AULA 04 - FUNÇÕES
from calculadora import somar, multiplicar

a = float(input("Digite o primeiro valor para as ações: "))
b = float(input("Digite o segundo valor para as ações: "))

op = input(f"O quê deseja fazer com os valores {a} e {b}? M = multiplicar/S = somar:")

if op.upper() == "S":
    resultado = somar(a,b)
elif op.upper() == "M":
    resultado = multiplicar(a,b)
else:
    print(f"Opção inválida.")
    exit()

print(f"Resultado é {resultado}")
