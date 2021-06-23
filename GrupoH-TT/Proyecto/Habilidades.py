import pygame

import Token
import Tablero
import EjercitoSelva
import Casilla
import main

def escabullirse(casillaOrig, casillaDestino):
    esperar = True
    tokenDestino = casillaDestino
    tokenCasilla = casillaOrig
    casillasPermitidas = []
    #tokenUnidad = casillaOrig.Contenido
    while esperar:
        #pos_Tok_X, pos_Tok_Y = casillaOrig.pos
        #casillaDestino = Tablero.tablero_Hash[(pos_Tok_X + i, pos_Tok_Y)]
        if casillaDestino.Contenido is not None:
            casillaOrig.append(casillaDestino)
            if tokenCasilla.Seleccionado is True:
                if main.tokenSeleccionado is True:
                    casillaOrig.Contenido.Posicion = tokenDestino
                    casillaOrig.Contenido.Seleccionado = False
                    main.tokenSeleccionado = False
                    c.Contenido = casillaOrig.Contenido
                    casillaOrig.Contenido = None
            pygame.display.update()

def vueloRapido():

    pass
