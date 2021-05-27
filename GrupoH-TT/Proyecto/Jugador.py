import random

import pygame

import Token
from Token import *
from Carta import *
from Tablero import *

class Jugador:

    PuntosDeAccion = 3
    PuntosDeVictoria = 0
    UnidadesJugador = []
    Mano = []
    Mazo = []

    def roboInicial(self):
        for i in range(5):
            n = random.randint(0,19-i)
            self.Mano.append(self.Mazo.pop(n))
        return self.Mano

    # def robaCarta(self):
    #     if len(self.Mano) < 5:
    #         n = random.randint(0, 9)
    #         self.Mano.append(self.Mazo[n])
    #         self.Mazo.pop(n)
#
    def jugarCartas(self, Carta, Casilla):
        Casilla.Contenido = Carta.token
        self.UnidadesJugador.append(Carta.token)


    def __init__(self, id, MazoInicial):
        self.id = id
        self.Mazo = MazoInicial
        self.Mano = self.roboInicial()