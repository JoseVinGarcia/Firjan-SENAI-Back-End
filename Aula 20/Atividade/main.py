from veiculo import Veiculo, inserir_dados
import time

# Valores iniciais
carros = []
carrosqtde = int(input("Quantos carros deseja cadastrar? "))
meta = float(input("Defina a meta de KM: "))

# Inserção dos dados
for i in range(carrosqtde):
    # Valores são inseridos em uma função
    modelo,kmp,combustivelL = inserir_dados();

    carro1 = Veiculo(modelo)
    carro1.registrar_dados(kmp,combustivelL)
    consumo = carro1.calcular_consumo(kmp,combustivelL)
    metabatida = carro1.verificar_meta(consumo,meta)
    carro1.exibir_resumo(modelo,kmp,combustivelL,consumo)
    
    if metabatida == True:

        texto = f"{modelo} atingiu a meta, com o consumo de {consumo}Km/L"
        carros.append(texto)
    else:
        texto = f"{modelo} não atingiu a meta, com o consumo de {consumo}Km/L"
        carros.append(texto)

# Mostrar os resultados finais
time.sleep(1)
print("\nFINAL:")
for i in range(len(carros)):
    print(carros[i])
