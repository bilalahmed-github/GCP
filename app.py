from flask import Flask, rendertemplate
from flasksocketio import SocketIO, emit

app = Flask(name)
socketio = SocketIO(app, corsallowedorigins='*')

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('ping')
def handle_message(data):
    emit('pong', room=request.sid)

if __name == '__main':
    socketio.run(app, host='0.0.0.0', port=80)
