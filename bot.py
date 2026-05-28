import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

intents = discord.Intents.default()
intents.voice_states = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

PARTY_CHANNELS = {
    1479870047311761428,
    937927167994630208,
    937927788973944842
}

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_voice_state_update(member, before, after):
    if member.bot:
        return

    if after.channel is not None:

        channel = after.channel

        if channel.id in PARTY_CHANNELS:

            if len(channel.members) == 1:

                announcements = discord.utils.get(
                    member.guild.text_channels,
                    name="announcements"
                )

                if announcements:
                    embed = discord.Embed(
                        title="🎮 Party Started!",
                        description=(
                            f"**{member.display_name}** has started a party in "
                            f"**{channel.name}**"
                        ),
                        color=discord.Color.blue()
                    )
                    await announcements.send("@everyone", embed=embed)

bot.run(TOKEN)