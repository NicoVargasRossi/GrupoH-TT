import pygame

import Tablero

class Token:

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

    def efecto(self):
        pass


def crea_token(tipo):
    if tipo == "oso":
        return Token("oso", pygame.image.load("Imagenes/LogosAnimales/polar-bear.png"), 2,"",10, ["Normal","Agua"], None)
    elif tipo == "gaviota":
        return Token("gaviota", pygame.image.load("Imagenes/LogosAnimales/gaviota.png"), 4,"",10, ["Normal","Agua","Bosque"], None)
    elif tipo == "zorro":
        return Token("zorro", pygame.image.load("Imagenes/LogosAnimales/zorro-artico.png"), 4, "",10,["Normal","Bosque"], None)
    elif tipo == "pinguino":
        return  Token("punguino", pygame.image.load("Imagenes/LogosAnimales/pinguino.png"), 3,"",10, ["Normal","Agua"], None)
    elif tipo == "reno":
        return Token("reno", pygame.image.load("Imagenes/LogosAnimales/reno.png"), 3,"",10, ["Normal"], None)
    elif tipo == "leon":
        return Token("leon", pygame.image.load("Imagenes/LogosAnimales/lion.png"), 3 , "Rugido", 10, ["Normal"], None)
    elif tipo == "cebra":
        return Token("cebra", pygame.image.load("Imagenes/LogosAnimales/zebra.png"),4,"Correr",15,["Normal"],None)
    elif tipo == "mono":
        return Token("mono", pygame.image.load("Imagenes/LogosAnimales/mono.png"),3,"Escabullirse",15,["Normal", "Bosque"],None)
    elif tipo == "tucan":
        return Token("tucan", pygame.image.load("Imagenes/LogosAnimales/tucan.png"),4,"Vuelo rápido",10,["Normal", "Bosque", "Agua"],None)
    elif tipo == "elefante":
        return Token("elefante", pygame.image.load("Imagenes/LogosAnimales/elephant.png"),2,"Inamovible",15,["Normal", "Agua"], None)