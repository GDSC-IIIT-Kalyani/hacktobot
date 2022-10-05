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

1. All the assets used must be stored in the directory `./resources`.
2. It is recommended to store all the constants used in `constants.py` in the root directory.
3. Utility classes and functions can be stored in the directory `./utils`.
4. The commands are divided into 3 major categories:
    1. `./exts/core` stores all the core commands related to the bot’s functioning. 
    2. `./exts/fun` stores fun and game commands.
    3. `./exts/utilities` stores utility and miscellaneous commands. 
5. It would be appreciated if you follow type annotations as per the style defined in [PEP 484](https://www.python.org/dev/peps/pep-0484/) and the [PEP 8 guidelines](https://www.python.org/dev/peps/pep-0008/).
6. For guidelines for contributions to this repository, see [Contribution Guidelines](#contributing-guidelines).

## Contributing Guidelines

1. Commits should be atomic, and the commit message must explain what and why. Commits should be as narrow in scope as possible since commits with a large span  of unrelated functions and files are very hard for the maintainers to follow. Don’t forget to lint before you push!
2. Use assets licensed for pubic use.
3. Do not open a pull request if you aren't assigned to the issue. If someone is already working on it, consider collaborating with that person to help the maintainers with the successful .