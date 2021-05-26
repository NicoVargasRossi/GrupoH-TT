import pygame

import Token

from Token import *
from Carta import *

#Tokens
IconoLeon = pygame.image.load("Imagenes/LogosAnimales/lion.png")
leon1 = Token.Token("leon", IconoLeon, 3 , "Rugido", 10, ["Normal"], None)
leon2 = Token.Token("leon", IconoLeon, 3 , "Rugido", 10, ["Normal"], None)
leon3 = Token.Token("leon", IconoLeon, 3 , "Rugido", 10, ["Normal"], None)
leon4 = Token.Token("leon", IconoLeon, 3 , "Rugido", 10, ["Normal"], None)
IconoCebra = pygame.image.load("Imagenes/LogosAnimales/zebra.png")
cebra1 = Token.Token("cebra", IconoCebra,4,"Correr",15,["Normal"],None)
cebra2 = Token.Token("cebra", IconoCebra,4,"Correr",15,["Normal"],None)
cebra3 = Token.Token("cebra", IconoCebra,4,"Correr",15,["Normal"],None)
cebra4 = Token.Token("cebra", IconoCebra,4,"Correr",15,["Normal"],None)
IconoMono = pygame.image.load("Imagenes/LogosAnimales/mono.png")
mono1 = Token.Token("mono", IconoMono,3,"Escabullirse",15,["Normal", "Bosque"],None)
mono2 = Token.Token("mono", IconoMono,3,"Escabullirse",15,["Normal", "Bosque"],None)
mono3 = Token.Token("mono", IconoMono,3,"Escabullirse",15,["Normal", "Bosque"],None)
mono4 = Token.Token("mono", IconoMono,3,"Escabullirse",15,["Normal", "Bosque"],None)
IconoTucan = pygame.image.load("Imagenes/LogosAnimales/tucan.png")
tucan1 = Token.Token("tucan", IconoTucan,4,"Vuelo rápido",10,["Normal", "Bosque", "Agua"],None)
tucan2 = Token.Token("tucan", IconoTucan,4,"Vuelo rápido",10,["Normal", "Bosque", "Agua"],None)
tucan3 = Token.Token("tucan", IconoTucan,4,"Vuelo rápido",10,["Normal", "Bosque", "Agua"],None)
tucan4 = Token.Token("tucan", IconoTucan,4,"Vuelo rápido",10,["Normal", "Bosque", "Agua"],None)
IconoElefante = pygame.image.load("Imagenes/LogosAnimales/elephant.png")
elefante1 = Token.Token("elefante", IconoElefante,2,"Inamovible",15,["Normal", "Agua"], None)
elefante2 = Token.Token("elefante", IconoElefante,2,"Inamovible",15,["Normal", "Agua"],None)
elefante3 = Token.Token("elefante", IconoElefante,2,"Inamovible",15,["Normal", "Agua"],None)
elefante4 = Token.Token("elefante", IconoElefante,2,"Inamovible",15,["Normal", "Agua"],None)
#Cartas
imgLeon = pygame.image.load("Imagenes/ImgCartas/Carta_Leon.png")
imgLeon = pygame.transform.rotate(pygame.transform.scale(imgLeon, (40, 80)), 90)
efectoCLeon = "Efecto: Una unidad enemiga no puede moverse el siguiente turno"
DULeon = "Habilidad “Rugido” (Una unidad enemiga que se encuentre en una casilla contigua no puede moverse el siguiente turno). Movimiento 3(Terrestre), Puntaje Máximo 10"
cleon1 = Carta("leon",imgLeon,leon1,efectoCLeon, DULeon)
cleon2 = Carta("leon",imgLeon,leon2,efectoCLeon, DULeon)
cleon3 = Carta("leon",imgLeon,leon3,efectoCLeon, DULeon)
cleon4 = Carta("leon",imgLeon,leon4,efectoCLeon, DULeon)
imgCebra = pygame.image.load("Imagenes/ImgCartas/Carta_Cebra.png")
imgCebra = pygame.transform.rotate(pygame.transform.scale(imgCebra, (40, 80)), 90)
efectoCCebra = "Efecto: Mueve una unidad aliada 2 casillas"
DUCebra = "Habilidad “Correr” (Puede moverse 2 casillas adicionales el primer turno). Movimiento 4 (Terrestre), Puntaje Máximo 15"
ccebra1 = Carta("cebra", imgCebra, cebra1, efectoCCebra, DUCebra)
ccebra2 = Carta("cebra", imgCebra, cebra2, efectoCCebra, DUCebra)
ccebra3 = Carta("cebra", imgCebra, cebra3, efectoCCebra, DUCebra)
ccebra4 = Carta("cebra", imgCebra, cebra4, efectoCCebra, DUCebra)
imgMono = pygame.image.load("Imagenes/ImgCartas/Carta_Mono.png")
imgMono = pygame.transform.rotate(pygame.transform.scale(imgMono, (40, 80)), 90)
efectoCMono ="Retira una unidad"
DUMono = "Habilidad “Escabullirse” (Intercambia su posición con un enemigo). Movimiento 3 (Árboles), Puntaje Máximo 15"
cmono1 = Carta("mono", imgMono, mono1, efectoCMono,DUMono)
cmono2 = Carta("mono", imgMono, mono2, efectoCMono,DUMono)
cmono3 = Carta("mono", imgMono, mono3, efectoCMono,DUMono)
cmono4 = Carta("mono", imgMono, mono4, efectoCMono,DUMono)
imgTucan = pygame.image.load("Imagenes/ImgCartas/Carta_tucan.png")
imgTucan = pygame.transform.rotate(pygame.transform.scale(imgTucan, (40, 80)), 90)
efectoCTucan = "Gana dos puntos de victoria por cada Tucán en el territorio"
DUTucan = "Habilidad “vuelo rápido” (El turno en el que se juega puede moverse 2 espacios adicionales). Movimiento 4(Todo), Puntaje Máximo 10"
ctucan1 = Carta("tucan", imgTucan, tucan1, efectoCTucan, DUTucan)
ctucan2 = Carta("tucan", imgTucan, tucan2, efectoCTucan, DUTucan)
ctucan3 = Carta("tucan", imgTucan, tucan3, efectoCTucan, DUTucan)
ctucan4 = Carta("tucan", imgTucan, tucan4, efectoCTucan, DUTucan)
imgElefante = pygame.image.load("Imagenes/ImgCartas/Carta_Elefante.png")
imgElefante = pygame.transform.rotate(pygame.transform.scale(imgElefante, (40, 80)), 90)
efectoCElefante = "Elige una unidad, durante el próximo turno no puede ser movida. Gana un punto de victoria."
DUElefante = "Habilidad “Inamovible” (No puede ser movido por el enemigo). Movimiento 2 (Agua), Puntaje Máximo 15"
celefante1 = Carta("elefante", imgElefante, elefante1, efectoCElefante, DUElefante)
celefante2 = Carta("elefante", imgElefante, elefante2, efectoCElefante, DUElefante)
celefante3 = Carta("elefante", imgElefante, elefante3, efectoCElefante, DUElefante)
celefante4 = Carta("elefante", imgElefante, elefante4, efectoCElefante, DUElefante)
mazoSelva = [cleon1,cleon2,cleon3,cleon4,
             celefante1,celefante2,celefante3,celefante4,
             cmono1,cmono2,cmono3,cmono4,
             ctucan1,ctucan2,ctucan3,ctucan4,
             ccebra1,ccebra2,ccebra3,ccebra4]