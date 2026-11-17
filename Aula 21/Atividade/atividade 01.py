# Atividade 01

from bonificacao import Vendedor, Gerente

NumeroVendor = int(input("São quantos vendedores? "))

# Calcula nome de vendedores
for i in range(NumeroVendor):
    print(f"Entre com os dados a baixo do {i+1}º Vendedor")

    nome = input("Nome: ")
    salario = float(input("Me diga o valor do seu salário: "))
    vendas = float(input(f"Qual valor das suas vendas {nome}?: "))
    meta = float(input("Me diga o valor de meta que voce precisa bater?: "))    
    
    vendedor1 = Vendedor(nome, salario)
    vendedor1.vendeu(vendas)
    vendedor1.valorMeta(meta)

# Calcula o bonus do gerente
print("\nAgora vamos ao cálculo do gerente...")

for i in range(1):
    print(f"Entre com os dados a baixo do gerente:")

    nome_g = input("Nome: ")
    salario_g = float(input("Me diga o valor do seu salário: "))
    vendas_g = float(input(f"Qual valor total das vendas da equipe: "))
    meta_g = float(input("Me diga o valor de meta que voce precisa bater?: "))    
    
    gerente = Gerente(nome_g, salario_g)
    gerente.vendas_equipe(vendas_g)
    gerente.avaliarEquipe(meta_g)
