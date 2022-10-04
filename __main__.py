from dotenv import load_dotenv
from datetime import datetime
import os
import asyncio

import discord
from discord.ext import commands

from utils import helper
import constants
import exts


def main() -> None:
    intents = discord.Intents.default()
    intents.message_content = True
    intents.bans = False
    intents.integrations = False
    intents.invites = False
    intents.typing = False
    intents.webhooks = False

    bot = commands.Bot(
        command_prefix=constants.Client.prefix,
        activity=discord.Game(name=f"Commands: {constants.Client.prefix}help"),
        case_insensitive=True,
        help_command=helper.Help(),
        allowed_mentions=discord.AllowedMentions(everyone=False),
        intents=intents)

    @bot.event
    async def on_ready() -> None:
        for directory in [directory for directory in os.listdir('exts') if os.path.isdir(f"exts/{directory}")]:
            for file_name in [file_name for file_name in os.listdir(f"exts/{directory}") if not os.path.isdir(f"exts/{directory}/{file_name}") and not file_name.startswith("__")]:
                await bot.load_extension(f"exts.{directory}.{file_name[:-3]}")
        print(f"[SUCCESS]: Logged in as {bot.user}")

    bot.run(constants.Client.token)


if __name__ == "__main__":
    main()
