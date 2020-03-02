import pygame
from core.draw_something import cell
from core.map_view import Board
from core.draw_something import place_between_levels


class GameBoard(Board):
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
        super().set_view(left, top, cell_size)
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

    def get_cell(self, mouse_pos):
        """
        Find selected cell
        :param mouse_pos: coordinates of mouse position
        :return: indexes of cell (self.board[i][j])
        """
        x, y = mouse_pos
        # x, y = x - self.left, y - self.top
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
