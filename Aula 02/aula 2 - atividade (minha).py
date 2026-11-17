# Aula 2 - Atividade modificada
notas = []

nome = input(f"Digite seu nome: ")
qtdeNotas = int(input(f"Digite quantas notas você deseja calcular: "))

for i in range(qtdeNotas):
    nota = float(input(f"{nome}, digite a {i+1}a nota: "))
    notas.append(nota)
somaNotas = sum(notas)

media = (somaNotas / qtdeNotas)

if media <= 5:
    print(f'Reprovado com a media {media}')
elif media > 5 and media <= 6.9:
    print(f"Recuperação com media {media}")
else:
    print(f"Aprovado com media {media}")
