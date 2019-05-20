import socket
import threading
import sys


class server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    conn = []
    def __init__(self):
        self.sock.bind(('192.168.1.179',8000))
        self.sock.listen(1)

    def Manipular_mensagens(self, c, a):
        while True:
            data = c.recv(1024)
            for conecao in self.conn:
                conecao.send(data)
            if not data:
                break

    def executar(self):
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target=self.Manipular_mensagens, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.conn.append(c)
            print(str(a[0]) + ":" + str(a[1]), "conectado")


class Cliente:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def __init__(self, adress):
        self.sock.connect((adress,5000))

        iThread = threading.Thread(target=self.MANDAR_MENSAGEM)
        iThread.deamon = True
        iThread.start()

        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(data)

    def MANDAR_MENSAGEM(self):

        while True:
            self.sock.send(bytes(input(), "utf-8"))


if __name__ == '__main__':

    if (len(sys.argv) > 1 ):
        cliente = Cliente(sys.argv[1])
    else:
        Servidor = server()
        Servidor.executar()
