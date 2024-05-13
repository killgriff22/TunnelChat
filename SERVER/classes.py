from modules import *

class Message:
    def __init__(self, message, sender, receiver):
        self.message = message
        self.sender = sender
        self.receiver = receiver
    def visable_str(self):
        return f"{self.sender} -> {self.receiver}: {self.message}"
    def anon_str(self):
        return f"Anon -> {self.receiver}: {self.message}"