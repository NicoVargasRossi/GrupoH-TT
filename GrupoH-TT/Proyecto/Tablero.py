from Casilla import *

from Carta import *

#La resolucion se cambia seleccionando screenX y screenY
screenX = 1024
screenY = 600

#El tablero puede cambiar de tamaño pero hay que ajustar el tamaño de las casillas segun sea la distribucion del nuevo tablero
mapX = 650
mapY = 300
# Tamaño del Rect de las casillas
casillaW = 50
casillaH = 50
# Tamaño del token
tokenW = 32
tokenH = 32
# Tamaño del rect de las cartas en la mano
carta_ManoW = 50
carta_ManoH = 50

Casilla00 = Casilla("Normal",(0,0),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 0), (screenY/2) - (mapY/2) + (casillaH *0),casillaW,casillaH)
Casilla01 = Casilla("Normal",(0,1),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 0), (screenY/2) - (mapY/2) + (casillaH *1) ,casillaW,casillaH)
Casilla02 = Casilla("Normal",(0,2),None, (0,5), "No", (screenX/2) - (mapX/2) + (casillaW * 0), (screenY/2) - (mapY/2) + (casillaH *2),casillaW,casillaH)
Casilla03 = Casilla("Normal",(0,3),None, (0,5), "No", (screenX/2) - (mapX/2) + (casillaW * 0), (screenY/2) - (mapY/2) + (casillaH *3),casillaW,casillaH)
Casilla04 = Casilla("Normal",(0,4),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 0), (screenY/2) - (mapY/2) + (casillaH *4),casillaW,casillaH)
Casilla05 = Casilla("Agua",  (0,5),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 0), (screenY/2) - (mapY/2) + (casillaH *5),casillaW,casillaH)
Casilla10 = Casilla("Normal",(1,0),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 1), (screenY/2) - (mapY/2) + (casillaH *0),casillaW,casillaH)
Casilla11 = Casilla("Normal",(1,1),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 1), (screenY/2) - (mapY/2) + (casillaH *1),casillaW,casillaH)
Casilla12 = Casilla("Normal",(1,2),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 1), (screenY/2) - (mapY/2) + (casillaH *2),casillaW,casillaH)
Casilla13 = Casilla("Normal",(1,3),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 1), (screenY/2) - (mapY/2) + (casillaH *3),casillaW,casillaH)
Casilla14 = Casilla("Normal",(1,4),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 1), (screenY/2) - (mapY/2) + (casillaH *4),casillaW,casillaH)
Casilla15 = Casilla("Agua",  (1,5),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 1), (screenY/2) - (mapY/2) + (casillaH *5),casillaW,casillaH)
Casilla20 = Casilla("Normal",(2,0),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 2), (screenY/2) - (mapY/2) + (casillaH *0),casillaW,casillaH)
Casilla21 = Casilla("Bosque",(2,1),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 2), (screenY/2) - (mapY/2) + (casillaH *1),casillaW,casillaH)
Casilla22 = Casilla("Normal",(2,2),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 2), (screenY/2) - (mapY/2) + (casillaH *2),casillaW,casillaH)
Casilla23 = Casilla("Normal",(2,3),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 2), (screenY/2) - (mapY/2) + (casillaH *3),casillaW,casillaH)
Casilla24 = Casilla("Normal",(2,4),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 2), (screenY/2) - (mapY/2) + (casillaH *4),casillaW,casillaH)
Casilla25 = Casilla("Normal",(2,5),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 2), (screenY/2) - (mapY/2) + (casillaH *5),casillaW,casillaH)
Casilla30 = Casilla("Normal",(3,0),None, (1,3), "No", (screenX/2) - (mapX/2) + (casillaW * 3), (screenY/2) - (mapY/2) + (casillaH *0),casillaW,casillaH)
Casilla31 = Casilla("Bosque",(3,1),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 3), (screenY/2) - (mapY/2) + (casillaH *1),casillaW,casillaH)
Casilla32 = Casilla("Normal",(3,2),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 3), (screenY/2) - (mapY/2) + (casillaH *2),casillaW,casillaH)
Casilla33 = Casilla("Normal",(3,3),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 3), (screenY/2) - (mapY/2) + (casillaH *3),casillaW,casillaH)
Casilla34 = Casilla("Bosque",(3,4),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 3), (screenY/2) - (mapY/2) + (casillaH *4),casillaW,casillaH)
Casilla35 = Casilla("Normal",(3,5),None, (1,3), "No", (screenX/2) - (mapX/2) + (casillaW * 3), (screenY/2) - (mapY/2) + (casillaH *5),casillaW,casillaH)
Casilla40 = Casilla("Normal",(4,0),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 4), (screenY/2) - (mapY/2) + (casillaH *0),casillaW,casillaH)
Casilla41 = Casilla("Normal",(4,1),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 4), (screenY/2) - (mapY/2) + (casillaH *1),casillaW,casillaH)
Casilla42 = Casilla("Normal",(4,2),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 4), (screenY/2) - (mapY/2) + (casillaH *2),casillaW,casillaH)
Casilla43 = Casilla("Normal",(4,3),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 4), (screenY/2) - (mapY/2) + (casillaH *3),casillaW,casillaH)
Casilla44 = Casilla("Normal",(4,4),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 4), (screenY/2) - (mapY/2) + (casillaH *4),casillaW,casillaH)
Casilla45 = Casilla("Normal",(4,5),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 4), (screenY/2) - (mapY/2) + (casillaH *5),casillaW,casillaH)
Casilla50 = Casilla("Normal",(5,0),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 5), (screenY/2) - (mapY/2) + (casillaH *0),casillaW,casillaH)
Casilla51 = Casilla("Agua",  (5,1),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 5), (screenY/2) - (mapY/2) + (casillaH *1),casillaW,casillaH)
Casilla52 = Casilla("Agua",  (5,2),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 5), (screenY/2) - (mapY/2) + (casillaH *2),casillaW,casillaH)
Casilla53 = Casilla("Normal",(5,3),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 5), (screenY/2) - (mapY/2) + (casillaH *3),casillaW,casillaH)
Casilla54 = Casilla("Normal",(5,4),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 5), (screenY/2) - (mapY/2) + (casillaH *4),casillaW,casillaH)
Casilla55 = Casilla("Normal",(5,5),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 5), (screenY/2) - (mapY/2) + (casillaH *5),casillaW,casillaH)
Casilla60 = Casilla("Normal",(6,0),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 6), (screenY/2) - (mapY/2) + (casillaH *0),casillaW,casillaH)
Casilla61 = Casilla("Agua",  (6,1),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 6), (screenY/2) - (mapY/2) + (casillaH *1),casillaW,casillaH)
Casilla62 = Casilla("Agua",  (6,2),None, (2,2), "No", (screenX/2) - (mapX/2) + (casillaW * 6), (screenY/2) - (mapY/2) + (casillaH *2),casillaW,casillaH)
Casilla63 = Casilla("Normal",(6,3),None, (2,2), "No", (screenX/2) - (mapX/2) + (casillaW * 6), (screenY/2) - (mapY/2) + (casillaH *3),casillaW,casillaH)
Casilla64 = Casilla("Normal",(6,4),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 6), (screenY/2) - (mapY/2) + (casillaH *4),casillaW,casillaH)
Casilla65 = Casilla("Normal",(6,5),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 6), (screenY/2) - (mapY/2) + (casillaH *5),casillaW,casillaH)
Casilla70 = Casilla("Normal",(7,0),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 7), (screenY/2) - (mapY/2) + (casillaH *0),casillaW,casillaH)
Casilla71 = Casilla("Normal",(7,1),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 7), (screenY/2) - (mapY/2) + (casillaH *1),casillaW,casillaH)
Casilla72 = Casilla("Normal",(7,2),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 7), (screenY/2) - (mapY/2) + (casillaH *2),casillaW,casillaH)
Casilla73 = Casilla("Normal",(7,3),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 7), (screenY/2) - (mapY/2) + (casillaH *3),casillaW,casillaH)
Casilla74 = Casilla("Bosque",(7,4),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 7), (screenY/2) - (mapY/2) + (casillaH *4),casillaW,casillaH)
Casilla75 = Casilla("Normal",(7,5),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 7), (screenY/2) - (mapY/2) + (casillaH *5),casillaW,casillaH)
Casilla80 = Casilla("Normal",(8,0),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 8), (screenY/2) - (mapY/2) + (casillaH *0),casillaW,casillaH)
Casilla81 = Casilla("Normal",(8,1),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 8), (screenY/2) - (mapY/2) + (casillaH *1),casillaW,casillaH)
Casilla82 = Casilla("Normal",(8,2),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 8), (screenY/2) - (mapY/2) + (casillaH *2),casillaW,casillaH)
Casilla83 = Casilla("Normal",(8,3),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 8), (screenY/2) - (mapY/2) + (casillaH *3),casillaW,casillaH)
Casilla84 = Casilla("Normal",(8,4),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 8), (screenY/2) - (mapY/2) + (casillaH *4),casillaW,casillaH)
Casilla85 = Casilla("Normal",(8,5),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 8), (screenY/2) - (mapY/2) + (casillaH *5),casillaW,casillaH)
Casilla90 = Casilla("Normal",(9,0),None, (3,1), "No", (screenX/2) - (mapX/2) + (casillaW * 9), (screenY/2) - (mapY/2) + (casillaH *0),casillaW,casillaH)
Casilla91 = Casilla("Normal",(9,1),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 9), (screenY/2) - (mapY/2) + (casillaH *1),casillaW,casillaH)
Casilla92 = Casilla("Normal",(9,2),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 9), (screenY/2) - (mapY/2) + (casillaH *2),casillaW,casillaH)
Casilla93 = Casilla("Normal",(9,3),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 9), (screenY/2) - (mapY/2) + (casillaH *3),casillaW,casillaH)
Casilla94 = Casilla("Normal",(9,4),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 9), (screenY/2) - (mapY/2) + (casillaH *4),casillaW,casillaH)
Casilla95 = Casilla("Normal",(9,5),None, (3,1), "No", (screenX/2) - (mapX/2) + (casillaW * 9), (screenY/2) - (mapY/2) + (casillaH *5),casillaW,casillaH)
Casilla100 = Casilla("Normal",(10,0),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 10), (screenY/2) - (mapY/2) + (casillaH *0),casillaW,casillaH)
Casilla101 = Casilla("Normal",(10,1),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 10), (screenY/2) - (mapY/2) + (casillaH *1),casillaW,casillaH)
Casilla102 = Casilla("Normal",(10,2),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 10), (screenY/2) - (mapY/2) + (casillaH *2),casillaW,casillaH)
Casilla103 = Casilla("Normal",(10,3),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 10), (screenY/2) - (mapY/2) + (casillaH *3),casillaW,casillaH)
Casilla104 = Casilla("Agua",  (10,4),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 10), (screenY/2) - (mapY/2) + (casillaH *4),casillaW,casillaH)
Casilla105 = Casilla("Normal",(10,5),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 10), (screenY/2) - (mapY/2) + (casillaH *5),casillaW,casillaH)
Casilla110 = Casilla("Agua",  (11,0),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 11), (screenY/2) - (mapY/2) + (casillaH *0),casillaW,casillaH)
Casilla111 = Casilla("Normal",(11,1),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 11), (screenY/2) - (mapY/2) + (casillaH *1),casillaW,casillaH)
Casilla112 = Casilla("Bosque",(11,2),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 11), (screenY/2) - (mapY/2) + (casillaH *2),casillaW,casillaH)
Casilla113 = Casilla("Normal",(11,3),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 11), (screenY/2) - (mapY/2) + (casillaH *3),casillaW,casillaH)
Casilla114 = Casilla("Normal",(11,4),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 11), (screenY/2) - (mapY/2) + (casillaH *4),casillaW,casillaH)
Casilla115 = Casilla("Normal",(11,5),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 11), (screenY/2) - (mapY/2) + (casillaH *5),casillaW,casillaH)
Casilla120 = Casilla("Agua",  (12,0),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 12), (screenY/2) - (mapY/2) + (casillaH *0),casillaW,casillaH)
Casilla121 = Casilla("Normal",(12,1),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 12), (screenY/2) - (mapY/2) + (casillaH *1),casillaW,casillaH)
Casilla122 = Casilla("Normal",(12,2),None, (5,0), "No", (screenX/2) - (mapX/2) + (casillaW * 12), (screenY/2) - (mapY/2) + (casillaH *2),casillaW,casillaH)
Casilla123 = Casilla("Normal",(12,3),None, (5,0), "No", (screenX/2) - (mapX/2) + (casillaW * 12), (screenY/2) - (mapY/2) + (casillaH *3),casillaW,casillaH)
Casilla124 = Casilla("Normal",(12,4),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 12), (screenY/2) - (mapY/2) + (casillaH *4),casillaW,casillaH)
Casilla125 = Casilla("Normal",(12,5),None, (0,0), "No", (screenX/2) - (mapX/2) + (casillaW * 12), (screenY/2) - (mapY/2) + (casillaH *5),casillaW,casillaH)

