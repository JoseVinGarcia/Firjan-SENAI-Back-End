# Aula 2
notas = []

nome = input(f"Digite seu nome: ")

for i in range(3):
    nota = float(input(f"{nome}, digite a {i+1}a nota: "))
    notas.append(nota)
somaNotas = sum(notas)

media = (somaNotas / 3)

if media <= 5:
    print(f'Reprovado com a media {media}')
elif media > 5 and media <= 6.9:
    print(f"Recuperação com media {media}")
else:
    print(f"Aprovado com media {media}")
