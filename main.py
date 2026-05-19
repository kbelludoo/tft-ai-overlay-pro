import asyncio
import sys
import threading
from core.config_manager import ConfigManager
from core.web_server import WebServer
from core.game_loop import GameLoop
from core.voice_manager import VoiceManager
from core.squad_network import SquadNetwork
from core.onboarding import Onboarding
from core.health_reporter import HealthReporter
from dotenv import load_dotenv

def main():
    load_dotenv()
    config = ConfigManager()
    
    # Onboarding se for primeira vez
    if config.is_first_run():
        onboarding = Onboarding(config)
        onboarding.run_wizard()
    
    # Inicializar módulos
    reporter = HealthReporter(config)
    squad = SquadNetwork(config)
    voice = VoiceManager(config)
    game = GameLoop(config, voice, squad)
    server = WebServer(game)
    
    # Threads
    t_game = threading.Thread(target=game.run, daemon=True)
    t_server = threading.Thread(target=server.run, daemon=True)
    
    t_game.start()
    t_server.start()
    
    print("✅ TFT AI Overlay Iniciado! (Modo Squad Ativo)")
    print("🎙️ Diga 'Oi Overlay' para começar.")
    
    try:
        while True:
            asyncio.run(server.check_shutdown())
    except KeyboardInterrupt:
        print("🛑 Encerrando...")
        reporter.send_final_summary()
        sys.exit(0)

if __name__ == "__main__":
    main()