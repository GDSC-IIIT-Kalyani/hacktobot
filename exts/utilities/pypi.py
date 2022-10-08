import requests

import discord
from discord import Embed
from discord.ext import commands

from constants import Colours

URL = "https://pypi.org/pypi/"
PYPI_LOGO = "https://raw.githubusercontent.com/GDSC-IIIT-Kalyani/hacktobot/main/resources/utilities/pypi_logo_small.png"


class PyPI(commands.Cog):
    """Get info about a pypi packages"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="pypi")
    async def pypi(self, ctx: commands.Context, package: str) -> None:
        """Provide information about a specific package from pypi."""

        embed = discord.Embed(color=Colours.python_blue)

        response = requests.get(f"{URL}{package}/json")

        if response.status_code == 404:
            embed.description = "Package could not be found."
        if response.status_code == 200:
            result = response.json()
            embed.title = f"{result['info']['name']} v{result['info']['version']}"
            embed.description = result['info']['summary']
            embed.url = result['info']['package_url']
            embed.set_thumbnail(url=PYPI_LOGO)
            embed.add_field(name="Homepage",
                            value=result['info']['home_page'], inline=False)
            embed.add_field(name="Package URL",
                            value=result['info']['package_url'], inline=False)

        await ctx.send(embed=embed)

    @pypi.error
    async def pypi_error(self, ctx: commands.Context, error) -> None:
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=Embed(
                colour=discord.Color.blue(),
                description=f"You forgot to provide the required paramater `{error.param.name}`.\n"
                            f"\nFor more details run: `{ctx.prefix}help {ctx.command.qualified_name}`"
            ))
        else:
            raise error


async def setup(bot: commands.Bot) -> None:
    """Load the PyPI cog."""
    await bot.add_cog(PyPI(bot))
