import pygame

class Casilla:
    def __init__(self, TipoTerreno, pos, Contenido, Puntuacion, Estado, a,b,c,d):
      self.TipoTerreno = TipoTerreno
      self.pos = pos
      self.Contenido = Contenido
      self.Puntuacion = Puntuacion
      self.Estado = Estado
      self.r = pygame.Rect(a,b,c,d)