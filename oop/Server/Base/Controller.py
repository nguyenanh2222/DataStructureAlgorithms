import socket

from oop.Server.Base.selecter import DefaultSelector


class BaseSocket:

    def __init__(self):
        ...

    def run(self):
        ...


class Socket(BaseSocket):

    def __init__(self, server="127.0.0.1", port=6543):
        super().__init__()
        self.server = server
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.server, self.port))
        self.socket.listen()

    def run(self):
        con, address = self.socket.accept()
        print(con)
        with con:
            while True:
                data = con.recv(1024)
                if not data:
                    break