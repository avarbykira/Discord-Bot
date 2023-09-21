# bot_mk2 is using slash command trigger, hence has a better UI when interacting.

import discord
import json
from discord import app_commands
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

with open('token.json', 'r') as json_file:
    token = json.load(json_file)
    discord_token = token["discord_token"]


@bot.event
async def on_ready():
    print("Bot is up!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)


@bot.tree.command(name="hello")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f"Hey {interaction.user.mention}! This is a slash command!", ephemeral=True)


@bot.tree.command(name="say")
@app_commands.describe(thing_to_say="What should I say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{interaction.user.name} said '{thing_to_say}'")


bot.run(discord_token)
