import pygame


from Carta import *
from Token import *



OsoPolar = ["oso", pygame.image.load("Imagenes/LogosAnimales/polar-bear.png"), 2,"",10, ["Normal","Agua"], None]
Gaviota = ["gaviota", pygame.image.load("Imagenes/LogosAnimales/gaviota.png"), 4,"",10, ["Normal","Agua","Bosque"], None]
Pinguino = ["pungüino", pygame.image.load("Imagenes/LogosAnimales/pinguino.png"), 3,"",10, ["Normal","Agua"], None]
Reno = ["reno", pygame.image.load("Imagenes/LogosAnimales/reno.png"), 3,"",10, ["Normal"], None]
Zorro = ["zorro blanco", pygame.image.load("Imagenes/LogosAnimales/zorro-artico.png"), 4, "",10,["Normal","Bosque"], None]

imgOso = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Imagenes/ImgCartas/Carta_Oso.png"), (40, 80)), 90)
imgPinguino = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Imagenes/ImgCartas/Carta_Pinguino.png"), (40, 80)), 90)
imgGaviota = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Imagenes/ImgCartas/Carta_Gaviota.png"), (40, 80)), 90)
imgReno = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Imagenes/ImgCartas/Carta_Reno.png"), (40, 80)), 90)
imgZorro = pygame.transform.rotate(pygame.transform.scale(pygame.image.load("Imagenes/ImgCartas/Carta_Zorro.png"), (40, 80)), 90)

# Crea mazo

mazoPolar = []

for i in range(4):
    mazoPolar.append(Carta("oso polar", imgOso, crea_token("oso"),"",""))
    mazoPolar.append(Carta("gaviota", imgGaviota, crea_token("gaviota"),"",""))
    mazoPolar.append(Carta("zorro", imgZorro, crea_token("zorro"),"",""))
    mazoPolar.append(Carta("pingüino", imgPinguino, crea_token("pinguino"),"",""))
    mazoPolar.append(Carta("reno", imgReno, crea_token("reno"),"",""))

