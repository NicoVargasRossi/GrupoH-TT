from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8000))
print("cliente basico")

while True:
    respuesta = s.recv(1024)
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
    s.send(orden.encode('utf-8'))



    if orden == "salir":
        break

s.close()
