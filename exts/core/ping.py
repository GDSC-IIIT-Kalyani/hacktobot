from datetime import datetime

import discord
from discord import Embed
from discord.ext import commands

from constants import Colours
import exts


class Ping(commands.Cog):
    """Get info about the bot's ping and uptime."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="uptime")
    async def uptime(self, ctx: commands.Context, /) -> None:
        """Get the current uptime of the bot."""
        difference = datetime.utcnow() - exts.start_time

        uptime_string = ""
        if difference.days > 0:
            uptime_string += f"{difference.days} day{'s' if difference.days>1 else ''}"
        if difference.seconds//3600 > 0:
            hours = difference.seconds//3600
            uptime_string += f"{' 'if uptime_string else ''}{hours} hour{'s' if hours>1 else ''}"
        if (difference.seconds//60) % 60 > 0:
            minutes = (difference.seconds//60) % 60
            uptime_string += f"{' 'if uptime_string else ''}{minutes} minute{'s' if minutes>1 else ''}"
        if difference.seconds % 60 > 0:
            seconds = difference.seconds % 60
            uptime_string += f"{' 'if uptime_string else ''}{seconds} second{'s' if seconds>1 else ''}"

        embed = Embed(
            title=":hourglass: Uptime!",
            colour=Colours.bright_green,
            description=f"Uptime: {uptime_string}",
        )

        await ctx.send(embed=embed)

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context, /) -> None:
        """Ping the bot to see its latency and state."""
        embed = Embed(
            title=":ping_pong: Pong!",
            colour=Colours.bright_green,
            description=f"Gateway Latency: {round(self.bot.latency * 1000)}ms",
        )

        await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    """Load the Ping cog."""
    await bot.add_cog(Ping(bot))
