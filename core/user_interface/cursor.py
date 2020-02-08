import pygame
from core.draw_something.draw_object import Object_image


class Cursor(Object_image):
    def __init__(self, *names_of_images):
        super(Cursor, self).__init__(*names_of_images)
        pygame.mouse.set_visible(0)

    def hover_rect(self):
        pass
