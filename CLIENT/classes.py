from modules import *

class tunnel:
    def __init__(self,Server,user=""):
        self.Server = Server
        self.user = user
        self.tunnel = None
    def spawn(self):
        # Create a tunnel to the server
        self.tunnel = subprocess.Popen(['ssh' ,'-L',f'{port}:localhost:{port}', f'{self.user}@{self.Server}',f'python3 TunnelChat/SERVER/server.py {port}'])
    def kill(self):
        self.tunnel.kill()
    def ping(self):
        # Check if the tunnel is still alive
        if self.tunnel.poll() is not None:
            self.spawn()
        try:
            r = self.post(f"http://localhost:{port}/")
            if r.status_code == 200:
                return True
            return False
        except requests.exceptions.ConnectionError:
            return False
    def get_messages(self):
        text = self.post(f"http://localhost:{port}/messages",data={"user":self.user}).text
        print(text)
        return eval(text)
    def send_message(self,message):
        self.post(f"http://localhost:{port}/send",data={"message":message,"user":self.user})
    def register_user(self):
        self.post(f"http://localhost:{port}/register",data={"user":self.user})
    def logout(self):
        self.post(f"http://localhost:{port}/logout",data={"user":self.user})
        self.kill()

    def post(self,url,data):
        return requests.post(url,json=data)