from ursina import *
import random
import json
import os
import threading
# Thank GPT for the saving/load system (j'avais la flemmeeee)
class Voxel(Button):
    def __init__(self, position=(2, 0, 0), block_type=1, scale=0.5, world_path=None, terrain_instance=None):
        super().__init__(
            parent=scene,
            position=position,
            origin_y=0.5,
            model='assets/block/base.obj',
            texture=self.get_texture(block_type),
            color=color.color(0, 0, random.uniform(0.9, 1)),
            highlight_color=color.light_gray,
            scale=scale,
            on_click=self.on_click_voxel)
        self.block_type = block_type
        self.world_path = world_path
        self.terrain_instance = terrain_instance

    def get_texture(self, block_type):
        textures = {
            1: 'assets/block/dirt/texture.png',
            2: 'assets/block/grass/texture.png',
            3: 'assets/block/plank/texture.png',
            999: 'assets/block/bedrock/texture.png',
            4: 'assets/block/tnt/texture.png',
        }
        return textures.get(block_type, 'assets/block/notfound.png')

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
                    if value1 in [1, 2, 3, 4]:
                        temp = Voxel(position=position, block_type=value1, world_path=self.world_path, terrain_instance=self.terrain_instance)

    def update_json(self, position, block_type):
        try:
            with open(self.world_path, "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = []

        data.append({'position': position, 'block_type': block_type, 'scale': 0.5})

        with open(self.world_path, "w") as f:
            json.dump(data, f)

        self.terrain_instance.load_from_json(data)


class Terrain:
    def __init__(self, world_path=None, spacing=1.0):
        if world_path is None:
            world_path = os.path.join("worlds", f"world{random.randint(1, 10000)}.json")
        self.world_path = world_path
        if not os.path.exists(self.world_path) or os.path.basename(self.world_path) == "RESET" or not os.path.isfile(self.world_path):
            self.generate_random_terrain(spacing)
        else:
            with open(self.world_path, "r") as f:
                data = json.load(f)
                self.load_from_json(data)

        self.save_lock = threading.Lock()
        self.save_world_timer = threading.Timer(10, self.manual_save_world)
        self.save_world_timer.start()

    def generate_random_terrain(self, spacing):
        terrain_data = []
        for z in range(random.randint(5, 20)):
            for x in range(random.randint(5, 20)):
                voxel = {'position': (x * spacing, 0, z * spacing), 'block_type': 2, 'scale': 0.5}
                terrain_data.append(voxel)
                for y in range(10):
                    voxel = {'position': (x * spacing, -y - 1, z * spacing), 'block_type': 1, 'scale': 0.5}
                    terrain_data.append(voxel)
        world_dir = os.path.dirname(self.world_path)
        os.makedirs(world_dir, exist_ok=True)
        with open(self.world_path, "w") as f:
            json.dump(terrain_data, f)
        self.save_to_json(terrain_data)
        self.load_from_json(terrain_data)

    def load_from_json(self, data):
        for voxel_data in data:
            Voxel(position=voxel_data['position'], block_type=voxel_data['block_type'], terrain_instance=self)


    def save_to_json(self, data):
        for voxel_data in data:
            position = voxel_data['position']
            voxel_data['position'] = (position[0], position[1], position[2])

        with open(self.world_path, "w") as f:
            json.dump(data, f, default=lambda o: o.__dict__)


    def manual_save_world(self):
        print("Saving #")
        self.save_lock.acquire()

        world_data = []
        for entity in scene.entities:
            if isinstance(entity, Voxel):
                world_data.append({'position': entity.position, 'block_type': entity.block_type, 'scale': entity.scale})

        save_thread = threading.Thread(target=self.save_to_json, args=(world_data,))
        save_thread.start()

        save_thread.join() 

        self.save_lock.release()
        print("Saving DONE")
        self.save_world_timer = threading.Timer(20, self.manual_save_world)
        self.save_world_timer.start()

