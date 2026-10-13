import os import asyncio import threading from flask import Flask import discord
app = Flask(name)
@app.route('/') def home(): return "Bot is alive!", 200
def run_flask(): port = int(os.environ.get("PORT", 10000)) app.run(host='0.0.0.0', port=port)
class MyClient(discord.Client): async def on_ready(self): print(f'Зашел как: {self.user}') await self.connect_voice()
async def connect_voice(self):
    channel_id = 1342450813741695051
    channel = self.get_channel(channel_id)
    if not channel:
        try:
            channel = await self.fetch_channel(channel_id)
        except Exception as e:
            print(f"Ошибка поиска канала: {e}")
            return

    if channel:
        try:
            await channel.connect(self_mute=True, self_deaf=True)
            print(f"Успешно зашел в канал: {channel.name}")
        except Exception as e:
            print(f"Ошибка подключения к голосовому каналу: {e}")
client = MyClient()
if name == "main": threading.Thread(target=run_flask, daemon=True).start() token = os.getenv('TOKEN') if token: client.run(token) else: print("ОШИБКА: Переменная TOKEN не найдена!")
