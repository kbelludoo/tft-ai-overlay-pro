import asyncio
import websockets
import webbrowser
import time
import os

# HTML Simples do HUD (Interface Gráfica)
HTML_HUD = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>TFT AI Overlay - kbelludoo</title>
    <style>
        body { background-color: rgba(0, 0, 0, 0.85); color: #00ffcc; font-family: 'Segoe UI', sans-serif; margin: 0; overflow: hidden; }
        #overlay { position: absolute; top: 20px; right: 20px; width: 300px; padding: 20px; border: 2px solid #00ffcc; border-radius: 10px; background: rgba(20, 20, 30, 0.9); }
        h2 { margin-top: 0; text-align: center; }
        .status { color: #0f0; font-weight: bold; }
        .advice { font-size: 1.2em; margin: 20px 0; min-height: 60px; }
        .btn { display: block; width: 100%; padding: 10px; margin: 5px 0; background: #00ffcc; color: #000; border: none; cursor: pointer; font-weight: bold; }
        .btn:hover { background: #fff; }
    </style>
</head>
<body>
    <div id="overlay">
        <h2>🎮 TFT AI Coach</h2>
        <p>Status: <span class="status">● Online</span></p>
        <p>Jogador: <strong>kbelludoo III</strong></p>
        <div id="advice" class="advice">Aguardando início da partida...</div>
        <button class="btn" onclick="speak()">🔊 Ouvir Dica</button>
        <button class="btn" onclick="toggleSquad()">🤝 Modo Squad</button>
    </div>
    <script>
        function speak() { alert('Dica: Foque em economia até o round 10!'); }
        function toggleSquad() { alert('Modo Squad Ativado! Conecte-se com seus amigos.'); }
    </script>
</body>
</html>
"""

class WebServer:
    def __init__(self, game_loop):
        self.game = game_loop
        self.clients = set()
        
    async def handler(self, websocket, path):
        self.clients.add(websocket)
        try:
            await websocket.send("CONNECTED")
            async for message in websocket:
                print(f"Comando recebido: {message}")
        finally:
            self.clients.discard(websocket)
            
    def run(self):
        # 1. Salvar o HTML temporário
        with open("hud_temp.html", "w", encoding="utf-8") as f:
            f.write(HTML_HUD)
        
        # 2. Abrir o Navegador Automaticamente
        print("🌐 Abrindo Interface Gráfica (HUD)...")
        webbrowser.open(os.path.abspath("hud_temp.html"))
        
        # 3. Iniciar Servidor WebSocket
        start_server = websockets.serve(self.handler, "localhost", 8765)
        asyncio.get_event_loop().run_until_complete(start_server)
        print("✅ Servidor WebSocket ativo na porta 8765")
        asyncio.get_event_loop().run_forever()
        
    async def check_shutdown(self):
        await asyncio.sleep(1)
