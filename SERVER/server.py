from classes import *
app = flask.Flask(__name__)

messages = [Message("Hello","Master","Global")]

users = []

@app.route('/')
def root():
    return " ",200

@app.route('/messages', methods=['POST'])
def messages():
    msgs = [msg.visable_str() if ('user' in flask.request.data and flask.request.data['user'] in users) else msg.anon_str() for msg in messages ]
    return str(msgs)

@app.route('/register', methods=['POST'])
def register():
    user = flask.request.form['user']
    return f"Registered as {user} <meta http-equiv='refresh' content='2;url=/messages'>"

@app.route('/logout', methods=['POST'])
def logout():
    if not 'user' in flask.request.data:
        return " ", 405
    if not flask.request.data['user'] in users:
        return " ", 405
    users.remove(flask.request.data['user'])
    return " ", 200

@app.route('/send', methods=['POST'])
def send():
    message = flask.request.data['message']
    sender = flask.request.data['user']
    if not 'user' in flask.request.data:
        return " ", 405
    if not flask.request.data['user'] in users:
        return " ", 405
    receiver = "Global"
    messages.append(Message(message,sender,receiver))
    return " ", 200

app.run("0.0.0.0",6060)