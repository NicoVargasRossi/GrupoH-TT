#Imports
import pygame
# import pygame_menu

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
FPS = 15

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
map =  Tablero.map

buttonW = screenX/16
buttonH = screenY/16

button_Mover = button ((186, 190, 195), ((screenX * 3/4) + screenX/8), screenY/16, buttonW, buttonH, "Mover")
button_Habilidad = button ((186, 190, 195), ((screenX * 3/4) + screenX/8), screenY/8, buttonW, buttonH, "Habilidad")
button_Cancelar = button ((186,190,195), ((screenX * 3/4) + (screenX/16)), (screenY/4 - screenY/16),buttonW,buttonH, "Cancelar")
button_JugarCarta = button ((186,190,195), ((screenX * 3/4) + (screenX/16)), screenY/16, buttonW,buttonH, "Jugar")
button_Retirar = button ((186,190,195), ((screenX * 3/4) + (screenX/8)), (screenY/4 - screenY/16),buttonW,buttonH, "Retirar")
botones = [button_Mover, button_Habilidad, button_Cancelar]
botonesRetirar = [button_Mover, button_Habilidad, button_Cancelar, button_Retirar]
botonesMano = [button_JugarCarta, button_Cancelar]
cartaSeleccionada = False
tokenSeleccionado = False
#Loop de juego
UnidadesEnJuego = []
running = True
jugador1 = Jugador(mazoSelva)
#Metodos
def paint_button (button):
    if button == button_JugarCarta:
        button_JugarCarta.draw(main.screen, (255, 244, 0))
        pygame.display.update()
    if button == button_Cancelar:
        button_Cancelar.draw(main.screen, (255, 244, 0))
        pygame.display.update()
    if button == button_Mover:
        button_Mover.draw(main.screen, (255, 244, 0))
        pygame.display.update()
    if button == button_Habilidad:
        button_Habilidad.draw(main.screen, (255, 244, 0))
        pygame.display.update()
    if button == button_Retirar:
        button_Retirar.draw(main.screen, (255, 244, 0))
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
                                        paint_button(button_JugarCarta)
                                        c.seleccionada = True
                                        jugarCarta(c)
                                        Esperar = False
                                    if btn.text == "Cancelar":
                                        Esperar = False

        for c in Tablero.tablero:
            if c.r.collidepoint(pos):
                if c.Contenido is not None:
                    if c.pos[0] >= 11:
                            for b in botonesRetirar:
                                b.draw(main.screen)
                    else:
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
                                            paint_button(button_Mover)
                                            c.Contenido.Seleccionado = True
                                            main.tokenSeleccionado = True
                                            MoverToken(c)
                                            main.tokenSeleccionado = False
                                            Esperar = False
                                        elif btn.text == "Efecto":
                                            paint_button(button_Habilidad)
                                            Esperar = False
                                            main.tokenSeleccionado = False
                                            c.Contenido.Seleccionado = False
                                        elif btn.text == "Cancelar":
                                            paint_button(button_Cancelar)
                                            Esperar = False
                                            main.tokenSeleccionado = False
                                            c.Contenido.Seleccionado = False
                                for btn in botonesRetirar:
                                    if c.pos[0] >= 11:
                                        if btn.rect.collidepoint(posicion):
                                            if btn.text == "Retirar":
                                                paint_button(button_Retirar)
                                                main.tokenSeleccionado = False
                                                c.Contenido.Seleccionado = False
                                                retirarToken(c)
                                                c.Contenido = None
                                                Esperar = False
                if c.Contenido is None:
                     Esperar = False
def retirarToken(c):
    if c.pos[0] >= 11:
        UnidadesEnJuego.remove(c.Contenido)
        main.jugador1.Mazo.append(c.Contenido.cartaAsignada)
        c.Contenido = None
        pygame.display.update()
        print (UnidadesEnJuego)
        print (len(jugador1.Mazo))
def jugarCarta(carta):
     Esperar = True
     casillasPermitidas = []
     while Esperar:
        FPS_CLOCK.tick(FPS)
        for c in Tablero.tablero:
            if c.pos[0] == 11 or c.pos[0] == 12:
                if c.TipoTerreno in carta.token.TerrenoFavorable:
                    pygame.draw.rect(main.screen, (255, 233, 0),
                                     c.r, 4)
                    casillasPermitidas.append(c)
        pygame.display.update()
        for event in pygame.event.get():
             if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    posicion = pygame.mouse.get_pos()
                    for c in Tablero.tablero:
                        if c.r.collidepoint(posicion):
                            if carta.seleccionada and c.Contenido is None:
                                if c in casillasPermitidas:
                                    posicionDestino = (c.r.left + ((Tablero.casillaW / 2) - (Tablero.tokenW / 2)),
                                                       c.r.top + ((Tablero.casillaH / 2) - (Tablero.tokenH / 2)))
                                    carta.token.Posicion = posicionDestino
                                    UnidadesEnJuego.append(carta.token)
                                    c.Contenido = carta.token
                                    carta.seleccionada = False
                                    posicionDestino = None
                                    carta.token.cartaAsignada = carta
                                    jugador1.Mano.remove(carta)
                                    main.cartaSeleccionada = False
                                    Esperar = False
                                    print(c.Contenido)
