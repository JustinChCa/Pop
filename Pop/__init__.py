from flask import Flask
from flask_socketio import SocketIO
from .app import create_app

app = create_app()
socket = SocketIO(app)


@socket.on('connect')
def user_connected():
    socket.emit('message', {"msg": "[CONNECTrED]"})


# Receiving any kind of message gets relayed back to everyone (for now).
@socket.on('message')
def message_received(json):
    socket.emit('message', json)


if __name__ == "__main__":
    socket.run(app, debug=False)
