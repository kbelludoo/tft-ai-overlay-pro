import asyncio
import sys
import threading
import os
from dotenv import load_dotenv

# Imports seguros
try:
    from core.config_manager import ConfigManager
    from core.web_server import WebServer
    from core.game_loop import GameLoop
    from core.voice_manager import VoiceManager
    from core.squad_network import SquadNetwork
    from core.onboarding import Onboarding
    from core.health_reporter import HealthReporter
except ImportError as e:
    print(f"❌ Erro crítico ao importar módulos: {e}")
    print("💡 Dica: Execute o installer.bat novamente para reinstalar as dependências.")
    input("Pressione Enter para sair...")
    sys.exit(1)

def main():
    print("🚀 Iniciando TFT AI Overlay Pro...")
    load_dotenv()
    
    # Configuração automática segura (sem token hardcoded)
    if not os.getenv("GITHUB_TOKEN"):
        # Se não tiver token, o sistema roda mas não envia erros pro GitHub
        print("ℹ️ Token GitHub não encontrado. Erros serão salvos apenas localmente.")
    
    config = ConfigManager()
    
    # Onboarding se for primeira vez
    if config.is_first_run():
        print("🎓 Primeira execução detectada. Inicie o configurador...")
        # Nota: O onboarding agora é feito via GUI no installer, pulamos aqui se já tiver .env
        if not os.path.exists(".env"):
             import subprocess
             subprocess.run(["python", "config_gui.py"])
             load_dotenv() # Recarrega após configurar
    
    # Inicializar módulos
    try:
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
        
        print("✅ Sistema iniciado com sucesso!")
        print("🎙️ Diga 'Oi Overlay' para interagir (se microfone estiver ativo).")
        
        while True:
            asyncio.run(server.check_shutdown())
            
    except Exception as e:
        print(f"❌ Erro fatal na inicialização: {e}")
        reporter.report_error(e, "Startup")
        input("Pressione Enter para sair...")
        sys.exit(1)

if __name__ == "__main__":
    main()
