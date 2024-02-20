from ursina import *
import random
class Voxel(Button):
    def __init__(self, position=(2, 0, 0), block_type=1, scale=0.5):  
        super().__init__(
            parent=scene,
            position=position,
            origin_y=0.5,
            model='assets/block/base.obj',  
            texture=self.gettexture(block_type),  
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=color.light_gray,
            scale=scale,
            on_click=self.on_click_voxel)
        self.block_type = block_type

    def gettexture(self, block_type):
        if block_type == 1:
            return 'assets/block/dirt/texture.png'
        elif block_type == 2:
            return 'assets/block/grass/texture.png'
        elif block_type == 3:
            return 'assets/block/plank/texture.png'
        elif block_type == 999:
            return 'assets/block/bedrock/texture.png'
        elif block_type == 4:
            return 'assets/block/tnt/texture.png'
        else:
            return 'assets/block/notfound.png' 

    def on_click_voxel(self):
        with open("cache/actualtool.txt", "r+") as f:
            value = int(f.read())
            f.seek(0)
            if value == 2:
                destroy(self)
            elif value == 1:
                position = mouse.world_point + mouse.normal
                position = round(position[0]), round(position[1]), round(position[2])
                with open("cache/actualblock.txt", "r+") as f1:
                    f1.seek(0)
                    value1 = int(f1.read())
                    if value1 == 1:
                        temp = Voxel(position=position, block_type=1)
                    elif value1 == 2:
                        temp = Voxel(position=position, block_type=2)
                    elif value1 == 3:
                        temp = Voxel(position=position, block_type=3)
                    elif value1 == 4:
                        temp = Voxel(position=position, block_type=4)

class Terrain:
    def __init__(self, spacing=1.0):
        for z in range(random.randint(10,30)):
            for x in range(random.randint(5,10)):
                    voxel = Voxel(position=(x * spacing, 0, z * spacing), block_type=2, scale=0.5)
                    for y in range(10):
                        y1 = y
                        y1 = y1 + 1 
                        voxel = Voxel(position=(x * spacing, -y1, z * spacing), block_type=1, scale=0.5)
                        #y1 = y1 + 5
                        #voxelbedrock = Voxel(position=(x * spacing, -y1, z * spacing), block_type=4, scale=0.5)