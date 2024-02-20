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
parser = argparse.ArgumentParser(description='MineTime a clone of Minecraft !')

parser.add_argument('username', type=str, help='Username')
#DISABLED DUE A BUG :parser.add_argument('--debug', action='store_true', help='Enable Debug mode')
args = parser.parse_args()
USERNAME = args.username
app = Ursina(development_mode=True,borderless=False, fullscreen=False, title=f"MineTime Beta-0.0.2 | Logged as {USERNAME}")

try:

    from utils.world.terrain import Terrain
    from utils.player import Player
    from utils.others import blockselect
except:
    print("FAILED TO IMPORT UTIL !")


#Game :
#============================================================================
# MENU (mainmenu its here)
MENU_BUTTON_START_BUTTON = None
MENU_BUTTON_EXIT_BUTTON = None   
MENU_IMAGE_UTIL_LOGO_ENTITY = None
player = None
def destroymenu():
    global MENU_BUTTON_START_BUTTON
    global MENU_BUTTON_START_BUTTON
    global player
    destroy(MENU_BUTTON_START_BUTTON)
    destroy(MENU_BUTTON_EXIT_BUTTON)
    destroy(MENU_IMAGE_UTIL_LOGO_ENTITY)
    terrain = Terrain()
    player = Player()
    player.enabled = True
    player.position = (0, 0, 0)
    #Sky(texture="assets/png/skybox.png")
print("[MAIN] : Loaded main menu")
MENU_IMAGE_UTIL_LOGO_ENTITY = Entity(model='quad', texture="assets/png/minetime.png")
MENU_IMAGE_UTIL_LOGO_ENTITY.scale = (5.3, 1.3)
MENU_IMAGE_UTIL_LOGO_ENTITY.position = (0, 3)
MENU_BUTTON_START_BUTTON = Button(text='Start Game', scale=(0.2, 0.1), position=(0, 0), color=color.green, on_click=destroymenu)
MENU_BUTTON_EXIT_BUTTON = Button(text='Exit', scale=(0.2, 0.1), position=(0, -0.2), color=color.red, on_click=exit)

#============================================================================


def input(key):
    if key == "y":
        #print("Y pressed")
        with open("cache/actualtool.txt", "r+") as f:
            value = f.read()
            f.seek(0) 
            if value == "1":
                f.write("2")
            else:
                f.write("1")

    elif key in blockselect.BLOCKSELECT_NUMBER_LIST:
        blockselect.BLOCKSELECT_SELECT(key)


        

                

window.exit_button.visible = False
app.run()