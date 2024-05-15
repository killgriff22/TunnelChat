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

@app.route('/',methods=['POST','GET'])
def root():
    return " ",200

@app.route('/messages', methods=['POST','GET'])
def get_messages():
    msgs = []
    if not 'user' in flask.request.json or not flask.request.json['user'] in users:
        for msg in messages:
            msgs.append(msg.anon_str())
    else:
        for msg in messages:
            msgs.append(msg.visivle_str())
    return str(msgs)

@app.route('/register', methods=['POST','GET'])
def register():
    user = flask.request.json['user']
    users.append(user)
    return " ", 200

@app.route('/logout', methods=['POST','GET'])
def logout():
    if not 'user' in flask.request.json:
        return " ", 405
    if not flask.request.json['user'] in users:
        return " ", 405
    users.remove(flask.request.json['user'])
    if len(users) == 0:
        shutdown_server()
    return " ", 200

@app.route('/send', methods=['POST','GET'])
def send():
    message = flask.request.json['message']
    sender = flask.request.json['user']
    if not 'user' in flask.request.json:
        return " ", 405
    if not flask.request.json['user'] in users:
        return " ", 405
    receiver = "Global"
    messages.append(Message(message,sender,receiver))
    return " ", 200
if len(args) > 1:
    port = args[1]
else:
    port = 6060
app.run("0.0.0.0",port)