import pygame

import Token

from Token import *
from Carta import *

#Tokens
IconoLeon = pygame.image.load("Imagenes/LogosAnimales/lion.png")
leon1 = Token.Token("leon", IconoLeon, 3 , "Rugido", 10, "Normal", None)
leon2 = Token.Token("leon", IconoLeon, 3 , "Rugido", 10, "Normal", None)
leon3 = Token.Token("leon", IconoLeon, 3 , "Rugido", 10, "Normal", None)
leon4 = Token.Token("leon", IconoLeon, 3 , "Rugido", 10, "Normal", None)
IconoCebra = pygame.image.load("Imagenes/LogosAnimales/zebra.png")
cebra1 = Token.Token("cebra", IconoCebra,4,"Correr",15,"Normal",None)
cebra2 = Token.Token("cebra", IconoCebra,4,"Correr",15,"Normal",None)
cebra3 = Token.Token("cebra", IconoCebra,4,"Correr",15,"Normal",None)
cebra4 = Token.Token("cebra", IconoCebra,4,"Correr",15,"Normal",None)
IconoMono = pygame.image.load("Imagenes/LogosAnimales/mono.png")
mono1 = Token.Token("mono", IconoMono,3,"Escabullirse",15,"Árboles",None)
mono2 = Token.Token("mono", IconoMono,3,"Escabullirse",15,"Árboles",None)
mono3 = Token.Token("mono", IconoMono,3,"Escabullirse",15,"Árboles",None)
mono4 = Token.Token("mono", IconoMono,3,"Escabullirse",15,"Árboles",None)
IconoTucan = pygame.image.load("Imagenes/LogosAnimales/tucan.png")
tucan1 = Token.Token("tucan", IconoTucan,4,"Vuelo rápido",10,"Todo",None)
tucan2 = Token.Token("tucan", IconoTucan,4,"Vuelo rápido",10,"Todo",None)
tucan3 = Token.Token("tucan", IconoTucan,4,"Vuelo rápido",10,"Todo",None)
tucan4 = Token.Token("tucan", IconoTucan,4,"Vuelo rápido",10,"Todo",None)