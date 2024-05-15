from classes import *
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()
app = flask.Flask(__name__)

messages = [Message("Hello","Master","Global")]

users = []

exit_flag = False

@app.route('/')
def root():
    return " ",200

@app.route('/messages', )
def get_messages():
    msgs = []
    if not 'user' in flask.request.data or not flask.request.data['user'] in users:
        for msg in messages:
            msgs.append(msg.anon_str())
    else:
        for msg in messages:
            msgs.append(msg.visivle_str())
    return str(msgs)

@app.route('/register', )
def register():
    user = flask.request.form['user']
    users.append(user)
    return " ", 200

@app.route('/logout', )
def logout():
    if not 'user' in flask.request.data:
        return " ", 405
    if not flask.request.data['user'] in users:
        return " ", 405
    users.remove(flask.request.data['user'])
    if len(users) == 0:
        shutdown_server()
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