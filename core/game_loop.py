class GameLoop:
    def __init__(self, config, voice, squad):
        self.config = config
        self.voice = voice
        self.squad = squad
        
    def run(self):
        self.voice.start_listening()
        print("🎮 Loop do jogo iniciado. Aguardando dados da Riot API...")
        while True:
            # Lógica principal do jogo
            pass