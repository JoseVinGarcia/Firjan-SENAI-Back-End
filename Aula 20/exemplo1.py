from bonificacao import Vendedor

NumeroVendor = int(input("São quantos vendedores? "))

for i in range(NumeroVendor):
    print(f"Entre com os dados a baixo do {i+1}º Vendedor")

    nome = input("Nome: ")
    vendas = float(input(f"Qual valor das suas vendas {nome}?: "))
    meta = float(input("Me diga o valor de meta que voce precisa bater?: "))
    
    
    
    vendedor1 = Vendedor(nome)
    vendedor1.vendeu(vendas)
    vendedor1.valorMeta(meta)

