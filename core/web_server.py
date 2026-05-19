import asyncio
import websockets

class WebServer:
    def __init__(self, game_loop):
        self.game = game_loop
        
    async def handler(self, websocket, path):
        await websocket.send("Connected")
        
    def run(self):
        start_server = websockets.serve(self.handler, "localhost", 8765)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()
        
    async def check_shutdown(self):
        await asyncio.sleep(1)