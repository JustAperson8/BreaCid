import pygame
from core.draw_something import cell
from core.map_view import Board
from core.draw_something import place_between_levels


class GameBoard(Board):
    def __init__(self, width, height, screen, cell_color, place_color, min_cell_size=20, max_cell_size=50, size_step=5):
        super().__init__(width, height, screen, cell_color, place_color)
        self.surfaces = []
        self.cell_min = min_cell_size
        self.cells_max = max_cell_size
        self.size_step = size_step

    def place_for_one_cell(self, screen, x, y, num_of_levels, name=None):
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

    def one_cell(self, screen, x, y, name=None):
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

    def create_terrain_surf(self, cell_size):
        surf = pygame.Surface((self.width * 4 * cell_size, self.height * 2 * cell_size))
        for i in range(self.width):
            for j in range(self.height):
                x, y = self.center_of_cell(i, j)
                if i != self.width - 1 and self.height - 1 != j:
                    if self.level_of_terrain[i][j] > self.level_of_terrain[i][j + 1] or \
                            self.level_of_terrain[i][j] > self.level_of_terrain[i + 1][j]:
                        self.place_for_one_cell(surf, self.place_color[self.texture_for_place[i][j]], x,
                                                y - self.cell_size * self.level_of_terrain[i][j],
                                                self.level_of_terrain[i][j])
                else:
                    self.place_for_one_cell(surf, self.place_color[self.texture_for_place[i][j]], x,
                                            y - self.cell_size * self.level_of_terrain[i][j],
                                            self.level_of_terrain[i][j])
                self.one_cell(x, y - self.cell_size * self.level_of_terrain[i][j], self.cell_color[self.board[i][j]])
        return surf

    def render(self):
        self.surfaces = [self.create_terrain_surf(i) for i in range(self.cell_min, self.cells_max, self.size_step)]

    def draw(self, num):
        self.scr.blit(self.surfaces[num], (self.left, self.top))
