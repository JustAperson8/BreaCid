import os
from ..draw_something import cell, place_between_levels
from ..download_something import download_image


class Board:
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
        self.cell_color = self.set_cell_color(cell_color)
        self.place_color = self.set_cell_color(place_color)
        self.texture_for_place = [[0] * height for _ in range(width)]
        self.left = 10
        self.top = 10
        self.cell_size = 30
        pass

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
        xo, yo = x + self.left, y + self.top
        for i in range(num_of_levels):
            if y + self.cell_size * i in range(-self.top - self.cell_size*10, -self.top + 768 + self.cell_size*10):
                try:
                    place_between_levels.set_texture_for_place(self.scr, self.cell_size, xo, yo + self.cell_size * i, name)
                except TypeError:
                    place_between_levels.draw_place(self.scr, self.cell_size, xo, yo + self.cell_size * i, name)

    def render(self):
        """
        This function draws a board.
        """
        for i in range(self.width):
            for j in range(self.height):
                x, y = self.center_of_cell(i, j)
                if i != self.width - 1 and self.height - 1 != j:
                    if self.level_of_terrain[i][j] > self.level_of_terrain[i][j + 1] or \
                        self.level_of_terrain[i][j] > self.level_of_terrain[i + 1][j]:
                        self.place_for_one_cell(x, y - self.cell_size * self.level_of_terrain[i][j],
                                self.level_of_terrain[i][j], self.place_color[self.texture_for_place[i][j]])
                else:
                    self.place_for_one_cell(x, y - self.cell_size * self.level_of_terrain[i][j],
                                            self.level_of_terrain[i][j], self.place_color[self.texture_for_place[i][j]])
                if x in range(-self.left - self.cell_size * 2, -self.left + 1366 + self.cell_size * 2) and \
                        y - self.cell_size * self.level_of_terrain[i][j] \
                        in range(-self.top - self.cell_size, - self.top + 768 + self.cell_size):

                    self.one_cell(x, y - self.cell_size * self.level_of_terrain[i][j],
                                  self.cell_color[self.board[i][j]])

    def center_of_cell(self, ix, iy):
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

    def get_cell(self, mouse_pos):
        """
        Find selected cell
        :param mouse_pos: coordinates of mouse position
        :return: indexes of cell (self.board[i][j])
        """
        x, y = mouse_pos
        x, y = x - self.left, y - self.top
        for i in range(self.width - 1, -1, -1):
            for j in range(self.height - 1, -1, -1):
                cx, cy = self.center_of_cell(i, j)
                cy = cy - self.level_of_terrain[i][j] * self.cell_size
                xn, yn = x - cx, y - cy
                if self.cell_size * -2 <= xn <= self.cell_size * 2 and (
                        (xn < 0 and (-xn) / 2 - self.cell_size <= yn <= xn / 2 + self.cell_size) or (
                        xn >= 0 and xn / 2 - self.cell_size <= yn <= (-xn) / 2 + self.cell_size)):
                    return i, j
        return None

    def on_click(self, cell_indexes):
        """
        Action for selected cell
        :param cell_indexes:
        """
        pass

    def get_click(self, mouse_pos):
        """
        Function joined on_click and get_cell
        :param mouse_pos: mouse position (event.pos)
        """
        cell = self.get_cell(mouse_pos)
        if cell:
            self.on_click(cell)

    def set_cell_color(self, colors):
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

    def set_terrain(self, board=None, level_of_terrain=None, texture_for_place=None):
        if board:
            self.board = board
        if level_of_terrain:
            self.level_of_terrain = level_of_terrain
        if texture_for_place:
            self.texture_for_place = texture_for_place
