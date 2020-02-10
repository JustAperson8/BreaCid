import pygame
from core.draw_something.useful_isntruments import set_color

class Widget:
    def __init__(self, x, y, width, height, transparency, background_color):
        self.surf = pygame.Surface((width, height))
        self.w, self.h = width, height
        self.trans = transparency
        self.back_col = set_color(background_color)
        self.x, self.y = x ,y

    def draw_in_widget(self):
        pass

    def update(self, screen):
        self.draw_in_widget()
        self.surf.set_alpha(self.trans)
        screen.blit(self.surf, (self.x, self.y))
        self.surf.fill(self.back_col)
