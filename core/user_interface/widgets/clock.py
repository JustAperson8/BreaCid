import pygame
from core.user_interface.widgets.widget import Widget
from core.draw_something.useful_isntruments import set_color


class Clock(Widget):
    def __init__(self, x, y, transparency=255, background_color="black", font_color="white", font_style=None,
                 font_size=20, left=0, top=0):
        super().__init__(x, y, font_size*3+left, font_size+top, transparency, background_color)
        self.font_color = set_color(font_color)
        self.font_style = font_style
        self.left, self.top = left, top
        self.seconds = 0
        self.font_size = font_size

    def draw_in_widget(self):
        self.surf.fill(self.back_col)
        font = pygame.font.Font(self.font_style, self.font_size)
        text = font.render(f"{(self.seconds // 60):02}:{(self.seconds % 60):02}", 1, self.font_color)
        self.surf.blit(text, (self.left, self.top))

    def set_time(self, seconds):
        self.seconds = seconds

    def tick(self):
        self.seconds += 1
