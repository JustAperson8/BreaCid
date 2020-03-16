import os
import pygame
from core.draw_something import cell, place_between_levels
from abc import ABC, abstractmethod
from core.download_something import download_image


class AbsBoard(ABC):
    left = 0
    top = 0
    cell_size = 30

    def __init__(self, width, height, screen, cell_color, place_color):
        """
        Create your board here!
        :param integer width: count of cells in width of board
        :param height: count of cells in height of board
        :param screen: screen of board. Example: scr = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
        :param cell_color: set colors of your cells (it can be path to file)
        """
        self.width = width
        self.height = height
        self.scr = screen
        self.level_of_terrain = [[0] * height for _ in range(width)]
        self.board = [[0] * height for _ in range(width)]
        self.cell_color = self._set_cell_color(cell_color)
        self.place_color = self._set_cell_color(place_color)
        self.texture_for_place = [[0] * height for _ in range(width)]

    @abstractmethod
    def render(self):
        pass

    def set_terrain(self, board=None, level_of_terrain=None, texture_for_place=None):
        """
        Set information of terrain here
        :param board: list of using textures for cells
        :param level_of_terrain: list of level of terrain
        :param texture_for_place: list of indexes of list of textures(or colors)
        """
        if board:
            self.board = board
        if level_of_terrain:
            self.level_of_terrain = level_of_terrain
        if texture_for_place:
            self.texture_for_place = texture_for_place

    @staticmethod
    def _set_cell_color(colors):
        """
        This function sets color or texture for cell
        :return: list of images and colors
        :param colors: list of colors or paths
        """
        lofcol = []
        for i in colors:
            if os.path.isfile(i):
                lofcol.append(download_image(i))
            else:
                lofcol.append(i)
        return lofcol

    @abstractmethod
    def set_view(self, left, top, cell_size):
        pass

    @abstractmethod
    def _on_click(self, cell_indexes):
        pass

    @abstractmethod
    def _get_cell(self, mouse_pos):
        pass

    def get_click(self, mouse_pos):
        """
        Function joined on_click and get_cell
        :param mouse_pos: mouse position (event.pos)
        """
        cell_in = self._get_cell(mouse_pos)
        if cell_in:
            self._on_click(cell_in)

    def _center_of_cell(self, ix, iy):
        """
        This function can help you to find the center coordinates of cell.
        :param ix: self.board[ix][0]
        :param iy: self.board[0][iy]
        :return: coordinates in the motorcade
        """
        xz = self.cell_size * 2 * self.height + self.left
        yz = self.top + self.cell_size
        ox = xz + ix * 2 * self.cell_size - iy * self.cell_size * 2
        oy = yz + iy * self.cell_size + ix * self.cell_size
        return ox, oy


class Board(AbsBoard):

    def set_view(self, left, top, cell_size):
        """
        Here, you can set some params to view
        :param left: margin space from left
        :param top: margin space from top
        :param cell_size: size of one cell on the map
        """
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def one_cell(self, x, y, name=None):
        """
        Draw something if you have not textures
        :param x: x coordinate of center
        :param y: y coordinate of center
        :param name: name of color or path to texture
        """
        xo, yo = x + self.left, y + self.top
        try:
            cell.set_cells_texture(self.scr, self.cell_size, xo, yo, name)
        except TypeError:
            cell.draw_cell(self.scr, self.cell_size, xo, yo, name)

    def place_for_one_cell(self, x, y, num_of_levels, name=None):
        """
        Draw place (not stairs)
        :param x: x of cell
        :param y: y of cell
        :param num_of_levels: element of level_of_terrain
        :param name: name of color or path to texture
        """
        xo, yo = x + self.left, y + self.top
        for i in range(num_of_levels):
            if y + self.cell_size * i in range(-self.top - self.cell_size * 2, -self.top + 478 + self.cell_size * 2):
                try:
                    place_between_levels.set_texture_for_place(self.scr, self.cell_size, xo, yo + self.cell_size * i,
                                                               name)
                except TypeError:
                    place_between_levels.draw_place(self.scr, self.cell_size, xo, yo + self.cell_size * i, name)

    def render(self):
        """
        This function draws a board.
        """
        for i in range(self.width):
            for j in range(self.height):
                x, y = self._center_of_cell(i, j)
                if i != self.width - 1 and self.height - 1 != j:
                    if self.level_of_terrain[i][j] > self.level_of_terrain[i][j + 1] or \
                            self.level_of_terrain[i][j] > self.level_of_terrain[i + 1][j]:
                        self.place_for_one_cell(x, y - self.cell_size * self.level_of_terrain[i][j],
                                                self.level_of_terrain[i][j],
                                                self.place_color[self.texture_for_place[i][j]])
                else:
                    self.place_for_one_cell(x, y - self.cell_size * self.level_of_terrain[i][j],
                                            self.level_of_terrain[i][j], self.place_color[self.texture_for_place[i][j]])
                if x in range(-self.left - self.cell_size * 2, -self.left + 1366 + self.cell_size * 2) and \
                        y - self.cell_size * self.level_of_terrain[i][j] \
                        in range(-self.top - self.cell_size, - self.top + 510 + self.cell_size):
                    self.one_cell(x, y - self.cell_size * self.level_of_terrain[i][j],
                                  self.cell_color[self.board[i][j]])

    def _get_cell(self, mouse_pos):
        """
        Find selected cell
        :param mouse_pos: coordinates of mouse position
        :return: indexes of cell (self.board[i][j])
        """
        x, y = mouse_pos
        x, y = x - self.left, y - self.top
        for i in range(self.width - 1, -1, -1):
            for j in range(self.height - 1, -1, -1):
                cx, cy = self._center_of_cell(i, j)
                cy = cy - self.level_of_terrain[i][j] * self.cell_size
                xn, yn = x - cx, y - cy
                if self.cell_size * -2 <= xn <= self.cell_size * 2 and (
                        (xn < 0 and (-xn) / 2 - self.cell_size <= yn <= xn / 2 + self.cell_size) or (
                        xn >= 0 and xn / 2 - self.cell_size <= yn <= (-xn) / 2 + self.cell_size)):
                    return i, j
        return None


