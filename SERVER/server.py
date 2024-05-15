from classes import *
app = flask.Flask(__name__)

messages = [Message("Hello","Master","Global")]

users = []

@app.route('/')
def root():
    return " ",200

@app.route('/messages', )
def get_messages():
    msgs = [msg.visable_str() for msg in messages] if 'user' in flask.request.data else [msg.anon_str() for msg in messages]
    return str(msgs)

@app.route('/register', )
def register():
    user = flask.request.form['user']
    users.append(user)
    return f"Registered as {user} <meta http-equiv='refresh' content='2;url=/messages'>", 200

@app.route('/logout', )
def logout():
    if not 'user' in flask.request.data:
        return " ", 405
    if not flask.request.data['user'] in users:
        return " ", 405
    users.remove(flask.request.data['user'])
    return " ", 200

@app.route('/send', )
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
if len(args) > 1:
    port = args[1]
else:
    port = 6060
app.run("0.0.0.0",port)