# Contributing Guidelines

1. Commits should be atomic, and the commit message must explain what and why. Commits should be as narrow in scope as possible since commits with a large span  of unrelated functions and files are very hard for the maintainers to follow. Don’t forget to lint before you push!
Commits should be atomic, and the commit message must explain what and why. Commits should be as narrow in scope as possible since commits with a large span of unrelated functions and files are very hard for the maintainers to follow. Don’t forget to lint before you push!
2. Use assets licensed for public use.
3. **Do not open a pull request if you aren't assigned to the issue.** If someone is already working on it, consider collaborating with that person to help the maintainers maintain a smooth workflow.

## Contributing to Hacktobot

1. All the assets used must be stored in the directory `./resources`.
2. It is recommended to store all the constants used in `constants.py` in the root directory.
3. Utility classes and functions can be stored in the directory `./utils`.
4. The commands are divided into 3 major categories:
    1. `./exts/core` stores all the core commands related to the bot’s functioning. 
    2. `./exts/fun` stores fun and game commands.
    3. `./exts/utilities` stores utility and miscellaneous commands. 
5. It would be appreciated if you follow type annotations as per the style defined in [PEP 484](https://www.python.org/dev/peps/pep-0484/) and the [PEP 8 guidelines](https://www.python.org/dev/peps/pep-0008/).
6. Feel free to open an issue if you believe that any feature needs implementation.
