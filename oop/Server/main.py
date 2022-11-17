from oop.Server.Base.BaseSocket import  Socket
import logging

#
if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    server = Socket()
    server.build()

