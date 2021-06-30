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

    def __init__(self, id, MazoInicial):
        self.id = id
        self.mazo = MazoInicial
        self.mano = []
        self.puntosDeAccion = [3]
        self.puntosDeVictoria = [0]
        self.unidadesJugador = []
        self.roboInicial()


