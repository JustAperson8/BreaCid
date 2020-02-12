import pygame
from core.user_interface.widgets.widget import Widget
from core.draw_something.useful_isntruments import set_color

class Information_for_user(Widget):
    def __init__(self, x, y, inform_list, transparency, background_color, font_color):
        super().__init__(x, y, 50 * len(inform_list), 25, transparency, background_color)
