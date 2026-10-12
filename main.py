import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import discord

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is active!")

def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHTTPRequestHandler)
    server.serve_forever()

threading.Thread(target=run_web_server, daemon=True).start()

TOKEN = os.environ.get("DISCORD_TOKEN")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Запущен как {self.user}')
        game = discord.Game(name="moscowsociety бог дискорда")
        await self.change_presence(status=discord.Status.online, activity=game)
        print("Статус CS2 успешно установлен!")

client = MyClient()
if TOKEN:
    client.run(TOKEN)
