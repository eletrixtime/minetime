from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
class Player(Entity):
    def __init__(self):
        super().__init__()
        self.controller = FirstPersonController()

