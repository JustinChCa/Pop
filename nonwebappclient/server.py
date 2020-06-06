from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread
import time


def wait_for_connections():
    """
    Handles incoming connections
    """
    run = True
    while run:
        try:
            client, addr = SERVER.accept()
            print(
                f"[CONNECTION] {addr} connected to the server at {time.time()}")
            addresses[client] = addr
            Thread(target=new_client, args=(client, addr)).start()
        except Exception as e:
            print("[ERROR]", e)
            run = False

    print("SERVER CRASHED")


def new_client(client: socket, addr):
    """
    Handles a single client
    """
    client.send(bytes("Welcome to Pop" +
                      "Type a screen name and press enter!", "utf8"))
    name = client.recv(BUFF_SIZE).decode("utf8")
    w_msg = f"Welcome to Pop {name}, if you ever want to quit, type {{quit}}!"
    client.send(bytes(w_msg, "utf8"))
    b_msg = f"{name} has joined the server."
    broadcast(bytes(b_msg, "utf8"))
    clients[client] = name
    run = True
    while run:
        msg = client.recv(BUFF_SIZE)
        if msg != bytes(f"{{quit}}", "utf8"):
            broadcast(msg, f"{name}: ")
        else:
            client.close()
            del clients[client]
            broadcast(bytes(f"{name} has left the server", "utf8"))
            print(
                f"[EXIT] {addr} {name} has left the server at {time.time()}")
            run = False


def broadcast(msg, prefix=""):
    """
    Broadcasts msg to all clients currently on the server.
    Assumes msg is already byte encoded
    """
    for client in clients:
        client.send(bytes(prefix, "utf8") + msg)


HOST = "127.0.0.1"
PORT = 6050
ADDR = (HOST, PORT)
BUFF_SIZE = 1024
SERVER = socket(AF_INET, SOCK_STREAM)
SERVER.bind(ADDR)
clients = {}
addresses = {}

if __name__ == "__main__":
    SERVER.listen(5)
    print("Waiting for connection...")
    INCOMING_THREAD = Thread(target=wait_for_connections)
    INCOMING_THREAD.start()
    INCOMING_THREAD.join()
    SERVER.close()
