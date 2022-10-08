from dotenv import load_dotenv
from os import environ

load_dotenv()


class Client:
    prefix = environ.get("PREFIX", ".")
    token = environ.get("BOT_TOKEN")


class Colours:
    blue = 0x0279FD
    python_blue = 0x4B8BBE
    python_yellow = 0xFFD43B
    twitter_blue = 0x1DA1F2
    bright_green = 0x01D277
    dark_green = 0x1F8B4C
    orange = 0xE67E22
    pink = 0xCF84E0
    purple = 0xB734EB
    soft_green = 0x68C290
    soft_orange = 0xF9CB54
    soft_red = 0xCD6D6D
    yellow = 0xF9F586
    grass_green = 0x66FF00
    gold = 0xE6C200

    # Hacktoberfest 2022
    hacktober22_void = 0x170F1E
    hacktober22_manga = 0xE5E1E5
    hacktober22_spark = 0xFFE27D
    hacktober22_surf = 0x64E3FF
    hacktober22_psybeam = 0x9092FF
    hacktober22_giga = 0xB4FF39
    hacktober22 = (hacktober22_void,
                   hacktober22_manga,
                   hacktober22_spark,
                   hacktober22_surf,
                   hacktober22_psybeam,
                   hacktober22_giga,
                   )


class Emojis:
    wastebasket = "\U0001f5d1\ufe0f"
    rewind = "\u23ea"
    fast_forward = "\u23e9"
    arrow_backward = "\u25c0\ufe0f"
    arrow_forward = "\u25b6\ufe0f"


class Tokens:
    github = environ.get("GITHUB_TOKEN")
