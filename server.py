from flask import Flask, render_template
from flask_socketio import SocketIO, emit
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'my_secret_key')
socketio = SocketIO(app)
print(os.environ.get('SECRET_KEY'))
messages = []

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@socketio.on('message')
def handle_message(message):
    messages.append(message)
    emit('message', message, broadcast=True)

# Auto-opening the app in Replit's web viewer
if __name__ == '__main__':
    app.run()
