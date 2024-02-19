from ursina import *

class Voxel(Button):
    def __init__(self, position=(2, 0, 0)):
        super().__init__(
            parent=scene,
            position=position,
            origin_y=0.5,
            model='assets/block/base.obj',  
            texture='assets/block/dirt/texture.png',
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=color.light_gray,
            scale=1,
            on_click=self.on_click_voxel  
        )

    def on_click_voxel(self):
        with open("cache.txt", "r+") as f:
            value = int(f.read()) 
            f.seek(0) 
            print(value)
            if value == 2: 
                destroy(self)
            elif value == 1:
                position = mouse.world_point
                temp = Voxel(position=position)

class Terrain:
    def __init__(self):
        for z in range(20):
            for x in range(20):
                voxel = Voxel(position=(x * 1.9, 0, z * 1.9))
