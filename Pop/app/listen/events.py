from .. import socket


@socket.on('connect')
def user_connected():
    socket.emit('message', {"msg": "[CONNECTED]"})


# Receiving any kind of message gets relayed back to everyone (for now).
@socket.on('message')
def message_received(json):
    socket.emit('message', json)