r1 = pygame.Rect(((screenX/2) - (mapX/2) + mapX + 15 ),(screenY/2) - (mapY/2) + (carta_ManoH * 0),carta_ManoW,carta_ManoH)
r2 = pygame.Rect(((screenX/2) - (mapX/2) + mapX + 15 ),(screenY/2) - (mapY/2) + (carta_ManoH * 1),carta_ManoW,carta_ManoH)
r3 = pygame.Rect(((screenX/2) - (mapX/2) + mapX + 15 ),(screenY/2) - (mapY/2) + (carta_ManoH * 2),carta_ManoW,carta_ManoH)
r4 = pygame.Rect(((screenX/2) - (mapX/2) + mapX + 15 ),(screenY/2) - (mapY/2) + (carta_ManoH * 3),carta_ManoW,carta_ManoH)
r5 = pygame.Rect(((screenX/2) - (mapX/2) + mapX + 15 ),(screenY/2) - (mapY/2) + (carta_ManoH * 4),carta_ManoW,carta_ManoH)
l1 = pygame.Rect(0,0,50,50)
l2 = pygame.Rect(0,50,50,50)
l3 = pygame.Rect(0,100,50,50)
l4 = pygame.Rect(0,150,50,50)
l5 = pygame.Rect(0,200,50,50)

