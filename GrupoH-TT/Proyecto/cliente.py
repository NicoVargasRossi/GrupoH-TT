from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.connect(('localhost', 8000))
print("cliente basico")

while True:
    respuesta = s.recv(1024)
    print(respuesta.decode('utf-8'))

    enviar = input()
    s.send(enviar.encode('utf-8'))

    if enviar == "salir":
        break


s.close()