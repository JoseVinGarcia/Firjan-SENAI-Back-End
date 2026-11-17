class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Vendedor(Funcionario):
    def vendeu(self, vendas):
        self.vendas = vendas
        
    def valorMeta(self, meta):
        if self.vendas > meta:
            print(self.nome, "GANHOU BONUS")
        else:
            print(self.nome, "NÃO GANHOU BONUS")

class Gerente(Funcionario):
    def vendas_equipe(self,vendas):
        self.vendas_equipe = vendas
    
    def avaliarEquipe(self, meta_equipe_batida):
        if self.vendas_equipe >= meta_equipe_batida:
            print(f"Meta batida! Parabéns! Bônus de 20% adicionado ao salário.")
        else:
            print(f"Meta não batida! Não haverá bônus.")

