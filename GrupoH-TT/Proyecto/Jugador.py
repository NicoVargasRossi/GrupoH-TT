import random

import pygame

import Token
from Token import *
from Carta import *
from Tablero import *

class Jugador:

    PuntosDeAccion = 3
    PuntosDeVictoria = 0
    UnidadesJugador = [Token.Token]
    Mano = [i for i in range(5)]
    Mazo = [i for i in range(20)]

    def roboInicial(self, mazoJugador):
        for i in range(len(self.Mano)):
            n = random.randint(0,19-i)
            self.Mano[i] = self.Mazo[n]
            self.Mazo.pop(n)
        return self.Mano

    def jugarCartas(self, Carta, Casilla):
        Casilla.Contenido = Carta.token
        self.UnidadesJugador.append(Carta.token)


    def __init__(self, MazoInicial):
        self.Mazo = MazoInicial
        self.ManoInicial = Jugador.roboInicial(self, MazoInicial)