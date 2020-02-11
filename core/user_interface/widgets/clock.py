import pygame
from core.user_interface.widgets.widget import Widget
from core.draw_something.useful_isntruments import set_color


class Clock(Widget):
    def __init__(self, x, y, transperency=255, background_color="black", font_color="green", font_style=None):
        super().__init__(x, y, 42, 24, transperency, background_color)
        self.font_color = set_color(font_color)
        self.font_style = font_style
        self.seconds = 0

    def draw_in_widget(self):
        self.surf.fill(self.back_col)
        font = pygame.font.Font(self.font_style, 20)
        text = font.render(f"{(self.seconds // 60):02}:{(self.seconds % 60):02}", 1, self.font_color)
        self.surf.blit(text, (5, 5))

    def set_time(self, seconds):
        self.seconds = seconds

    def tick(self):
        self.seconds += 1
