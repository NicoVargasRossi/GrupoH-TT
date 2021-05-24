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
imgCarta_Leon_compl = pygame.transform.scale(pygame.image.load("Imagenes/ImgCartas/Carta_Leon.png"),(150,200))
imgCarta_Cebra_compl = pygame.transform.scale(pygame.image.load("Imagenes/ImgCartas/Carta_Cebra.png"),(150,200))
imgCarta_Mono_compl = pygame.transform.scale(pygame.image.load("Imagenes/ImgCartas/Carta_Mono.png"),(150,200))
imgCarta_Tucan_compl = pygame.transform.scale(pygame.image.load("Imagenes/ImgCartas/Carta_tucan.png"),(150,200))
imgCarta_Elefante_compl = pygame.transform.scale(pygame.image.load("Imagenes/ImgCartas/Carta_Elefante.png"),(150,200))
carta_Img_Hash = {
    "leon": imgCarta_Leon_compl,
    "cebra": imgCarta_Cebra_compl,
    "mono": imgCarta_Mono_compl,
    "tucan": imgCarta_Tucan_compl,
    "elefante": imgCarta_Elefante_compl,
}