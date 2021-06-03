from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 8000))
print("cliente basico")

while True:
    respuesta = s.recv(1024)
    print(respuesta.decode('utf-8'))

    orden = input()

    if orden.split()[0] == "1":
        orden = "1 mono 3 Escabullirse 15 346 309 2 Normal Bosque"

    s.send(orden.encode('utf-8'))

    if orden == "salir":
        break

s.close()
