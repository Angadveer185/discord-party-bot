import discord
from discord.ext import commands
import os
import time
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

COOLDOWN = 10  # seconds

active_parties = set()
channel_cooldowns = {}


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.event
async def on_voice_state_update(member, before, after):
    if member.bot:
        return

    if before.channel == after.channel:
        return

    if after.channel and after.channel.id in PARTY_CHANNELS:

        channel = after.channel

        if len(channel.members) == 1 and channel.id not in active_parties:

            now = time.time()

            if (
                channel.id in channel_cooldowns and
                now - channel_cooldowns[channel.id] < COOLDOWN
            ):
                return

            active_parties.add(channel.id)
            channel_cooldowns[channel.id] = now

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

                await announcements.send(
                    f"🎮 **{member.display_name}** started a party in **{channel.name}**! @everyone",
                    embed=embed
                )

    if before.channel and before.channel.id in PARTY_CHANNELS:

        if len(before.channel.members) == 0:
            active_parties.discard(before.channel.id)


bot.run(TOKEN)