from os import system
modules = [   
    ("rich", "rich"),
    ("uuid", "uuid"),
    ("socks", "pysocks"),
    ("telebot", "telebot"),
    ("aiohttp", "aiohttp"),
    ("requests","requests"),
    ("colorama","colorama"),
    ("telethon", "telethon"),
    ("Topython", "Topython"),
    ("pyfiglet", "pyfiglet"),
    ("argparse", "argparse"),
    ("bs4", "beautifulsoup4"),
    ("cfonts","python-cfonts"),
    ("stdiomask", "stdiomask"),
    ("user_agent","user_agent"),
    ("youtube_dl", "youtube_dl"),
    ("curl2pyreqs", "curl2pyreqs"),
    ("instaloader", "instaloader"),
    ("InstagramAPI", "InstagramAPI")
]

missing = []

for module, pip  in modules:
    try:
        __import__(module)
    except ModuleNotFoundError:
        missing.append(pip)

if missing:
    toinstall = " ".join(missing)
    system(f"pip install {toinstall}")

