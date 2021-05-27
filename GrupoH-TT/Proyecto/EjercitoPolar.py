import pygame


from Carta import *
from Token import *

MazoPolar = []

# OsoPolar = ["oso", pygame.image.load("Imagenes/LogosAnimales/polar-bear.png"), 2,"",10, ["Normal","Agua"], None]
# Gaviota = ["gaviota", pygame.image.load("Imagenes/LogosAnimales/gaviota.png"), 4,"",10, ["Normal","Agua","Bosque"], None]
# Pinguino = ["pungüino", pygame.image.load("Imagenes/LogosAnimales/pinguino.png"), 3,"",10, ["Normal","Agua"], None]
# Reno = ["reno", pygame.image.load("Imagenes/LogosAnimales/reno.png"), 3,"",10, ["Normal"], None]
# Zorro = ["zorro blanco", pygame.image.load("Imagenes/LogosAnimales/zorro-artico.png"), 4, "",10,["Normal","Bosque"], None]

# Cartas
for i in range(4):
    MazoPolar.append(Carta("oso polar", pygame.image.load("Imagenes/ImgCartas/Carta_Negra.png"),
                           Token("oso", pygame.image.load("Imagenes/LogosAnimales/polar-bear.png"), 2,"",10, ["Normal","Agua"], None),"",""))
    MazoPolar.append(Carta("gaviota", pygame.image.load("Imagenes/ImgCartas/Carta_Negra.png"),
                           Token("gaviota", pygame.image.load("Imagenes/LogosAnimales/gaviota.png"), 4,"",10, ["Normal","Agua","Bosque"], None),"",""))
    MazoPolar.append(Carta("zorro",pygame.image.load("Imagenes/ImgCartas/Carta_Negra.png"),
                           Token("zorro blanco", pygame.image.load("Imagenes/LogosAnimales/zorro-artico.png"), 4, "",10,["Normal","Bosque"], None),"",""))
    MazoPolar.append(Carta("pingüino",pygame.image.load("Imagenes/ImgCartas/Carta_Negra.png"),
                           Token("pungüino", pygame.image.load("Imagenes/LogosAnimales/pinguino.png"), 3,"",10, ["Normal","Agua"], None),"",""))
    MazoPolar.append(Carta("reno",pygame.image.load("Imagenes/ImgCartas/Carta_Negra.png"),
                           Token("reno", pygame.image.load("Imagenes/LogosAnimales/reno.png"), 3,"",10, ["Normal"], None),"",""))

