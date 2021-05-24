#Imports
import pygame
import pygame_menu

import Carta
import EjercitoSelva
import Tablero
import Token
import main
from Tablero import *
from Casilla import *
from EjercitoSelva import *
from Jugador import *
from Carta import *
from button import *
#Inicialización y display
pygame.init()

FPS_CLOCK = pygame.time.Clock()
FPS = 10

pygame.display.set_caption("Tácticas Salvajes")
icon = pygame.image.load('Imagenes/leo.png')
pygame.display.set_icon(icon)

# La resolucion se cambia desde el archivo de tablero
screenX = Tablero.screenX
screenY = Tablero.screenY
screen = pygame.display.set_mode((screenX, screenY))
mainRect = pygame.Rect(0,0,screenX,screenY)
mapX = Tablero.mapX
mapY = Tablero.mapY
map = pygame.image.load('Imagenes/map.png')

buttonW = 60
buttonH = 25
button_Token1 = button ((186,190,195), screenX-buttonW - 5, buttonH * 1, buttonW,buttonH, "Mover")
button_Token2 = button ((186,190,195), screenX-buttonW - 5, buttonH * 2 + 5, buttonW,buttonH, "Efecto")
button_Cancelar = button ((186,190,195), screenX-buttonW - 5, buttonH * 3 + 10,buttonW,buttonH, "Cancelar")
button_JugarCarta = button ((186,190,195), screenX-buttonW - 5, buttonH * 1, buttonW,buttonH, "Jugar")
button_Retirar = button ((186,190,195), screenX-buttonW - 5, buttonH * 4 + 15,buttonW,buttonH, "Retirar")
botones = [button_Token1, button_Token2, button_Cancelar]
botonesMano = [button_JugarCarta, button_Cancelar]
cartaSeleccionada = False
tokenSeleccionado = False
#Loop de juego
UnidadesEnJuego = []
running = True
jugador1 = Jugador(mazoSelva)
#Metodos
def mostrarBotones(pos):
    Esperar = True
    while Esperar:
        FPS_CLOCK.tick(FPS)
        for c in jugador1.Mano:
            if c.posicionEnMano.collidepoint(pos):
                for b in botonesMano:
                    b.draw(main.screen)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            posicion = pygame.mouse.get_pos()
                            for btn in botonesMano:
                                if btn.rect.collidepoint(posicion):
                                    if btn.text == "Jugar":
                                        c.seleccionada = True
                                        jugarCarta(c)
                                        Esperar = False
                                    if btn.text == "Cancelar":
                                        Esperar = False

        for c in Tablero.tablero:
            if c.r.collidepoint(pos):
                if c.Contenido is not None:
                    for b in botones:
                        b.draw(main.screen)
                    pygame.display.update()
                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONUP:
                            if event.button == 1:
                                posicion = pygame.mouse.get_pos()
                                for btn in botones:

                                    if btn.rect.collidepoint(posicion):
                                        if btn.text == "Mover":
                                            c.Contenido.Seleccionado = True
                                            main.tokenSeleccionado = True
                                            MoverToken(c)
                                            main.tokenSeleccionado = False
                                            Esperar = False
                                        elif btn.text == "Efecto":
                                            Esperar = False
                                            main.tokenSeleccionado = False
                                            c.Contenido.Seleccionado = False
                                        elif btn.text == "Cancelar":
                                            Esperar = False
                                            main.tokenSeleccionado = False
                                            c.Contenido.Seleccionado = False
                if c.Contenido is None:
                     Esperar = False

def jugarCarta(carta):
     Esperar = True
     while Esperar:
        for event in pygame.event.get():
             if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: