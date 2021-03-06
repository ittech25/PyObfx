banner1 = """

 /$$$$$$$             /$$$$$$  /$$        /$$$$$$          
| $$__  $$           /$$__  $$| $$       /$$__  $$         
| $$  \ $$ /$$   /$$| $$  \ $$| $$$$$$$ | $$  \__//$$   /$$
| $$$$$$$/| $$  | $$| $$  | $$| $$__  $$| $$$$   |  $$ /$$/
| $$____/ | $$  | $$| $$  | $$| $$  \ $$| $$_/    \  $$$$/ 
| $$      | $$  | $$| $$  | $$| $$  | $$| $$       >$$  $$ 
| $$      |  $$$$$$$|  $$$$$$/| $$$$$$$/| $$      /$$/\  $$
|__/       \____  $$ \______/ |_______/ |__/     |__/  \__/
           /$$  | $$                                       
v1.0      |  $$$$$$/  ~ https://github.com/PyObfx
           \______/     
"""

banner2 = """

  _____        ____  _      __      
 |  __ \      / __ \| |    / _|     
 | |__) |   _| |  | | |__ | |___  __
 |  ___/ | | | |  | | '_ \|  _\ \/ /
 | |   | |_| | |__| | |_) | |  >  < 
 |_|    \__, |\____/|_.__/|_| /_/\_\\
         __/ |                      
v1.0    |___/ ~ https://github.com/PyObfx
"""

banner3 = """

██████╗ ██╗   ██╗ ██████╗ ██████╗ ███████╗██╗  ██╗
██╔══██╗╚██╗ ██╔╝██╔═══██╗██╔══██╗██╔════╝╚██╗██╔╝
██████╔╝ ╚████╔╝ ██║   ██║██████╔╝█████╗   ╚███╔╝
██╔═══╝   ╚██╔╝  ██║   ██║██╔══██╗██╔══╝   ██╔██╗
██║        ██║   ╚██████╔╝██████╔╝██║     ██╔╝ ██╗
╚═╝        ╚═╝    ╚═════╝ ╚═════╝ ╚═╝     ╚═╝  ╚═╝

v1.0                  ~ https://github.com/PyObfx

"""

banner4 = """

8888888b.            .d88888b.  888       .d888
888   Y88b          d88P" "Y88b 888      d88P"
888    888          888     888 888      888
888   d88P 888  888 888     888 88888b.  888888 888  888
8888888P"  888  888 888     888 888 "88b 888    `Y8bd8P'
888        888  888 888     888 888  888 888      X88K
888        Y88b 888 Y88b. .d88P 888 d88P 888    .d8""8b.
888         "Y88888  "Y88888P"  88888P"  888    888  888
                888
v1-0       Y8b d88P  ~ https://github.com/PyObfx
            "Y88P"
"""

banner5 = """
 ██▓███ ▓██   ██▓ ▒█████   ▄▄▄▄     █████▒▒██   ██▒
▓██░  ██▒▒██  ██▒▒██▒  ██▒▓█████▄ ▓██   ▒ ▒▒ █ █ ▒░
▓██░ ██▓▒ ▒██ ██░▒██░  ██▒▒██▒ ▄██▒████ ░ ░░  █   ░
▒██▄█▓▒ ▒ ░ ▐██▓░▒██   ██░▒██░█▀  ░▓█▒  ░  ░ █ █ ▒ 
▒██▒ ░  ░ ░ ██▒▓░░ ████▓▒░░▓█  ▀█▓░▒█░    ▒██▒ ▒██▒
▒▓▒░ ░  ░  ██▒▒▒ ░ ▒░▒░▒░ ░▒▓███▀▒ ▒ ░    ▒▒ ░ ░▓ ░
░▒ ░     ▓██ ░▒░   ░ ▒ ▒░ ▒░▒   ░  ░      ░░   ░▒ ░
░░       ▒ ▒ ░░  ░ ░ ░ ▒   ░    ░  ░ ░     ░    ░  
         ░ ░         ░ ░   ░               ░    ░  
         ░ ░                    ░                  
v1.0                    ~ https://github.com/PyObfx
"""

from random import choice

def print_banner():
    """
    Chooses random banner from provided banners above
    """
    banners = [banner1, banner2, banner3, banner4, banner5]
    print(choice(banners))
