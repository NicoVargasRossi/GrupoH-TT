import pygame
import Token
class Carta:
    imagen = pygame.image
    token = Token
    efectoEspecial = ""
    seleccionada = False
    posicionEnMano = None
    def __init__(self,nombre, img, token, efecto, detalles):
        self.nombre = nombre
        self.imagen = img
        self.token = token
        self.efecto = efecto
        self.detalles = detalles
