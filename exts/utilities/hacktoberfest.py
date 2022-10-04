from datetime import datetime
from typing import Literal
import random

import discord
from discord import Embed
from discord.ext import commands
from requests import request
import requests

from constants import Colours, Tokens


URL = "https://api.github.com/search/issues?per_page=100&q=is:issue+label:hacktoberfest+state:open"
HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "GDSC IIIT Kalyani Hacktoberbot"
}

if GITHUB_TOKEN := Tokens.github:
    HEADERS["Authorization"] = f"token {GITHUB_TOKEN}"


class Hacktober(commands.Cog):
    """Commands related to hacktoberfest."""

    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
        self.cache = {"normal": {}, "beginner": {}}

    @commands.group(name="hacktober", aliases=("hacktoberfest",))
    async def hacktober(self, ctx: commands.Context) -> None:
        """Commands related to hacktoberfest."""
        if ctx.invoked_subcommand is None:
            helper = self.bot.help_command
            helper.context = ctx
            await helper.send_group_help(ctx.command)

    @staticmethod
    def issue_embed(issue: dict) -> Embed:
        """Formats the embed for issues command."""

        description = issue.get("body") or ""
        labels = [label["name"] for label in issue["labels"]]

        embed = Embed(
            title=issue["title"],
            colour=random.choice(Colours.hacktober22),
            url=issue["html_url"],
            description=description[:1000] +
            "..." if len(description) > 1000 else description
        )
        embed.add_field(name="Labels", value=f"`{'`, `'.join(labels)}`")
        embed.set_footer(text=issue["html_url"])

        return embed

    @hacktober.group(name="issues", aliases=("issue",))
    async def issues(self, ctx: commands.Context, language: str, option: Literal["beginner"] = None) -> None:
        """Get a random hacktober issue from GitHub of the provided language.

        Option \"beginner\" will also narrow issue down to the \"good first issue\" label.
        """

        now = datetime.utcnow()
        year = now.year+int(now.month > 10)
        start = datetime(year, 9, 30, 10)
        end = datetime(year, 11, 1, 12)
        language = language.lower()

        url = URL+f"+language:{language}"

        embed = Embed(
            colour=random.choice(Colours.hacktober22)
        )

        if start <= now <= end:  # Current time is within Hacktoberfest.
            create_time = ctx.message.created_at.replace(tzinfo=None)

            if option == "beginner":
                cache_time = self.cache["beginner"].get(
                    language, {}).get("cache_time", datetime(year-1, 12, 31, 0, 0, 1))
                url += "+label:\"good first issue\""

                if (create_time - cache_time).seconds <= 120 and self.cache["beginner"].get(language, False):
                    embed = self.issue_embed(random.choice(
                        self.cache["beginner"][language]["items"]))
                else:
                    page = random.randint(1, 10)
                    url += f"&page={page}"

                    response = requests.get(url, headers=HEADERS)
                    if response.ok:
                        result = response.json()
                        result["cache_time"] = ctx.message.created_at.replace(
                            tzinfo=None)
                        self.cache["beginner"][language] = result
                        embed = self.issue_embed(
                            random.choice(result["items"]))
                    else:
                        embed.description = f"Got `Error {response.status_code}` from GitHub API."

            else:
                cache_time = self.cache["normal"].get(
                    language, {}).get("cache_time", datetime(year-1, 12, 31, 0, 0, 1))

                if (create_time - cache_time).seconds <= 120 \
                        and self.cache["normal"].get(language, False):
                    embed = self.issue_embed(random.choice(
                        self.cache["normal"][language]["items"]))
                else:
                    page = random.randint(1, 10)
                    url += f"&page={page}"

                    response = requests.get(url, headers=HEADERS)
                    if response.ok:
                        result = response.json()
                        result["cache_time"] = ctx.message.created_at.replace(
                            tzinfo=None)
                        self.cache["normal"][language] = result
                        embed = self.issue_embed(
                            random.choice(result["items"]))
                    else:
                        embed.description = f"Got `Error {response.status_code}` from GitHub API."

        else:
            days_left = (start-now).days
            embed.description = f"It\'s not Hacktober yet. The next one will start in {days_left} day{'s' if days_left>1 else ''}."

        await ctx.send(embed=embed)

    @issues.error
    async def issues_error(self, ctx: commands.Context, error) -> None:
        if isinstance(error, commands.MissingRequiredArgument):
            helper = self.bot.help_command
            helper.context = ctx
            await ctx.send(embed=Embed(
                colour=random.choice(Colours.hacktober22),
                description=f"You forgot to provide the required paramater `{error.param.name}`.\n"
                            f"\nFor more details run: `{ctx.prefix}help {ctx.command.qualified_name}`"
            ))
        else:
            raise error

    @hacktober.command(name="timeleft", aliases=("time",))
    async def timeleft(self, ctx: commands.Context) -> None:
        """Tells you how long left until Hacktober is over!"""
        now = datetime.utcnow()
        year = now.year+int(now.month > 10)
        start = datetime(year, 9, 30, 10)
        end = datetime(year, 11, 1, 12)

        embed = Embed(
            title=f":hourglass: Hacktoberfest {year}: Time left!",
            colour=random.choice(Colours.hacktober22)
        )

        if start <= now <= end:  # Current time is within Hacktoberfest.
            difference = end-now
            days = difference.days
            hours = difference.seconds//3600
            minutes = (difference.seconds//60) % 60

            embed_text = "There are "
            if difference.days > 0:
                embed_text += f"{difference.days} day{'s' if difference.days>1 else ''} "
            if difference.seconds//3600 > 0:
                hours = difference.seconds//3600
                embed_text += f"{hours} hour{'s' if hours>1 else ''} "
            if (difference.seconds//60) % 60 > 0:
                minutes = (difference.seconds//60) % 60
                embed_text += f"{minutes} minute{'s' if minutes>1 else ''} "
            embed_text += "left until the end of Hacktober."

            embed.description = embed_text

        else:
            days_left = (start-now).days
            embed.description = f"It\'s not Hacktober yet. The next one will start in {days_left} day{'s' if days_left>1 else ''}."

        await ctx.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    """Load the Hacktober cog."""
    await bot.add_cog(Hacktober(bot))
