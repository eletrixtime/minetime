from ursina import *
from utils.world.terrain import Terrain
from utils.player import Player

BUTTON_START_BUTTON = None
BUTTON_EXIT_BUTTON = None   
IMAGE_UTIL_LOGO_ENTITY = None

def destroymenu():
    global BUTTON_START_BUTTON
    global BUTTON_EXIT_BUTTON
    global IMAGE_UTIL_LOGO_ENTITY
    global player
    destroy(BUTTON_START_BUTTON)
    destroy(BUTTON_EXIT_BUTTON)
    destroy(IMAGE_UTIL_LOGO_ENTITY)
    terrain = Terrain()
    player = Player()
    player.enabled = True
    player.position = (0, 1, 0)


class mainmenu(Entity):
    def __init__(self):
        global BUTTON_START_BUTTON
        global BUTTON_EXIT_BUTTON
        global IMAGE_UTIL_LOGO_ENTITY
        
        print("[MAIN] : Loaded main menu")
        IMAGE_UTIL_LOGO_ENTITY = Entity(model='quad', texture="assets/png/minetime.png")
        IMAGE_UTIL_LOGO_ENTITY.scale = (5.3, 1.3)
        IMAGE_UTIL_LOGO_ENTITY.position = (0, 3)
        BUTTON_START_BUTTON = Button(text='Start Game', scale=(0.2, 0.1), position=(0, 0), color=color.green, on_click=destroymenu)
        BUTTON_EXIT_BUTTON = Button(text='Exit', scale=(0.2, 0.1), position=(0, -0.2), color=color.red, on_click=exit)

