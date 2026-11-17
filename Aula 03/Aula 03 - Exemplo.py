# Aula 03 - Exemplo

frutas = []

frutas.append("Maçã")
frutas.append("Uva")
frutas.append("Abacate")
print(f"Lista: {frutas}")

frutas.sort() # Ordena os elementos dentro do Array
print(f"Lista ordenada: {frutas}")

frutas.pop(1) # Remove o item de índice 1 (Uva)
frutas.insert(1,"Melancia") # Adiciona item no índice 1
print(f"Lista sem o índice 1: {frutas}")

frutas.insert(0,"Abacate")
c = frutas.count("Abacate")
print(c) #Conta quantas ocorrencias do tipo Abacate tem

frutas.clear() # Esvazia a lista
print(frutas)

total = len(frutas) # calcula o tamanho da lista
print(total)