class GameBoard(AbsBoard):
    def __init__(self, width, height, screen, cell_color, place_color, min_cell_size=20, max_cell_size=40, size_step=5):
        super().__init__(width, height, screen, cell_color, place_color)
        self.surfaces = []
        self.cell_min = min_cell_size
        self.cells_max = max_cell_size
        self.scale_levels = [i for i in range(min_cell_size, max_cell_size, size_step)]
        self.size_step = size_step
        self.number_of_surface = 0
        self.cell_size = min_cell_size

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        if cell_size not in self.scale_levels:
            self.number_of_surface = -1
        else:
            self.number_of_surface = self.scale_levels.index(cell_size)

    def center_of_cell_surf(self, ix, iy):
        xz = self.cell_size * self.height * 2
        yz = self.cell_size
        ox = xz + ix * 2 * self.cell_size - iy * self.cell_size * 2
        oy = yz + iy * self.cell_size + ix * self.cell_size
        return ox, oy

    def place_for_one_cell_surf(self, screen, x, y, num_of_levels, name=None):
        """
        Draw place (not stairs)
        :param screen: using screen
        :param x: x of cell
        :param y: y of cell
        :param num_of_levels: element of level_of_terrain
        :param name: name of color or path to texture
        """
        xo, yo = x + self.left, y + self.top
        for i in range(num_of_levels):
            try:
                place_between_levels.set_texture_for_place(screen, self.cell_size, xo, yo + self.cell_size * i, name)
            except TypeError:
                place_between_levels.draw_place(screen, self.cell_size, xo, yo + self.cell_size * i, name)

    def one_cell_surf(self, screen, x, y, name=None):
        """
        Draw something if you have not textures
        :param x: x coordinate of center
        :param y: y coordinate of center
        :param name: name of color or path to texture
        """
        xo, yo = x + self.left, y + self.top
        try:
            cell.set_cells_texture(screen, self.cell_size, xo, yo, name)
        except TypeError:
            cell.draw_cell(screen, self.cell_size, xo, yo, name)

    def create_terrain_surf(self):
        surf = pygame.Surface((self.width * 4 * self.cell_size, self.height * 2 * self.cell_size))
        for i in range(self.width):
            for j in range(self.height):
                x, y = self.center_of_cell_surf(i, j)
                if i != self.width - 1 and self.height - 1 != j:
                    if self.level_of_terrain[i][j] > self.level_of_terrain[i][j + 1] or \
                            self.level_of_terrain[i][j] > self.level_of_terrain[i + 1][j]:
                        self.place_for_one_cell_surf(surf, x, y - self.cell_size * self.level_of_terrain[i][j],
                                                     self.level_of_terrain[i][j],
                                                     self.place_color[self.texture_for_place[i][j]])
                else:
                    self.place_for_one_cell_surf(surf, x, y - self.cell_size * self.level_of_terrain[i][j],
                                                 self.level_of_terrain[i][j],
                                                 self.place_color[self.texture_for_place[i][j]])
                self.one_cell_surf(surf, x, y - self.cell_size * self.level_of_terrain[i][j],
                                   self.cell_color[self.board[i][j]])
        return surf

    def render(self):
        save_cell_size = self.cell_size
        for i in self.scale_levels:
            self.cell_size = i
            self.surfaces.append(self.create_terrain_surf())
        self.cell_size = save_cell_size

    def draw(self):
        self.scr.blit(self.surfaces[self.number_of_surface], (self.left, self.top))

    def _get_cell(self, mouse_pos):
        """
        Find selected cell
        :param mouse_pos: coordinates of mouse position
        :return: indexes of cell (self.board[i][j])
        """
        x, y = mouse_pos
        for i in range(self.width - 1, -1, -1):
            for j in range(self.height - 1, -1, -1):
                cx, cy = self._center_of_cell(i, j)
                cy = cy - self.level_of_terrain[i][j] * self.cell_size
                xn, yn = x - cx, y - cy
                if self.cell_size * -2 <= xn <= self.cell_size * 2 and (
                        (xn < 0 and (-xn) / 2 - self.cell_size <= yn <= xn / 2 + self.cell_size) or (
                        xn >= 0 and xn / 2 - self.cell_size <= yn <= (-xn) / 2 + self.cell_size)):
                    return i, j
        return None
