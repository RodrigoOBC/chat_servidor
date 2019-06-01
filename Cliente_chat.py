import socket
import threading
import sys


class Cliente:
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    def __init__(self, adress):
        self.sock.connect((adress,5000))

        iThread = threading.Thread(target=self.MANDAR_MENSAGEM)
        iThread.deamon = True
        iThread.start()

        while True:
            data = self.sock.recv(1024)
            print(f"mensagem enviada = {str(data)}")

    def MANDAR_MENSAGEM(self):

        while True:
            valor = input()
            if valor == "sair":
                self.sock.send(bytes(valor, "utf-8"))
                sys.exit(True)
            else:
                self.sock.send(bytes(valor, "utf-8"))


if __name__ == '__main__':
    cliente = Cliente(input("coloque o ip do sevidor: \n"))