tablero = [Casilla00,Casilla01,Casilla02,Casilla03,Casilla04,Casilla05,
           Casilla10,Casilla11,Casilla12,Casilla13,Casilla14,Casilla15,
           Casilla20,Casilla21,Casilla22,Casilla23,Casilla24,Casilla25,
           Casilla30,Casilla31,Casilla32,Casilla33,Casilla34,Casilla35,
           Casilla40,Casilla41,Casilla42,Casilla43,Casilla44,Casilla45,
           Casilla50,Casilla51,Casilla52,Casilla53,Casilla54,Casilla55,
           Casilla60,Casilla61,Casilla62,Casilla63,Casilla64,Casilla65,
           Casilla70,Casilla71,Casilla72,Casilla73,Casilla74,Casilla75,
           Casilla80,Casilla81,Casilla82,Casilla83,Casilla84,Casilla85,
           Casilla90,Casilla91,Casilla92,Casilla93,Casilla94,Casilla95,
           Casilla100,Casilla101,Casilla102,Casilla103,Casilla104,Casilla105,
           Casilla110,Casilla111,Casilla112,Casilla113,Casilla114,Casilla115,
           Casilla120,Casilla121,Casilla122,Casilla123,Casilla124,Casilla125]

tablero_Hash = {
    (0,0): Casilla00, (1,0):  Casilla10, (2,0): Casilla20, (3,0): Casilla30, (4,0): Casilla40, (5,0): Casilla50, (6,0): Casilla60, (7,0): Casilla70, (8,0): Casilla80, (9,0): Casilla90, (10,0): Casilla100, (11,0): Casilla110, (12,0): Casilla120,
    (0,1): Casilla01, (1,1):  Casilla11, (2,1): Casilla21, (3,1): Casilla31, (4,1): Casilla41, (5,1): Casilla51, (6,1): Casilla61, (7,1): Casilla71, (8,1): Casilla81, (9,1): Casilla91, (10,1): Casilla101, (11,1): Casilla111, (12,1): Casilla121,
    (0,2): Casilla02, (1,2):  Casilla12, (2,2): Casilla22, (3,2): Casilla32, (4,2): Casilla42, (5,2): Casilla52, (6,2): Casilla62, (7,2): Casilla72, (8,2): Casilla82, (9,2): Casilla92, (10,2): Casilla102, (11,2): Casilla112, (12,2): Casilla122,
    (0,3): Casilla03, (1,3):  Casilla13, (2,3): Casilla23, (3,3): Casilla33, (4,3): Casilla43, (5,3): Casilla53, (6,3): Casilla63, (7,3): Casilla73, (8,3): Casilla83, (9,3): Casilla93, (10,3): Casilla103, (11,3): Casilla113, (12,3): Casilla123,
    (0,4): Casilla04, (1,4):  Casilla14, (2,4): Casilla24, (3,4): Casilla34, (4,4): Casilla44, (5,4): Casilla54, (6,4): Casilla64, (7,4): Casilla74, (8,4): Casilla84, (9,4): Casilla94, (10,4): Casilla104, (11,4): Casilla114, (12,4): Casilla124,
    (0,5): Casilla05, (1,5):  Casilla15, (2,5): Casilla25, (3,5): Casilla35, (4,5): Casilla45, (5,5): Casilla55, (6,5): Casilla65, (7,5): Casilla75, (8,5): Casilla85, (9,5): Casilla95, (10,5): Casilla105, (11,5): Casilla115, (12,5): Casilla125,

}

ManoPl1 = [r1,r2,r3,r4,r5]
ManoPl2 = [l1,l2,l3,l4,l5]