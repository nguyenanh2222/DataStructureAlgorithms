import socket
from _ast import List
from selectors import SelectorKey
from threading import Thread
from typing import Tuple, Union

from select import select

from oop.Server.Base.selecter import DefaultSelector


class BaseSocket:

    def __init__(self):
        ...

    def run(self):
        ...


class Socket(BaseSocket, Thread):

    def __init__(self, server="127.0.0.1", port=6666):
        super().__init__()
        self.server = server
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.server, self.port))
        self.socket.listen()
        self.con = {}

    def run(self):
        while True:

            x, y, z = select([self.socket], self.con, [])
            if x:
                con, address = self.socket.accept()
                self.con[con.fileno()] = con
                print("connect")
            elif y:
                a = self.con[y[0]].recv(1024)
                print(a)
                if not a:
                    print("ok")
                    self.con.pop((y[0]))
            print("con:  " ,  self.con)
            # con, address = self.socket.accept()
            # self.con.append(con)
            # x, y, z = select([self.socket], self.con, [])
            # print(x,y,z)
            # x, y, z = select([self.socket], self.con, [])
            # print(x,y,z)
            # con.sendall("hello")
            # x, y, z = select([self.socket], self.con, [])
            # print(x, y, z)

        # with con:
        #     while True:
        #         data = con.recv(1024)
        #         if not data:
        #             break
