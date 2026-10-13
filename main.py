import os
import asyncio
import threading
from flask import Flask
import discord

app = Flask(__name__)

@app.route('/')
def home():
    return "OK", 200

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)

client = discord.Client()

@client.event
async def on_ready():
    print(f"DEBUG: Logged in as {client.user}", flush=True)
    await asyncio.sleep(5)
    
    channel_id = 1342451073335693333
    channel = client.get_channel(channel_id)
    if not channel:
        try:
            channel = await client.fetch_channel(channel_id)
        except Exception as e:
            print(f"ERROR fetching channel: {e}", flush=True)
            return

    if channel:
        try:
            await channel.connect(self_mute=True, self_deaf=True)
            print(f"SUCCESS: Connected to voice channel: {channel.name}", flush=True)
        except Exception as e:
            print(f"ERROR connecting to voice: {e}", flush=True)

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    token = os.getenv('TOKEN')
    if token:
        client.run(token)
    else:
        print("TOKEN NOT FOUND")
