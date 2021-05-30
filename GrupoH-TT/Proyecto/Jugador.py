import random
import Tablero


class Jugador:

    def roboInicial(self):
        for i in range(5):
            n = random.randint(0, 19 - i)
            self.mano.append(self.mazo.pop(n))

    def robarCarta(self):
        if len(self.mazo) > 0:
            n = random.randint(0, (len(self.mazo) - 1))
            carta = self.mazo.pop(n)
            self.mano.append(carta)
            if self.id == 1:
                for i in range(len(self.mano)):
                    self.mano[i].posicionEnMano = Tablero.ManoPl1[i]
            else:
                for i in range(len(self.mano)):
                    self.mano[i].posicionEnMano = Tablero.ManoPl2[i]

    # def robaCarta(self):
    #     if len(self.Mano) < 5:
    #         n = random.randint(0, 9)
    #         self.Mano.append(self.Mazo[n])
    #         self.Mazo.pop(n)
    #
    def jugarCartas(self, Carta, Casilla):
        Casilla.Contenido = Carta.token
        self.unidadesJugador.append(Carta.token)

    def __init__(self, id, MazoInicial):
        self.id = id
        self.mazo = MazoInicial
        self.mano = []
        self.puntosDeAccion = [3]
        self.puntosDeVictoria = [0]
        self.unidadesJugador = []

