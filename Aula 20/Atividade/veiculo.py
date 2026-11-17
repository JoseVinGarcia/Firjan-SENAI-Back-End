# Função para pedir os dados
def inserir_dados():
    litros = 0
    modelo = input("Insira o modelo do Carro: ")
    distancia = float(input("Insira a quantidade de Km percorridos: "))
    while litros == 0:
        try:
            litros = float(input("Insira a quantidade de litros de combustível usado: "))
            if litros == 0:
                print("Impossível o gasto ser de 0 litros!")
        except ValueError:
            print("Valor inválido!")
    
    return modelo, distancia, litros

class Veiculo():
    def __init__(self,nome):
        self.nome = nome

    def registrar_dados(self,km,litros):
        self.km = km
        self.litros = litros

    def calcular_consumo(self,km,litros):
        consumo = self.km/self.litros
        return consumo

    def verificar_meta(self,consumo,meta):
        if consumo >= meta:
            return True
        else:
            return False

    def exibir_resumo(self,nome,km,litros,consumo):
        print(f"Modelo do carro: {nome}, distância percorrida: {km}Km, litros gastos: {litros}L, média de consumo: {consumo}Km/L")
