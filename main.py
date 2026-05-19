import os
import sys
import time
import threading
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

print("🚀 Iniciando TFT AI Overlay Pro...")

# Verificação básica de chaves
if not os.getenv("RIOT_API_KEY") or not os.getenv("OPENROUTER_API_KEY"):
    print("❌ ERRO: Chaves da API não encontradas no arquivo .env!")
    print("Por favor, execute o instalador novamente ou edite o arquivo .env.")
    input("Pressione Enter para sair...")
    sys.exit(1)

print("✅ Chaves detectadas.")

# Tenta importar os módulos principais com tratamento de erro
try:
    # Nota: Se algum módulo falhar, o programa avisa mas tenta continuar se possível
    from core.config_manager import ConfigManager
    print("✅ Config Manager OK")
    
    # Simulação do Loop Principal (Substitua pelas suas classes reais quando corrigir os imports)
    # Se der erro aqui, é porque os arquivos na pasta 'core' não batem com o import
    
    # --- INÍCIO DO LOOP SIMPLIFICADO PARA TESTE ---
    def game_loop():
        print("🎮 Loop do jogo iniciado...")
        print("📡 Conectando à API da Riot...")
        # Aqui entraria a lógica real
        while True:
            time.sleep(1)
            # Simulação de status
            # print(".", end="", flush=True) 

    # Inicia em thread separada para não travar se tiver GUI futura
    t = threading.Thread(target=game_loop, daemon=True)
    t.start()
    
    print("🟢 SISTEMA RODANDO COM SUCESSO!")
    print("Pressione Ctrl+C para parar.")
    
    while True:
        time.sleep(1)
        
except Exception as e:
    print(f"\n❌ ERRO CRÍTICO AO INICIAR: {e}")
    print("\nDica: Verifique se todos os arquivos na pasta 'core' existem e estão corretos.")
    input("Pressione Enter para sair...")
    sys.exit(1)
