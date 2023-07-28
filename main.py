# 1°: Importa o Flask
from flask import Flask, render_template
from flask_socketio import SocketIO, send

# 2°: Cria seu app: app = Flask(__name__)
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

#Funcionalidade de enviar mensagem
@socketio.on("message")
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

# 3°: Cria 1° página/1° rota
@app.route("/")
def homepage():
    return render_template("index.html")

# 4°: Roda o app
socketio.run(app, host="192.168.18.6") 