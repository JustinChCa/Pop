from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

HOST = '127.0.0.1'
PORT = 6050
ADDR = (HOST, PORT)
BUFF_SIZE = 1024
SERVER = socket(AF_INET, SOCK_STREAM)
msg_list = []


def receive():
    run = True
    while run:
        try:
            msg = SERVER.recv(BUFF_SIZE).decode("utf8")
            print(msg)
        except OSError:
            break
        except Exception as e:
            print("[ERROR]", e)
            run = False
            print("CLIENT CRASHED")

    print("CONNECTION TERMINATED")


def send():
    run = True
    while run:
        try:
            msg = input()
            SERVER.send(bytes(msg, "utf8"))
            if msg == f"{{quit}}":
                SERVER.close()
                run = False
        except Exception as e:
            print("[ERROR]", e)
            run = False
            print("CLIENT CRASHED")
            print("CONNECTION TERMINATED")


if __name__ == "__main__":
    SERVER.connect(ADDR)
    RECIEVING_THREAD = Thread(target=receive)
    RECIEVING_THREAD.start()
    send()
