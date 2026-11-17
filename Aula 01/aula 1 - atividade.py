# AULA 01
# Atividade 01 - Cálculo de altura
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))

if altura >= 1.60:
  print(f"{nome} possui altura igual ou superior a 1.60m.")
else:
  print(f"{nome} possui altura inferior a 1.60m.")



# Atividade 02 - Verificação de Temperatura
cidade = input("Digite o nome da cidade: " )
temperatura = int(input("Digite a temperatura atual: "))

if temperatura >= 25:
  print(f"{cidade} está com temperatura quente.")
else:
  print(f"{cidade} está com temperatura amena.")



# Atividade 03 - Verificação de Pontos
jogador = input("Digite o nome do jogador: ")
pontos = int(input("Digite a quantidade de pontos: "))

if pontos >= 10:
  print(f"{jogador} alcançou a meta de pontos.")
else:
  print(f"{jogador} não alcançou a meta de pontos.")
