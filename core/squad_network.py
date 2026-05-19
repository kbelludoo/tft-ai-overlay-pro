import requests
import threading
import time

class SquadNetwork:
    def __init__(self, config):
        self.config = config
        self.connected = False
        self.teammates = []
        
    def create_room(self):
        code = "TFT-" + str(time.time())[-6:].replace('.', '').upper()
        print(f"🟢 Sala Criada: {code}")
        self.connected = True
        return code
        
    def join_room(self, code):
        print(f"🔵 Entrando na sala: {code}")
        self.connected = True
        # Lógica de conexão P2P simulada
        self.teammates = ["Player2", "Player3"]
        
    def sync_data(self):
        if not self.connected: return
        # Envio de dados criptografados para o squad