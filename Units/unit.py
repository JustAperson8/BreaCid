from core.objects.object_sprite import ObjectSprite
from core.objects.groups_of_sprites import *


class UnitKernel(ObjectSprite):
    def __init__(self, *list_of_groups):
        super().__init__(*list_of_groups)
        self.speed = 10
        self.range_of_attack = 5
        self.hp = 100
        self.spells = []

    def set_params(self, speed=10, range_of_attack=5, hp=100):
        self.speed = speed
        self.range_of_attack = range_of_attack
        self.hp = hp

    def set_spells(self, list_of_spells):
        self.spells = list_of_spells

    def get_spells(self):
        return self.spells

    def update(self, *args):
        super().update()
        x1, y1 = args
