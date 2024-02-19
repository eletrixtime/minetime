'''''
----------------------------------------------------------------------
  __  __ _____ _   _ ______ _______ _____ __  __ ______ 
 |  \/  |_   _| \ | |  ____|__   __|_   _|  \/  |  ____|
 | \  / | | | |  \| | |__     | |    | | | \  / | |__   
 | |\/| | | | | . ` |  __|    | |    | | | |\/| |  __|  
 | |  | |_| |_| |\  | |____   | |   _| |_| |  | | |____ 
 |_|  |_|_____|_| \_|______|  |_|  |_____|_|  |_|______|
----------------------------------------------------------------------
By EletrixTime
Github : https://github.com/EletrixtimeYT/minetime
Itch.io (Compiled binaries for windows) : soon !
'''
print("""  __  __ _____ _   _ ______ _______ _____ __  __ ______ 
 |  \/  |_   _| \ | |  ____|__   __|_   _|  \/  |  ____|
 | \  / | | | |  \| | |__     | |    | | | \  / | |__   
 | |\/| | | | | . ` |  __|    | |    | | | |\/| |  __|  
 | |  | |_| |_| |\  | |____   | |   _| |_| |  | | |____ 
 |_|  |_|_____|_| \_|______|  |_|  |_____|_|  |_|______|""")

from ursina import *
import argparse
from assets import assetsconfig
parser = argparse.ArgumentParser(description='MineTime a clone of Minecraft !')

parser.add_argument('username', type=str, help='Username')
#DISABLED DUE A BUG :parser.add_argument('--debug', action='store_true', help='Enable Debug mode')
args = parser.parse_args()
USERNAME = args.username
app = Ursina(development_mode=True,borderless=False, fullscreen=False, title=f"MineTime 0.0.1 | Logged as {USERNAME}")

try:
    from utils.menu.mainmenu import mainmenu
    from utils.player import Player
    from utils.world.terrain import Terrain
except:
    print("FAILED TO IMPORT UTIL !")


#Game :

mainmenu = mainmenu()
Player = Player
def input(key):
    if key == "y":
        print("Y pressed")
        with open("cache.txt", "r+") as f:
            value = f.read()
            f.seek(0) 
            if value == "1":
                f.write("2")
            else:
                f.write("1")

window.exit_button.visible = False
app.run()