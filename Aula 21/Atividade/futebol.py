class Jogador:
    def __init__(self,nome,altura,velocidade,passe):
        self.nome = nome
        self.altura = altura
        self.velocidade = velocidade
        self.passe = passe

    def passou(self):
        print(f"{self.nome} tocou a bola!")

    def correr(self):
        print(f"{self.nome} está correndo na velocidade {self.velocidade}!")

class JogadorGoleiro(Jogador):
    def agarrar(self):
        print(f"{self.nome} pulou e defendeu o chute!")

class JogadorAtacante(Jogador):
    def finalizar(self):
        print(f"{self.nome} chutou forte para o gol!")

jogador1 = JogadorAtacante("Atacante Azul",1.75,10,2)
jogador2 = JogadorAtacante("Atacante Vermelho",1.80,11,1)
goleiro1 = JogadorGoleiro("Goleiro Azul",1.80,5,3)

jogador2.passou()
jogador1.correr()
jogador2.finalizar()
goleiro1.agarrar()
