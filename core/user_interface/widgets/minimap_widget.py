from core.user_interface.widgets.widget import Widget
from core.draw_something.mini_cell import draw_cell, set_cells_texture
from core.map_view.set_cell_color import set_cell_color


class Mini_map(Widget):
    def __init__(self, x, y, width, height, board, cell_mini_colour, transparency=255, background_color=None):
        super().__init__(x, y, width, height, transparency, background_color)
        self.board = board
        self.cell_mini_colour = set_cell_color(cell_mini_colour)

    def draw_in_widget(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                try:
                    set_cells_texture(self.surf, self.w // len(self.board), self.h // len(self.board[i]),
                                      self.w // len(self.board) * i, self.h // len(self.board[i]) * j,
                                      self.cell_mini_colour[self.board[i][j]])
                except TypeError:
                    draw_cell(self.surf, self.w // len(self.board), self.h // len(self.board[i]),
                              self.w // len(self.board) * i, self.h // len(self.board[i]) * j,
                              self.cell_mini_colour[self.board[i][j]])
