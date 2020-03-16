from core.draw_something.mini_cell import draw_cell, set_cells_texture
from core.user_interface.widgets.widget import Widget
import pygame
from core.draw_something.useful_isntruments import set_color
from core.map_view.set_cell_color import set_cell_color


class InformationBar(Widget):
    def __init__(self, x, y, image_list, inform_list, letter_list=None, transparency=100, background_color="black",
                 font_color="white", font_style=None, font_size=16, left=5, top=5):
        super().__init__(x, y, 100 * len(inform_list) + 10, top * 2 + font_size, transparency, background_color)
        self.font_color = set_color(font_color)
        self.font_style = font_style
        self.left, self.top = left, top
        self.font_size = font_size
        if letter_list:
            self._letter_list = letter_list
        else:
            self._letter_list = ['' for _ in range(len(inform_list))]
        self._inform_list = inform_list
        self._image_list = set_cell_color(image_list)

    def draw_in_widget(self):
        self.surf.fill(self.back_col)
        font = pygame.font.Font(self.font_style, self.font_size)
        for i in range(len(self._inform_list)):
            try:
                set_cells_texture(self.surf, 20, 20, i * 100 + 5, 5, self._image_list[i])
            except TypeError:
                draw_cell(self.surf, self.font_size, self.font_size, 100 * i + 5, 5, self._image_list[i])
            text = font.render(str(int(self._inform_list[i])) + self._letter_list[i], 1, self.font_color)
            self.surf.blit(text, (i * 100 + 30, self.top))

    def set_list_of_images(self, image_list):
        self._image_list = set_cell_color(image_list)

    def set_list_of_information(self, inform_list):
        self._inform_list = inform_list

    def set_list_of_letters(self, letter_list):
        self._letter_list = letter_list
