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
                                            # MoverToken(c)
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
                    posicion = pygame.mouse.get_pos()
                    for c in Tablero.tablero:
                        if c.r.collidepoint(posicion):
                            if carta.seleccionada == True and c.Contenido is None:
                                posicionDestino = (c.r.left + ((Tablero.casillaW / 2) - (Tablero.tokenW / 2)),
                                                   c.r.top + ((Tablero.casillaH / 2) - (Tablero.tokenH / 2)))
                                carta.token.Posicion = posicionDestino
                                UnidadesEnJuego.append(carta.token)
                                c.Contenido = carta.token
                                carta.seleccionada = False
                                posicionDestino = None
                                jugador1.Mazo.append(carta)
                                jugador1.Mano.remove(carta)
                                main.cartaSeleccionada = False
                                Esperar = False
                                print(c.Contenido)

def MoverToken(casillaOrig):
    Esperar = True
    while Esperar:
        pos_Tok_X, pos_Tok_Y = casillaOrig.pos
        for i in range(casillaOrig.Contenido.Movimiento):
            if pos_Tok_X + 1 + i < 13:
                pygame.draw.rect(main.screen, (255, 233, 0),Tablero.tablero_Hash[(pos_Tok_X + 1 + i, pos_Tok_Y)].r, 4)
                pygame.display.update()
            if pos_Tok_Y + 1 + i < 6:
                    pygame.draw.rect(main.screen, (255, 233, 0),Tablero.tablero_Hash[(pos_Tok_X, pos_Tok_Y + 1 + i)].r, 4)
                    pygame.display.update()
            if pos_Tok_X - 1 - i >= 0:
                    pygame.draw.rect(main.screen, (255, 233, 0),Tablero.tablero_Hash[(pos_Tok_X - 1 - i, pos_Tok_Y)].r, 4)
                    pygame.display.update()
            if pos_Tok_Y - 1 - i >= 0:
                    pygame.draw.rect(main.screen, (255, 233, 0),Tablero.tablero_Hash[(pos_Tok_X, pos_Tok_Y - 1 - i)].r, 4)
                    pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    posicion = pygame.mouse.get_pos()
                    for c in Tablero.tablero:
                        if c.r.collidepoint(posicion):
                            if c.Contenido is None:
                                posicionDestino = (c.r.left + ((Tablero.casillaW / 2) - (Tablero.tokenW / 2)),
                                        c.r.top + ((Tablero.casillaH / 2) - (Tablero.tokenH / 2)))

                                if casillaOrig.Seleccionado is True:
                                    if main.tokenSeleccionado is True:
                                        casillaOrig.Contenido.Posicion = posicionDestino
                                        casillaOrig.Contenido.Seleccionado = False
                                        main.tokenSeleccionado = False
                                        c.Contenido = casillaOrig.Contenido
                                        casillaOrig.Contenido = None
                                    elif main.tokenSeleccionado is False:
                                        esperar = False
                                        casillaOrig.Contenido.Seleccionado = False
                                        main.tokenSeleccionado = False
                                elif casillaOrig.Contenido.Seleccionado is False:
                                    esperar = False
                                    main.tokenSeleccionado = False

                            elif c.Contenido is not None:
                                casillaOrig.Contenido.Seleccionado = False
                                main.tokenSeleccionado = False
                                esperar = False

                            esperar = False
def requisitosMov(posicion,casilla, movimiento):
    cdx, cdy = casilla
    posx, posy = posicion.pos
    if cdx <= posx - movimiento -1 and cdy <= posy - movimiento - 1 and cdx >= posx + movimiento + 1 and posy >= posy + movimiento +1 :
        return True
# Divido la anchura y altura de screen para asignarle el alto y ancho a la carta
carta_Mostrada_W = int(screenX/5.5)
carta_Mostrada_H = int(screenY/2.5)
carta_Mostrada = pygame.image.load("Imagenes/ImgCartas/Carta_Negra.png")
while running:
    screen.fill((0, 0, 0))
    screen.blit(map, ((screenX/2) - (mapX/2), (screenY/2) - (mapY/2)))
    # Transformo escalando la carta para que sea responsive a la dimension de la pantalla
    carta_Mostrada_Escalada = pygame.transform.scale(carta_Mostrada, (carta_Mostrada_W, carta_Mostrada_H))
    screen.blit(carta_Mostrada_Escalada, (screenX - carta_Mostrada_W, screenY - carta_Mostrada_H))
    for u in UnidadesEnJuego:
        if u.Posicion is not None:
         screen.blit(u.Icono,(u.Posicion))
         for i in range(len(jugador1.Mano)):
             jugador1.Mano[i].posicionEnMano = Tablero.ManoPl1[i]
             screen.blit(jugador1.Mano[i].imagen, Tablero.ManoPl1[i])
         for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 running = False
             # Cartas
             # Seleccionar Carta
             if event.type == pygame.MOUSEBUTTONUP:
                 if event.button == 3:
                     posicion = pygame.mouse.get_pos()
                     for c in jugador1.Mano:
                         if c.posicionEnMano.collidepoint(posicion):
                             if cartaSeleccionada == False:
                                 if c.seleccionada == False:
                                     c.seleccionada = True
                                     cartaSeleccionada = True
                             mostrarBotones(posicion)
                     # Token
                     # Seleccionar Token
             if event.type == pygame.MOUSEBUTTONDOWN:
                     if event.button == 3:
                         posicion = pygame.mouse.get_pos()
                         for c in Tablero.tablero:
                             if c.r.collidepoint(posicion):
                                 if tokenSeleccionado == False:
                                     if c.Contenido is not None:
                                         c.Contenido.Seleccionado = True
                                         tokenSeleccionado = True
                                         mostrarBotones(posicion)
                                     else:
                                         print("coso")
                         for c in jugador1.Mano:
                             if c.posicionEnMano.collidepoint(posicion):
                                 carta_Mostrada = carta_Img_Hash[c.nombre]
                                 pygame.display.update()
             pygame.display.update()