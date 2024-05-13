from modules import *

class tunnel:
    def __init__(self,Server,user=""):
        self.Server = Server
        self.user = user
        self.tunnel = None
        self.get = requests.get
        self.post = requests.post
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
            r = self.get(f"http://localhost:{port}/")
            if r.status_code == 200:
                return True
            return False
        except requests.exceptions.ConnectionError:
            return False
    def get_messages(self):pass
    def send_message(self):pass