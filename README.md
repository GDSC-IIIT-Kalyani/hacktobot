# hacktobot

[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Contributors][3]][4]
[![Commit Activity][5]][6]
[![Discord][7]][8]
[![Twitter][9]][10]


<!-- Contributors -->
[3]: https://img.shields.io/github/contributors/GDSC-IIIT-Kalyani/hacktobot
[4]: https://github.com/GDSC-IIIT-Kalyani/hacktobot/graphs/contributors
<!-- Commit Activity -->
[5]: https://img.shields.io/github/commit-activity/m/GDSC-IIIT-Kalyani/hacktobot
[6]: https://github.com/GDSC-IIIT-Kalyani/hacktobot/commits/main
<!-- Discord -->
[7]: https://img.shields.io/discord/799321288555888683?logo=discord
[8]: https://discord.gg/tcaxPN6CNs
<!-- Twitter -->
[9]: https://img.shields.io/twitter/follow/gdsciiitkalyani?style=social&logo=twitter
[10]: https://twitter.com/intent/follow?screen_name=gdsciiitkalyani

An open-source Discord bot to introduce and encourage participants to contribute to open-source projects and familiarize them with the bot development environment during Hacktoberfest 2022.

### Requirements:

1. [Python 3.8+](https://www.python.org/downloads/)
2. [Git](https://git-scm.com/downloads)
3. Test server
4. [Bot Account](https://discordpy.readthedocs.io/en/stable/discord.html)

### Development Environment

We recommend creating a [virtual environment](https://docs.python.org/3/library/venv.html) to install and manage all the required dependencies.

```bash
# Creating the virtual environment
$ python3 -m venv .venv

# Activating the virtual environment
# POSIX
$ source .venv/bin/activate         # bash/zsh
$ source .venv/bin/activate.fish    # fish
$ source .venv/bin/activate.csh     # csh/tcsh
$ .venv/bin/Activate.ps1            # PowerShell Core

# Windows
C:\> .venv\Scripts\activate.bat     # cmd.exe
PS C:\> .venv\Scripts\Activate.ps1  # PowerShell

# Installing dependencies
$ pip3 install -r requirements.txt

# Running the bot
$ python3 __main__.py
```

### Environment variables

| Environment Variable | Description |
| --- | --- |
| `PREFIX` | Bot's command invocation prefix |
| `BOT_TOKEN` | Bot Token from the Discord developer portal |
| `GITHUB_TOKEN` | Personal access token for GitHub |

### Contributing to Hacktobot

For guidelines for contributions to this repository, see [Contribution Guidelines](https://github.com/GDSC-IIIT-Kalyani/hacktobot/blob/main/CONTRIBUTING.md).
