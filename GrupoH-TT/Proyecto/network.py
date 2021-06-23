import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.server = "10.42.0.80"
        self.port = 5555
        self.addr = (self.server, self.port)
        print("esto es antes de declarar pos")
        self.pos = self.connect()
        print("aca ya declare pos", self.pos)


    def getPos(self):
        return self.pos

    def connect(self):
        try:
            self.client.connect(self.addr)
            auxstr = self.client.recv(2048).decode()
            print("la str auxiliar es: ", auxstr)
            return auxstr
        except:

            pass

    def send(self,data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print("e")

n = Network ()
print(n.send("Hello"))
print(n.send("Working"))