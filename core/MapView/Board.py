import pygame
import os
from .download_image import download_image


class Board:
    # создание поля
    def __init__(self, width, height, screen, colors):
        """
        Create your board here!
        :param integer width: count of cells in width of board
        :param height: count of cells in height of board
        :param screen: screen of board. Example: scr = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
        :param colors: set colors of your cells (it can be path to file)
        """
        self.width = width
        self.height = height
        self.scr = screen
        self.go = False
        self.zn = [0, 1]
        self.board = [[0] * height for _ in range(width)]
        self.set_cell_color(colors)
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        """
        Here, you can set some params to view your game view
        :param left: margin space from left
        :param top: margin space form top
        :param cell_size: size of one cell on the map
        """
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def one_Cell(self, x, y, name=None):
        """
        Draw something if you have not textures
        :param x: x coord of center
        :param y: y coord of center
        :param p: color of cell, None is black
        """
        xo, yo = x + self.left, y + self.top
        try:
            self.set_cells_texture(xo, yo, name)
        except:
            self.draw_cell(xo, yo, name)

    def draw_cell(self, xo, yo, color):
        if color:
            pygame.draw.polygon(self.scr, pygame.Color(color),
                                [[xo - self.cell_size * 2, yo], [xo, yo - self.cell_size],
                                 [xo + self.cell_size * 2, yo], [xo, yo + self.cell_size]])
        else:
            pygame.draw.polygon(self.scr, pygame.Color("#353535"),
                                [[xo - self.cell_size * 2, yo], [xo, yo - self.cell_size],
                                 [xo + self.cell_size * 2, yo], [xo, yo + self.cell_size]], 1)

    def set_cells_texture(self, xo, yo, name):
        image = pygame.transform.scale(name, (self.cell_size*4, self.cell_size*2))
        self.scr.blit(image, (xo-self.cell_size*2, yo-self.cell_size))

    def render(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                x, y = self.center_of_cell(i, j)
                if x in range(-self.left - self.cell_size * 2, -self.left + 1366 + self.cell_size * 2) and \
                        y in range(-self.top - self.cell_size, -self.top + 768 + self.cell_size):
                    self.one_Cell(x, y, self.cell_color[self.board[i][j]])

    def center_of_cell(self, ix, iy):
        xz = self.cell_size * 2 * self.height + self.left
        yz = self.top + self.cell_size
        ox = xz + ix * 2 * self.cell_size - iy * self.cell_size * 2
        oy = yz + iy * self.cell_size + ix * self.cell_size
        return ox, oy

    def get_cell(self, mouse_pos):
        x, y = mouse_pos
        x, y = x - self.left, y - self.top
        for i in range(self.width):
            for j in range(self.height):
                cx, cy = self.center_of_cell(i, j)
                xn, yn = x - cx, y - cy
                if self.cell_size * -2 <= xn <= self.cell_size * 2 and (
                        (xn < 0 and (-xn) / 2 - self.cell_size <= yn <= xn / 2 + self.cell_size) or (
                        xn >= 0 and xn / 2 - self.cell_size <= yn <= (-xn) / 2 + self.cell_size)):
                    return i, j
        return None

    def on_click(self, cell_coords):
        pass

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell: self.on_click(cell)

    def set_cell_color(self, colors):
        lofcol = []
        for i in colors:
            if os.path.isfile(i):
                lofcol.append(download_image(i))
            else:
                lofcol.append(i)
        self.cell_color = lofcol

    def load_grid(self, name):
        pass
