import asyncio
from threading import Thread
import discord
from discord.ext import commands
from flask import Flask

app = Flask('')


@app.route('/')
def home():
  return 'OK'


def run():
  app.run(host='0.0.0.0', port=10000)


def keep_alive():
  t = Thread(target=run)
  t.start()


keep_alive()

bot = commands.Bot(command_prefix='!', self_bot=True)

VOICE_CHANNEL_ID = 1342450813741695051
TOKEN = (
    'MTU1OTYwNTcxMjgwMjQyMjg0Nw.G4pJuY._YGR0EeS8rIiY_Js6v4fuJjOmUVkqjKuWLPgzQ'
)


@bot.event
async def on_ready():
  print(f'Зашел как: {bot.user}')
  await bot.change_presence(status=discord.Status.online, activity=None)

  channel = bot.get_channel(VOICE_CHANNEL_ID)
  if channel:
    try:
      vc = await channel.connect(self_mute=True, self_deaf=True)
      print(f'Успешно зашел в канал: {channel.name}')
      while True:
        await asyncio.sleep(30)
        if not vc.is_connected():
          print('Соединение потеряно. Переподключаюсь...')
          vc = await channel.connect(self_mute=True, self_deaf=True)
    except Exception as e:
      print(f'Ошибка: {e}')
  else:
    print('Голосовой канал не найден!')


bot.run(TOKEN)
