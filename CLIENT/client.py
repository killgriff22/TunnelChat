from classes import *
Tunnel = tunnel("x-x.ftp.sh","skye")
Tunnel.spawn()
def Exit():
    Tunnel.kill()
atexit.register(Exit)

while not Tunnel.ping():
    pass
print("Made connection to server")