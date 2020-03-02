from core.objects.object_sprite import ObjectSprite
from core.objects.groups_of_sprites import *


class UnitKernel(ObjectSprite):
    def __init__(self, *list_of_groups):
        super().__init__(*list_of_groups)
        self.terrain = []
        self.commands = []
        self.speed = 10
        self.hp = 100
        self.spells = []

    def set_terrain(self, terrain):
        self.terrain = terrain

    def set_params(self, speed=10, hp=100):
        self.speed = speed
        self.hp = hp

    def get_spells(self):
        return self.spells

    def update(self, *args):
        super().update()
        x1, y1 = args


class UnitControl:
    def __init__(self, *list_of_groups):
        self.range_of_attack = 5
        self.name_spells = []
        self.spells = []
        self.unit_kernel = UnitKernel(list_of_groups[0])

    def set_spells(self, name_or_image_of_spells, list_of_spells):
        self.name_spells = name_or_image_of_spells
        self.spells = list_of_spells

    def set_movement(self, x, y):
        pass
