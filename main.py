import asyncio
import sys
import threading
import os
import logging
from dotenv import load_dotenv

# Configurar Log Automático em Arquivo
logging.basicConfig(
    filename='error_log.txt',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# ... (Resto do seu código main.py mantendo os imports seguros)
# Certifique-se de que os imports estão dentro de try/except se forem opcionais

def main():
    try:
        load_dotenv()
        print("🚀 Iniciando TFT AI Overlay Pro...")
        
        # Imports seguros
        try:
            from core.config_manager import ConfigManager
            from core.web_server import WebServer
            from core.game_loop import GameLoop
            from core.voice_manager import VoiceManager
            from core.health_reporter import HealthReporter
        except ImportError as e:
            logging.error(f"Falha crítica na importação: {e}")
            print(f"❌ Erro ao carregar módulos: {e}")
            print("Verifique o arquivo error_log.txt")
            input("Pressione Enter para sair...")
            return

        config = ConfigManager()
        reporter = HealthReporter(config)
        voice = VoiceManager(config)
        game = GameLoop(config, voice) # Simplificado para teste
        server = WebServer(game)
        
        # Threads
        t_game = threading.Thread(target=game.run, daemon=True)
        t_server = threading.Thread(target=server.run, daemon=True)
        
        t_game.start()
        t_server.start()
        
        print("✅ SISTEMA RODANDO! Verifique a área de trabalho ou o navegador.")
        
        while True:
            time.sleep(1)
            
    except Exception as e:
        logging.error(f"Erro fatal na execução: {e}", exc_info=True)
        print(f"❌ Ocorreu um erro inesperado: {e}")
        print("Detalhes salvos em error_log.txt")
        input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()
