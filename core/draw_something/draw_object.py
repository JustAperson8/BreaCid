import pygame
from core.download_something.download_image import download_image


class Object_image:
    def __init__(self, *names_of_images):
        self.ob_images = []
        self.add_images(*names_of_images)
        self.using_cursor = 0

    def switch_image(self, num):
        self.using_cursor = num

    def render_image(self, scr, x, y):
        if pygame.mouse.get_focused():
            scr.blit(self.ob_images[self.using_cursor], (x, y))

    def add_images(self, *names_of_images):
        self.ob_images += list(map(lambda x: download_image(x), names_of_images))


class Object_sprite(pygame.sprite.Sprite):
    pass
