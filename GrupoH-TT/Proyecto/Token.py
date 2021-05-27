import pygame

import Tablero

class Token:
    cartaAsignada = None
    def __init__(self, Nombre, Icono, Movimiento, Efecto, PuntajeMax, Terreno, Rect):

        self.Nombre = Nombre
        self.Icono = Icono
        self.Movimiento = Movimiento
        self.Efecto = Efecto
        self.PuntajeMax = PuntajeMax
        self.TerrenoFavorable = Terreno
        self.r = pygame.Rect
        self.Posicion = None
        self.Seleccionado = False

    def pintarCasillas(self, casilla, screen):
        print("Flag Mover")
        Esperar = True
        while Esperar:
            pos_Tok_X , pos_Tok_Y = casilla.pos
            for i in range (self.Movimiento):
                pygame.draw.rect(screen, (0,127,0), Tablero.tablero_Hash[(pos_Tok_X + i,pos_Tok_Y + i)].r)

    def efecto():
        pass