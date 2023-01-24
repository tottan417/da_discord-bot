# インストールした discord.py を読み込む
from discord.ext import tasks
import discord
import config
import time

# 自分のBotのアクセストークンに置き換えてください
TOKEN = config.TOKEN

# 接続に必要なオブジェクトを生成
client = discord.Client(intents=discord.Intents.all())

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    print("アクションの実行", time.time())
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「/neko」と発言したら「にゃーん」が返る処理
    if message.content == '/neko':
        await message.channel.send('にゃーん')

@tasks.loop(seconds=10)
async def send_message_every_10sec():
    print(time.time())

# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)