class Vendedor():
    def __init__(self, nome):
        self.nome = nome
    def vendeu(self, vendas):
        self.vendas = vendas
        
    def valorMeta(self, meta):
        if self.vendas > meta:
            print(self.nome,"GANHOU BONUS")
        else:
            print(self.nome, "NÃO GANHOU BONUS")
