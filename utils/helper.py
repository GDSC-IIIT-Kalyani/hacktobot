from typing import Mapping, Optional, List, Any

import discord
from discord import Embed
from discord.ext import commands

from constants import Colours
from constants import Emojis

COMMANDS_PER_PAGE = 5


class Paginator(discord.ui.View):
    def __init__(self, cmd_list, timeout=180):
        super().__init__(timeout=timeout)
        self.index = 0
        self.cmd_list = cmd_list
        self.length = len(cmd_list)
        self.button_status = {"first": True,
                              "prev": True,
                              "stop": False,
                              "next": self.index == self.length-1,
                              "last": self.index == self.length-1}

    async def on_timeout(self) -> None:
        for item in self.children:
            item.disabled = True

        await self.message.edit(view=self)

    def check_disable(self) -> None:
        self.button_status["first"] = self.button_status["prev"] = self.index == 0
        self.button_status["next"] = self.button_status["last"] = self.index == self.length-1

    def generate_page(self) -> Embed:
        embed = Embed(title="Command Help")
        embed.description = ""
        for cmd in self.cmd_list[self.index]:
            if cmd != None:
                embed.description += f"`{cmd.name}`\n{cmd.short_doc}\n\n"
        embed.set_footer(text=f"Page: 1/{self.length}")
        return embed

    @discord.ui.button(emoji=Emojis.rewind, style=discord.ButtonStyle.gray, custom_id="first", disabled=True)
    async def first(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        button.disabled = self.first
        self.index = 0
        self.check_disable()
        for child in self.children:
            child.disabled = self.button_status[child.custom_id]
        await interaction.response.edit_message(embed=self.generate_page(), view=self)

    @discord.ui.button(emoji=Emojis.arrow_backward, style=discord.ButtonStyle.gray, custom_id="prev", disabled=True)
    async def prev(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        button.disabled = self.prev
        self.index -= 1
        self.check_disable()
        for child in self.children:
            child.disabled = self.button_status[child.custom_id]
        await interaction.response.edit_message(embed=self.generate_page(), view=self)

    @discord.ui.button(emoji=Emojis.wastebasket, style=discord.ButtonStyle.gray, custom_id="stop")
    async def trash(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.stop()
        for child in self.children:
            child.disabled = True
        await interaction.response.edit_message(view=self)

    @discord.ui.button(emoji=Emojis.arrow_forward, style=discord.ButtonStyle.gray, custom_id="next")
    async def next(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.index += 1
        self.check_disable()
        for child in self.children:
            child.disabled = self.button_status[child.custom_id]
        await interaction.response.edit_message(embed=self.generate_page(), view=self)

    @discord.ui.button(emoji=Emojis.fast_forward, style=discord.ButtonStyle.gray, custom_id="last")
    async def last(self, interaction: discord.Interaction, button: discord.ui.Button) -> None:
        self.index = self.length-1
        self.check_disable()
        for child in self.children:
            child.disabled = self.button_status[child.custom_id]
        await interaction.response.edit_message(embed=self.generate_page(), view=self)


class Help(commands.HelpCommand):
    async def send_bot_help(self, mapping: Mapping[Optional[commands.Cog], List[commands.Command[Any, ..., Any]]], /) -> None:
        embed = Embed(title="Command Help")
        embed.description = ""
        cmd_list = []
        for cog, cmds in mapping.items():
            cmd_list.extend(cmds)
        cmd_list = [cmd_list[i:i+COMMANDS_PER_PAGE]
                    for i in range(0, len(cmd_list), COMMANDS_PER_PAGE)]
        for cmd in cmd_list[0]:
            embed.description += f"`{cmd.name}`\n{cmd.short_doc}\n\n"
        embed.set_footer(text=f"Page: 1/{len(cmd_list)}")
        channel = self.get_destination()
        view = Paginator(cmd_list=cmd_list)
        view.message = await channel.send(embed=embed,  view=view)

    async def send_command_help(self, command: commands.Command, /) -> None:
        embed = Embed(title=f"Help: {command.name}")
        embed.description = f"```\n{self.context.prefix}{command.qualified_name} {command.signature}```\n"
        if command.aliases:
            embed.description += f"**Can also use:** `{'`, `'.join(command.aliases)}`\n"
        embed.description += f"*{command.help}*\n"

        channel = self.get_destination()
        await channel.send(embed=embed)

    async def send_group_help(self, group: commands.Group, /) -> None:
        embed = Embed(title=f"Help: {group.name}")
        embed.description = f"```\n{self.context.prefix}{group.qualified_name} {group.signature}```\n"
        if group.aliases:
            embed.description += f"**Can also use:** `{'`, `'.join(group.aliases)}`\n"
        embed.description += f"*{group.help}*\n"
        embed.description += f"\n**Subcommands:**\n"
        for subcommand in group.commands:
            embed.description += f"`{subcommand.name}`\n{subcommand.short_doc}\n"

        channel = self.get_destination()
        await channel.send(embed=embed)

    def command_not_found(self, string: str, /) -> str:
        return f"**Error 404**: Command `{string}` not found!"

    def subcommand_not_found(self, command: commands.Command[Any, ..., Any], string: str, /) -> str:
        if isinstance(command, commands.Group) and len(command.all_commands) > 0:
            error_message = f"**Error 404**: Command `{command.qualified_name}` has no subcommand named `{string}`!\n"
            error_message += f"\nAvailable subcommands:\n`{'`, `'.join(command.all_commands.keys())}`"
            return error_message
        return f"**Error 404**: Command `{command.qualified_name}` has no subcommands!"
