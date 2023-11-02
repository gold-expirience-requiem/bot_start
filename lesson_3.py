import discord
from lesson2 import gen_pass

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642")
    elif message.content.startswith('$password'):
        await message.channel.send(gen_pass(10))
    else:
        await message.channel.send(message.content)

client.run("MTE2ODkwNjE0MzE5Njc4MjY3NA.GQrg4c.3oSMwHqPN3Nm6r_c4mDZOeRVneLagTKql5vJ0U")
