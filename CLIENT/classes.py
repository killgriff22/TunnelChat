from modules import *

class tunnel:
    def __init__(self,Server,user=""):
        self.Server = Server
        self.user = user
        self.register_user()
        self.tunnel = None
    def spawn(self):
        # Create a tunnel to the server
        self.tunnel = subprocess.Popen(['ssh', '-N' ,'-L',f'{port}:localhost:{port}', f'{self.user}@{self.Server}'])
    def kill(self):
        self.tunnel.kill()
    def ping(self):
        # Check if the tunnel is still alive
        if self.tunnel.poll() is not None:
            self.spawn()
        try:
            r = requests.get(f"http://localhost:{port}/")
            if r.status_code == 200:
                return True
            return False
        except requests.exceptions.ConnectionError:
            return False
    def get_messages(self):
        return eval(requests.get(f"http://localhost:{port}/messages").text,data={"user":self.user})
    def send_message(self,message):
        requests.post(f"http://localhost:{port}/send",data={"message":message,"user":self.user})
    def register_user(self):
        requests.post(f"http://localhost:{port}/register",data={"user":self.user})
    def logout(self):
        requests.post(f"http://localhost:{port}/logout",data={"user":self.user})
        self.kill()