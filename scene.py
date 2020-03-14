import bpy
from mathutils import Vector
import random

random.seed(42)

scene = bpy.context.scene

# clear scene
for obj in scene.objects:
    obj.select_set(True)
bpy.ops.object.delete()


def update():
    bpy.context.view_layer.update()


class Camera:
    def __init__(self, name, lens=18):
        self.data = bpy.data.cameras.new(name)
        self.name = name
        self.data.lens = lens

        self._init_obj()

    def _init_obj(self):
        self.obj = bpy.data.objects.new(name=self.name, object_data=self.data)

    def link(self, scene):
        scene.collection.objects.link(self.obj)

    def look_at(self, point):
        loc_camera = self.obj.matrix_world.to_translation()
        direction = point - loc_camera

        # point the cameras '-Z' and use its 'Y' as up
        rot_quat = direction.to_track_quat('-Z', 'Y')

        # assume we're using euler rotation
        self.obj.rotation_euler = rot_quat.to_euler()


class Light:
    def __init__(self, name, energy=30):
        self.data = bpy.data.lights.new(name, type='POINT')
        self.name = name
        self.data.energy = energy

        self._init_obj()

    def _init_obj(self):
        self.obj = bpy.data.objects.new(name=self.name, object_data=self.data)

    def link(self, scene):
        scene.collection.objects.link(self.obj)


# add camera
cam = Camera('Camera 1', lens=25)
cam.link(scene)
scene.camera = cam.obj

cam.obj.location = (2. + random.random()*8., 2. + random.random()*8., 2. + random.random()*8.)
update()
cam.look_at(Vector((0., 0., 0.)))
update()

# import object
obj = bpy.ops.import_scene.obj(filepath='obj/monkey.obj')

# light
light = Light('Light 1', energy=1000)
light.obj.location = (2. + random.random()*8., 2. + random.random()*8., 2. + random.random()*8.)
light.link(scene)

# Render
bpy.context.scene.render.filepath = 'data/image.jpg'
bpy.ops.render.render(write_still=True)
