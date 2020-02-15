import pygame
from core.draw_something.useful_isntruments import set_color


class Widget:
    def __init__(self, x, y, width, height, transparency, background_color):
        self.surf = pygame.Surface((width, height))
        self.surf.set_alpha(transparency)
        self.w, self.h = width, height
        self.back_col = set_color(background_color)
        self.x, self.y = x, y

    def draw_in_widget(self):
        pass

    def update(self, screen):
        screen.blit(self.surf, (self.x, self.y))