def MoverToken(casillaOrig):
    esperar = True
    casillasPermitidas = []
    tokenUnidad = casillaOrig.Contenido
    while esperar:
        FPS_CLOCK.tick(FPS)
        pos_Tok_X, pos_Tok_Y = casillaOrig.pos
        for i in range(1, casillaOrig.Contenido.Movimiento + 1):
            if pos_Tok_X + i <= 12:
                casillaDestino = Tablero.tablero_Hash[(pos_Tok_X + i, pos_Tok_Y)]
                if casillaDestino.Contenido is None and casillaDestino.TipoTerreno in tokenUnidad.TerrenoFavorable:
                    pygame.draw.rect(main.screen, (255, 233, 0), Tablero.tablero_Hash[(pos_Tok_X + i, pos_Tok_Y)].r, 4)
                    casillasPermitidas.append(casillaDestino)
                    pygame.display.update()
                elif tokenUnidad.Nombre != "tucan":
                    break

        for i in range(1, casillaOrig.Contenido.Movimiento + 1):
            if pos_Tok_Y + i <= 5:
                casillaDestino = Tablero.tablero_Hash[(pos_Tok_X, pos_Tok_Y + i)]
                if casillaDestino.Contenido is None and casillaDestino.TipoTerreno in tokenUnidad.TerrenoFavorable:
                    pygame.draw.rect(main.screen, (255, 233, 0), Tablero.tablero_Hash[(pos_Tok_X, pos_Tok_Y + i)].r, 4)
                    casillasPermitidas.append(casillaDestino)
                    pygame.display.update()
                elif tokenUnidad.Nombre != "tucan":
                    break

        for i in range(1, casillaOrig.Contenido.Movimiento + 1):
            if pos_Tok_X - i >= 0:
                casillaDestino = Tablero.tablero_Hash[(pos_Tok_X - i, pos_Tok_Y)]
                if casillaDestino.Contenido is None and casillaDestino.TipoTerreno in tokenUnidad.TerrenoFavorable:
                    pygame.draw.rect(main.screen, (255, 233, 0), Tablero.tablero_Hash[(pos_Tok_X - i, pos_Tok_Y)].r, 4)
                    casillasPermitidas.append(casillaDestino)
                    pygame.display.update()
                elif tokenUnidad.Nombre != "tucan":
                    break

        for i in range(1, casillaOrig.Contenido.Movimiento + 1):
            if pos_Tok_Y - i >= 0:
                casillaDestino = Tablero.tablero_Hash[(pos_Tok_X, pos_Tok_Y - i)]
                if casillaDestino.Contenido is None and casillaDestino.TipoTerreno in tokenUnidad.TerrenoFavorable:
                    pygame.draw.rect(main.screen, (255, 233, 0), Tablero.tablero_Hash[(pos_Tok_X, pos_Tok_Y - i)].r, 4)
                    casillasPermitidas.append(casillaDestino)
                    pygame.display.update()
                elif tokenUnidad.Nombre != "tucan":
                    break

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    posicion = pygame.mouse.get_pos()
                    for c in Tablero.tablero:
                        if c.r.collidepoint(posicion):
                            if c in casillasPermitidas:
                                posicionDestino = (c.r.left + ((Tablero.casillaW / 2) - (Tablero.tokenW / 2)),
                                                   c.r.top + ((Tablero.casillaH / 2) - (Tablero.tokenH / 2)))

                                if tokenUnidad.Seleccionado is True:
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

#Arreglar*
carta_Mostrada_W = Tablero.carta_Mostrada_W
carta_Mostrada_H = Tablero.carta_Mostrada_H
carta_Mostrada = Tablero.carta_Mostrada

while running:
    screen.fill((160, 216, 160))
    screen.blit(map, ((screenX/4) - (mapX/4), (screenY/2) - (mapY/2)))
    screen.blit(Tablero.fondo_Hud, (screenX * (3 / 4), 0))
    screen.blit(Tablero.cuadro_De_puntuacion, (int(screenX * 13/16), int(screenY * 5/16)))

    # Transformo escalando la carta para que sea responsive a la dimension de la pantalla
    carta_Mostrada_Escalada = pygame.transform.scale(carta_Mostrada, (carta_Mostrada_W, carta_Mostrada_H))
    screen.blit(carta_Mostrada_Escalada, ((screenX * (3/4) + screenX/16), ((screenY/2) + screenY/16)))

    for u in UnidadesEnJuego:
        if u.Posicion is not None:
         screen.blit(u.Icono,(u.Posicion))
    for i in range(len(jugador1.Mano)):
             jugador1.Mano[i].posicionEnMano = Tablero.ManoPl1[i]
             screen.blit(jugador1.Mano[i].imagen, Tablero.ManoPl1[i])
    for carta in range(len(Tablero.ManoPl2)):
             screen.blit(Tablero.img_Dorso_Carta, Tablero.ManoPl2[carta] )
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

exit()