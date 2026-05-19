import asyncio
import sys
import threading
import os
import time
from dotenv import load_dotenv

# Imports dos módulos locais
try:
    from core.config_manager import ConfigManager
    from core.web_server import WebServer
    from core.game_loop import GameLoop
    # Importe outros módulos conforme necessário
except ImportError as e:
    print(f"❌ Erro ao importar módulos: {e}")
    sys.exit(1)

def main():
    print("🚀 Iniciando TFT AI Overlay Pro...")
    load_dotenv()
    
    # Verificar .env
    if not os.path.exists(".env"):
        print("❌ Arquivo .env não encontrado. Execute o installer.bat novamente.")
        return

    config = ConfigManager()
    print("✅ Config Manager OK")
    
    # Inicializar Loop do Jogo (Backend)
    game = GameLoop(config) 
    print("🎮 Loop do jogo iniciado...")
    
    # Inicializar Servidor Web (Frontend/HUD)
    server = WebServer(game)
    
    # Rodar o servidor em uma thread separada para não travar o console
    t_server = threading.Thread(target=server.run, daemon=True)
    t_server.start()
    
    print("🟢 SISTEMA RODANDO COM SUCESSO!")
    print("📡 Conectando à API da Riot...")
    print("💡 Se o navegador não abriu, verifique se há pop-ups bloqueados.")
    
    try:
        while True:
            time.sleep(1)
            # Aqui entraria a lógica principal do jogo
    except KeyboardInterrupt:
        print("\n🛑 Encerrando sistema...")
        sys.exit(0)

if __name__ == "__main__":
    main()
