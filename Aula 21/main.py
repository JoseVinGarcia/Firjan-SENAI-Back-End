class Jogador:
    def __init__(self, altura, velocidade, passe, drible, precisao):
        self.altura = altura
        self.velocidade = velocidade
        self.passe = passe
        self.drible = drible
        self.precisao = precisao

    def passar(self):
        print("Mirar")
        print("Encostar na bola com a força de passe do jogador")

    def chutar(self):
        print("Mirar")
        print("Encostar na bola com 2x a força de passe do jogador")


class Jogador_Goleiro(Jogador):
    def agarrar(self):
        print("Pular")
        print("Se esticar para pegar a bola")


class Jogador_Linha(Jogador):
    pass


# --- Exemplo de uso ---
if __name__ == "__main__":
    # Criando um jogador comum
    jogador_comum = Jogador(1.80, 85, 75, 80, 90)
    print("Ações do Jogador de Linha:")
    jogador_comum.passar()
    jogador_comum.chutar()
    
    print("-" * 30)

    # Criando um goleiro (herdando de Jogador)
    goleiro = Jogador_Goleiro(1.90, 75, 60, 50, 70)
    print("Ações do Goleiro:")
    goleiro.agarrar()
    goleiro.passe = 65  # Pode usar os atributos herdados também
