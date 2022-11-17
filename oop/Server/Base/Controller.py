import socket
from threading import Thread
import logging
import time
import orjson
from select import select

from oop.Server.Base.selecter import DefaultSelector


class BaseSocket:

    def __init__(self):
        ...

    def build(self):
        ...


class Socket(BaseSocket):

    def __init__(self, server="127.0.0.1", port=6666):
        super().__init__()
        self.server = server
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.server, self.port))
        self.socket.listen()
        self.con = {}
        self.state = [False, False]
        # self.accepct_service = None

    def build(self):
        logging.info(f"SERVER: {self.server}:{self.port}")
        Thread(target=self.accepct).start()
        while True:
            time.sleep(2)
            print(".....")

    def accepct(self):
        self.state[0] = True
        another_user = {}
        while self.state[0]:
            x, y, z = select([self.socket], another_user, [], 0.2)
            if x:
                con, address = self.socket.accept()
                another_user[con.fileno()] = con
                logging.info(f"Client {con.fileno()}: connect")
            if y:
                mess = self.recv(another_user[y[0]])
                logging.info(f"Client {y[0]} tell {mess}")
                #Handle Login
                                

                if not mess:
                    logging.info(f"Client {y[0]} Disconnect")
                    another_user.pop((y[0]))

    def handle_event(self, y):
        mess = self.con[y[0]].recv(1024)
        logging.info(f"Client {y[0]} tell {mess}")
        if not mess:
            logging.info(f"Client {y[0]} Disconnect")
            self.con.pop((y[0]))

    def recv(self, client) -> orjson:
        mess = client.recv(1024)
        return orjson.loads(mess)
