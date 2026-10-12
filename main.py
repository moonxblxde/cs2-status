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
APP_ID = 1559310882415054968

class MyClient(discord.Client):
    async def on_ready(self):
        activity = discord.Activity(
            type=discord.ActivityType.playing,
            name="moscowsociety ebawit",
            application_id=APP_ID,
            details="лучший",
            state="из лучших",
            assets={
                "large_image": "logo",
                "large_text": "Counter-Strike 2"
            }
        )
        await self.change_presence(status=discord.Status.online, activity=activity)

client = MyClient()

if TOKEN:
    client.run(TOKEN)
