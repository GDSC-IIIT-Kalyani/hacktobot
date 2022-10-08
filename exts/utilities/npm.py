import requests
import re

import discord
from discord import Embed
from discord.ext import commands

URL = "https://registry.npmjs.org/"
NPM_LOGO = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Npm-logo.svg/320px-Npm-logo.svg.png"


class NPM(commands.Cog):
    """Get info about a npm packages"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="npm")
    async def npm(self, ctx: commands.Context, package: str) -> None:
        """Provide information about a specific package from npm."""

        embed = Embed(colour=discord.Colour.blue())

        response = requests.get(f"{URL}{package}/")

        if response.status_code == 404:
            embed.description = "Package could not be found."
        if response.status_code == 200:
            result = response.json()

            embed.title = f"{result['_id']} v{result['dist-tags']['latest']}"
            embed.description = result["description"]
            embed.url = f"https://www.npmjs.com/package/{result['_id']}"
            embed.set_thumbnail(url=NPM_LOGO)

            latest = result["versions"][result["dist-tags"]["latest"]]
            if latest.get("homepage", False):
                embed.add_field(name="Homepage",
                                value=latest["homepage"], inline=False)
            if latest.get("repository", False):
                github_pattern = r'github.com\/[a-zA-Z0-9_-]+\/[a-zA-Z0-9_-]+'
                repo_url = re.search(
                    github_pattern, latest["repository"]["url"])
                embed.add_field(
                    name="Repository", value=f"https://{repo_url[0]}", inline=False)

        await ctx.send(embed=embed)

    @npm.error
    async def npm_error(self, ctx: commands.Context, error) -> None:
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=Embed(
                colour=discord.Color.blue(),
                description=f"You forgot to provide the required paramater `{error.param.name}`.\n"
                            f"\nFor more details run: `{ctx.prefix}help {ctx.command.qualified_name}`"
            ))
        else:
            raise error


async def setup(bot: commands.Bot) -> None:
    """Load the NPM cog."""
    await bot.add_cog(NPM(bot))
