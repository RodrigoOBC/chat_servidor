import socket
import threading
import sys


class server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM )
    conn = []
    def __init__(self):
        self.sock.bind(('0.0.0.0',5000))
        self.sock.listen(2)

    def Manipular_mensagens(self, c, a):
        while True:
            print(type(c))
            data = c.recv(1024)

            if data == bytes("sair", "utf-8"):
                print("saiu:"+str(a[1]))
                sys.exit(True)
            else:
                x = 0
                for conecao in self.conn:
                    if x > 0:
                        conecao.send(data)
                    x+=1
                x = 0

    def executar(self):
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target=self.Manipular_mensagens, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.conn.append(c)
            print(str(a[0]) + ":" + str(a[1]), "conectado")




if __name__ == '__main__':

    # if (len(sys.argv) > 1 ):
    #
    # else:
    Servidor = server()
    Servidor.executar()
