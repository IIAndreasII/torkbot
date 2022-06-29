import os
import discord
import sys

from operator import concat

ARTIFACT_PATH = "E:\\source\\artifacts\\"

client = discord.Client()


@client.event
async def on_ready():
    print('Client logged in as {0.user}'.format(client))



@client.event
async def on_message(message):
    if message.author == client.user:
        return

    await handle_command(message)
    #if message.content.startswith('$hello'):   
        #await message.channel.send('Hello!')


async def handle_command(msg):
    cmd = msg.content
    if not cmd.startswith('>'):
        return

    if cmd == ">torka":
        await torka_ludvig(msg)

    if cmd == ">stats":
        await show_ludvig(msg)


async def torka_ludvig(msg):
    count = 0
    with open(concat(ARTIFACT_PATH, "ludvigcounter.txt")) as f:
        count = int(f.readline())
        count += 1
        f.close()
    with open(concat(ARTIFACT_PATH, "ludvigcounter.txt"), "w") as f:
        f.write(str(count))
        f.close()

    await msg.channel.send("```Ludvig torkad!```")

async def show_ludvig(msg):
    count = 0
    with open(concat(ARTIFACT_PATH, "ludvigcounter.txt")) as f:
        count = int(f.readline())
        f.close()
    
    out = "```Antal torkningar av Ludvig: {info}```"

    await msg.channel.send(out.format(info=count))



if __name__ == "__main__":

    #args = sys.argv

    print(concat(ARTIFACT_PATH, "ludvigcounter.txt"))
    tkn = ""
    with open(concat(ARTIFACT_PATH, "torkbot.txt")) as f:
        tkn = f.readlines()[0]
        f.close()

    if tkn != "":
        client.run(tkn)
    else:
        print("Could not find token...")