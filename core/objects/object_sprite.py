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

    def set_images(self, *names_of_images):
        self.ob_sprite_images = list(map(lambda x: download_image(x), names_of_images))

    def add_images(self, *names_of_images):
        self.ob_sprite_images += list(map(lambda x: download_image(x), names_of_images))

    def set_objects(self, *objects):
        self.ob_sprite_images = list(objects)

    def add_objects(self, *objects):
        self.ob_sprite_images += list(objects)

    def set_rect_size(self, w, h):
        self.rect.w = w
        self.rect.h = h

    def set_image_size(self, wi, wh):
        self.image = pygame.transform.scale(self.image, (wi, wh))

    def switch_image(self, num):
        self.image = self.ob_images[num]
        self.rect = self.image.get_rect()

    def update(self, *args):
        if pygame.sprite.spritecollideany(self, hover_group):
            hovering_group.add(self)
