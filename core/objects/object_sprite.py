import pygame

from core.download_something.download_image import download_image
from core.objects.groups_of_sprites import *


class ObjectSprite(pygame.sprite.Sprite):
    def __init__(self, *list_of_groups):
        self.ob_sprite_images = []
        if list_of_groups:
            super().__init__(list_of_groups)
        self.image = None
        self.rect = None
        self.im_group = 0

    def add_group_of_images(self, *names_of_images, type_of_images=None):
        self.ob_sprite_images.append(list(map(lambda x: download_image(x, type_of_images), names_of_images)))

    def add_images(self, *names_of_images, type_of_images=None):
        self.ob_sprite_images[-1] += list(map(lambda x: download_image(x, type_of_images), names_of_images))

    def add_group_of_objects(self, *objects):
        self.ob_sprite_images += list(objects)

    def add_objects(self, *objects):
        self.ob_sprite_images[-1] += list(objects)

    def set_rect_size(self, w, h):
        self.rect.w = w
        self.rect.h = h

    def set_image_size(self, wi, wh):
        self.image = pygame.transform.scale(self.image, (wi, wh))

    def set_pos(self, x, y):
        self.rect = self.rect.move(x, y)

    def switch_image_group(self, num):
        self.im_group = num

    def switch_image(self, num):
        self.image = self.ob_sprite_images[self.im_group][num]
        self.rect = self.image.get_rect()

    def update(self, *args):
        pass
