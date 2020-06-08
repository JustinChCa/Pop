from flask import Flask
from flask_socketio import SocketIO
from .app import create_app, socket

app = create_app()

if __name__ == "__main__":
    socket.run(app, debug=False, host="0.0.0.0", port="5000")
