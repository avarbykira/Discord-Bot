import json
import discord

import chatgpt


# save token in a json file to access
with open('token.json', 'r') as json_file:
    token = json.load(json_file)


def run_discord_bot():
    discord_token = token["discord_token"]
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    # this syntactic sugar means that when client.event execute at this certain point,
    # this function would be executed
    async def on_message(message):
        if message.author == client.user:
            return

        # username = str(message.author)
        # user_message = str(message.content)
        # channel = str(message.channel)

        if str(message.content)[0] == '#' or '-':
            # todo: use a list to contain all trigger characters, and be able to print them in 'help' module
            # activate bot
            await respond(message)

    client.run(discord_token)


async def respond(message):
    # input: -ai hello; output: ai hello
    user_message = (str(message.content).lower())[1:]
    # use following to debug
    username = str(message.author)
    channel = str(message.channel)

    print(f"{username} said: ’{user_message}‘ （{channel})")

    if user_message.startswith("ai"):
        tips = "Let me think so..."  # todo: more replies, ues a random function to choose one of them
        await message.channel.send(tips)

        # make calls
        prompt = chatgpt.get_prompt(user_message)
        print("prompt: " + prompt)

        if len(prompt) >= 2:
            output = chatgpt.get_output(prompt)
        else:
            output = ["What do you mean? I don't get it.", 0]

        reply = output[0]
        token_used = output[1]

        # format embedded reply in discord
        embed = discord.Embed(
            colour=discord.Colour.from_rgb(0, 166, 126),
            description=reply,
            title="Reply to \" " + prompt + " \""
        )
        # embed.add_field(name=reply, value="————")
        embed.set_footer(text="--- \n This message costs " + str(token_used) + " tokens")
        embed.set_thumbnail(url="https://raw.githubusercontent.com/avarbykira/img-bed/107e809437545fb4d2a474844d5719399e94f86c/openai-icon-png.png")

        await message.channel.send(embed=embed, reference=message)

    # if user_message.startswith(""):
