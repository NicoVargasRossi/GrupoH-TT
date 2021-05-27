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
imgCarta_Zorro_compl = pygame.transform.scale(pygame.image.load("Imagenes/ImgCartas/Carta_Zorro.png"),(150,200))
imgCarta_Oso_compl = pygame.transform.scale(pygame.image.load("Imagenes/ImgCartas/Carta_Oso.png"),(150,200))
imgCarta_Gaviota_compl = pygame.transform.scale(pygame.image.load("Imagenes/ImgCartas/Carta_Gaviota.png"),(150,200))
imgCarta_Pinguino_compl = pygame.transform.scale(pygame.image.load("Imagenes/ImgCartas/Carta_Pinguino.png"),(150,200))
imgCarta_Reno_compl = pygame.transform.scale(pygame.image.load("Imagenes/ImgCartas/Carta_Reno.png"),(150,200))
carta_Img_Hash = {
    "leon": imgCarta_Leon_compl,
    "cebra": imgCarta_Cebra_compl,
    "mono": imgCarta_Mono_compl,
    "tucan": imgCarta_Tucan_compl,
    "elefante": imgCarta_Elefante_compl,
    "zorro": imgCarta_Zorro_compl,
    "oso polar": imgCarta_Oso_compl,
    "gaviota": imgCarta_Gaviota_compl,
    "pingüino": imgCarta_Pinguino_compl,
    "reno": imgCarta_Reno_compl,
}