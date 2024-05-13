from classes import *
Tunnel = tunnel("x-x.ftp.sh","skye")
Tunnel.spawn()
def Exit():
    Tunnel.logout()
atexit.register(Exit)

while not Tunnel.ping():
    pass
for msg in Tunnel.get_messages():
    print(msg)