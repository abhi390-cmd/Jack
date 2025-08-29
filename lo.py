"""𝐅𝚊𝚜𝚝𝚎𝚜𝚝 𝐏𝚒𝚙𝚜, 𝐑𝚞𝚗 𝐅𝚞𝚕𝚕𝚢 𝐓𝚒𝚕𝚕 𝐅𝚒𝚗𝚒𝚜𝚑𝚒𝚗𝚐 𝐒𝚌𝚛𝚎𝚎𝚗 𝐀𝚙𝚙𝚎𝚊𝚛𝚜
𝐔𝚙𝚕𝚘𝚊𝚍𝚎𝚍 𝐎𝚗 @𝚙𝚢𝚋𝚊𝚜𝚒𝚌𝚜"""






















































































black='\033[0;30m'
reset = '\033[0m'
white = '\033[1;37m'
red = '\033[1;31m'
green = '\033[1;32m'

import os

os.system("pip install cfonts")
from cfonts import render
import sys
os.system('clear')
print(f"{white}")
pips = render('{{PIPS}}', colors=['cyan', 'blue'], align='center')
print(pips)
print("	")

enter=input(f"""ㅤ{white}[⚚] 𝐏𝚛𝚎𝚜𝚜 𝐄𝚗𝚝𝚎𝚛 𝐅𝚘𝚛 𝐓𝚑𝚎 𝐈𝚗𝚜𝚝𝚊𝚕𝚕𝚊𝚝𝚒𝚘𝚗 𝐎𝚏 𝐏𝚒𝚙𝚜 ⏎""")
os.system("clear")
import importlib.util
import subprocess

def check(module):

    spec = importlib.util.find_spec(module)
    return spec is not None

def install(module):

    if not check(module):
        print(f"ㅤ{green}[⚚] 𝐈𝚗𝚜𝚝𝚊𝚕𝚕𝚒𝚗𝚐 {module}. . .")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", module])
            print(f"ㅤ{green}[⚚] 𝐈𝚗𝚜𝚝𝚊𝚕𝚕𝚎𝚍 {module} 𝐒𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕𝚕𝚢.")
        except subprocess.CalledProcessError:
            print(f"ㅤ{red}[⚚] 𝐔𝚗𝚎𝚡𝚙𝚎𝚌𝚝𝚎𝚍 𝐄𝚛𝚛𝚘𝚛 𝐎𝚌𝚌𝚞𝚛𝚎𝚍")
    else:#"𝐃𝐯𝐦𝐛"
        print(f"ㅤ{white}[⚚] {module} 𝐀𝚕𝚛𝚎𝚊𝚍𝚢 𝐄𝚡𝚒𝚜𝚝𝚜, 𝐒𝚔𝚒𝚙𝚙𝚒𝚗𝚐")

def main():

    listt = [
        "requests",
        "aiohttp",
        "rich",
        "bs4",
        "time",
        "Topython",
        "user_agent",
        "fake_useragent",
        "pyfiglet",
        "requests",
        "telegram",
        "py_compile",
        "uuid",
        "random",
        "datetime",
        "string",
        "webbrowser",
        "colorama",
        "secrets",
        "pysocks",
        "pyfiglet",
        "curl2pyreqs",
        "telethon",
        "asyncio",
    ]
    
    for module in listt:
        install(module)

if __name__ == "__main__":
    main()



installed = render('done', colors=['green', 'white'], align='center')
"𝐃𝚟𝚖𝚋 𝐈𝚜 𝐖𝚊𝚝𝚌𝚑𝚒𝚗𝚐";os.system("clear")
print(installed)

print("	")
print(f"ㅤ{green}[⚚] 𝐈𝚗𝚜𝚝𝚊𝚕𝚕𝚊𝚝𝚒𝚘𝚗 𝐒𝚞𝚌𝚌𝚎𝚜𝚜𝚏𝚞𝚕") 

print(f"ㅤ{white}[⚚] 𝐂𝚑𝚊𝚗𝚗𝚎𝚕 - @𝚍𝚟𝚖𝚋𝚙𝚢 | 𝐔𝚙𝚕𝚘𝚊𝚍𝚎𝚍 𝐎𝚗 - @𝚙𝚢𝚋𝚊𝚜𝚒𝚌𝚜")
import webbrowser
webbrowser.open('https://t.me/dvmbpy')

#	𝐁𝚢 - @𝚙𝚢𝚊𝚜𝚒𝚌𝚜 