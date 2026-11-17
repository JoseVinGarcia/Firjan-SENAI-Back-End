# Aula 03 - Atividade

geladeira = []

print("Olá!")

for i in range(5):
    item = input(f"Insira o nome do {i+1} item: ")
    geladeira.append(item)

print(f"Itens atualmente na geladeira: {geladeira}")

geladeira.sort() # Ordena os elementos dentro do Array
print(f"Lista ordenada: {geladeira}")

geladeira.pop(1) # Remove o item de índice 1 (Uva)

item = input(f"Insira o nome do item que você quer adicionar na geladeira: ")

geladeira.insert(1,item) # Adiciona item no índice 1
print(f"Lista sem o índice 1: {geladeira}")

busca = input(f"Insira o nome do item que você quer procurar na geladeira: ")

c = geladeira.count(busca)
print(f"Tem {c} itens de nome {busca} na geladeira.") #Conta quantas ocorrencias do tipo busca tem

geladeira.clear() # Esvazia a lista
print(geladeira)

total = len(geladeira) # calcula o tamanho da lista
print(total)
