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
from ursina import mouse
from utils.others import updatechecker
parser = argparse.ArgumentParser(description='MineTime a clone of Minecraft !')

parser.add_argument('username', type=str, help='Username')
#DISABLED DUE A BUG :parser.add_argument('--debug', action='store_true', help='Enable Debug mode')
args = parser.parse_args()
USERNAME = args.username
app = Ursina(development_mode=True,borderless=False, fullscreen=False, title=f"MineTime {updatechecker.TYPE}-{updatechecker.VERSION}{updatechecker.PATCHNUMBER} | Logged as {USERNAME}")

try:

    from utils.world.terrain import Terrain
    from utils.player import Player
    from utils.others import blockselect
    import os, sys
except:
    print("FAILED TO IMPORT UTIL !")


#Game :
#============================================================================
# MENU (mainmenu its here)
MENU_BUTTON_START_BUTTON = None
MENU_BUTTON_EXIT_BUTTON = None   
MENU_IMAGE_UTIL_LOGO_ENTITY = None
MENU_BUTTON_REPLAY_BUTTON = None
MENU_BUTTON_START_BUTTON_MP = None
MENU_BUTTON_EXIT_BUTTON = None
MENU_UPDATE_GUI_TEXT = None

newworld = None
grid = None
player = None
selected_world = None


def select_world(filename):
    global grid
    if grid:
        destroy(grid)  
        destroy(newworld)
    global selected_world
    selected_world5 = os.path.join("worlds", filename)
    if filename == "NEWWORLDqdqsd":
        terrain = Terrain()
        player = Player()
        player.enabled = True          
        player.position = (0, 0, 0)
    else:
        
        terrain = Terrain(selected_world5)
        player = Player()
        player.enabled = True          
        player.position = (0, 0, 0)

def destroymenu():
    global player
    global grid
    global newworld
    destroy(newworld)
    destroy(MENU_BUTTON_START_BUTTON)
    destroy(MENU_BUTTON_EXIT_BUTTON)
    destroy(MENU_IMAGE_UTIL_LOGO_ENTITY)
    destroy(MENU_BUTTON_START_BUTTON_MP)

    grid = Entity() 

    newworld = Button(text='New world', scale=(0.2, 0.1), position=(0, -0.4), color=color.red, on_click=lambda: select_world(str("NEWWORLDqdqsd")))
    for i, filename in enumerate(os.listdir("worlds")):
        if os.path.isfile(os.path.join("worlds", filename)):
            print(filename)
            btn = Button(text=filename, color=color.green, parent=grid, on_click=lambda: select_world(str(filename)))

            btn.y = i * 1  
            btn.scale = (0.5, 0.5) 
    
   


    #Sky(texture="assets/png/skybox.png")
print("[MAIN] : Loaded main menu")

def mainmenu():
    global MENU_BUTTON_EXIT_BUTTON  
    if MENU_BUTTON_EXIT_BUTTON:
        destroy(MENU_BUTTON_EXIT_BUTTON)
    destroy(MENU_UPDATE_GUI_TEXT)
    global MENU_BUTTON_START_BUTTON
    global MENU_IMAGE_UTIL_LOGO_ENTITY
    global MENU_BUTTON_START_BUTTON_MP
    MENU_IMAGE_UTIL_LOGO_ENTITY = Entity(model='quad', texture="assets/png/minetime.png")
    MENU_IMAGE_UTIL_LOGO_ENTITY.scale = (5.3, 1.3)
    MENU_IMAGE_UTIL_LOGO_ENTITY.position = (0, 3)
    MENU_BUTTON_START_BUTTON = Button(text='Start Game', scale=(0.2, 0.1), position=(0, 0), color=color.green, on_click=destroymenu)
    MENU_BUTTON_START_BUTTON_MP = Button(text='Multiplayer', scale=(0.2, 0.1), position=(0, -0.2), color=color.orange, on_click=destroymenu)
    MENU_BUTTON_EXIT_BUTTON = Button(text='Exit', scale=(0.2, 0.1), position=(0, -0.4), color=color.red, on_click=exit)

def updategui():
    global MENU_UPDATE_GUI_TEXT
    global MENU_BUTTON_EXIT_BUTTON
    descr = dedent('''Hi ! a update is available ! please go to our github for downloading latest update ! or you can skip it !''').strip()

    Text.default_resolution = 1080 * Text.size
    MENU_UPDATE_GUI_TEXT = Text(text=descr, wordwrap=30)
    MENU_BUTTON_EXIT_BUTTON = Button(text='Skip', scale=(0.2, 0.1), position=(0, -0.4), color=color.red, on_click=mainmenu)


#============================================================================

def input(key):
    global MENU_BUTTON_REPLAY_BUTTON
    if key == "y":
        with open("cache/actualtool.txt", "r+") as f:
            value = f.read()
            f.seek(0) 
            if value == "1":
                f.write("2")
            else:
                f.write("1")
    elif key in blockselect.BLOCKSELECT_NUMBER_LIST:
        blockselect.BLOCKSELECT_SELECT(key)
    elif key == "escape":  
        if mouse.locked:   
                mouse.locked = False  

                #destroy(MENU_BUTTON_START_BUTTON)
                #MENU_BUTTON_REPLAY_BUTTON = Button(text='Resume', scale=(0.2, 0.1), position=(0, 0), color=color.green, on_click=exec("mouse.locked=True;destroy(MENU_BUTTON_EXIT_BUTTON);destroy(MENU_IMAGE_UTIL_LOGO_ENTITY);destroy(MENU_BUTTON_REPLAY_BUTTON)"))
                #MENU_BUTTON_EXIT_BUTTON = Button(text='Exit', scale=(0.2, 0.1), position=(0, -0.2), color=color.red, on_click=exit)
        else:
            
            destroy(MENU_BUTTON_EXIT_BUTTON)
            destroy(MENU_IMAGE_UTIL_LOGO_ENTITY)
            mouse.locked = True  

if updatechecker.check() == True:
    mainmenu()
else:
    print("UPDATE AVAILABLE")
    updategui()
window.exit_button.visible = False
app.run()
