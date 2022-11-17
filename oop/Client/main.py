import socket

import orjson

from oop.Client.model.User.model import UserLogin

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 6666  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    user_login = UserLogin(
        username="sang01",
        password="123")

    s.sendall(orjson.dumps(user_login.dict()))
    mess = s.recv(1024)
    print(mess)
    # data = s.recv(1024)