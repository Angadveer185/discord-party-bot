import discord
from discord.ext import commands
import os

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.voice_states = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

PARTY_CHANNELS = {
    "party-1-🎧",
    "party-2-🎧",
    "party-3-🎧"
}

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_voice_state_update(member, before, after):

    if after.channel is not None:

        channel = after.channel

        if channel.name in PARTY_CHANNELS:

            if len(channel.members) == 1:

                announcements = discord.utils.get(
                    member.guild.text_channels,
                    name="announcements"
                )

                if announcements:
                    await announcements.send(
                        f"@everyone 🎮 "
                        f"**{member.display_name}** started a party in "
                        f"**{channel.name}**!"
                    )

bot.run(TOKEN)