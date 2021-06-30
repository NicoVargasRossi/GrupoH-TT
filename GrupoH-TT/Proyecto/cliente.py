from socket import *
from main import jugador1

conexion = socket(AF_INET, SOCK_STREAM)
conexion.connect(('localhost', 8000))
print("cliente basico")

def recibe_orden():

    conexion.send(str("estoy esperando ordenes").encode('utf-8'))

    orden_juego = conexion.recv(1024)  # queda a la espera de orden
    lista_movimiento = orden_juego.decode('utf-8').split()  # separa la orden en una lsita de strings
    print(lista_movimiento)  # el primer elemento deberia ser el tipo de accion

    if lista_movimiento[0] == "1":  # orden de reestablecer
        print("reestableciendo")


    elif lista_movimiento[0] == "2": # orden de crear Token
        print("creo token y espero otra orden")

        print(lista_movimiento[1])

    elif lista_movimiento[0] == "3": # orden de mover token

       print("muevo token y espero otra orden")

def envia_orden():
    respuesta = conexion.recv(1024)
    print(respuesta.decode('utf-8'))

    orden = input()

    if orden.split()[0] == "1":
        print("restablece puntos de accion")
    elif orden.split()[0] == "2":
        orden = "2 oso 346 309"
        print("creo token de oso")
    elif orden.split()[0] == "3":
        orden = "3 346 309 396 309"
        print("muevo el oso a la derecha")
    conexion.send(orden.encode('utf-8'))
    if orden == "salir":
        conexion.close()
        quit()
    pass


while True:
    if jugador1.puntosDeAccion[0]!=0:
        recibe_orden()
    elif jugador1.puntosDeAcction[0]==0:
        envia_orden()


