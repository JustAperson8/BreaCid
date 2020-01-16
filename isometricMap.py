import pygame

pygame.init()
scr = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()
fps = 60


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.go = False
        self.zn = [0, 1]
        self.board = [[0] * height for _ in range(width)]
        # значения по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30

    # настройка внешнего вида
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def one_Cell(self, x, y, p=0):
        global scr
        xo, yo = x + self.left, y + self.top
        if p:
            pygame.draw.polygon(scr, pygame.Color("#FFFFFF"),
                                [[xo - self.cell_size * 2, yo], [xo, yo - self.cell_size],
                                 [xo + self.cell_size * 2, yo], [xo, yo + self.cell_size]])
        pygame.draw.polygon(scr, pygame.Color("#FFFFFF"),
                            [[xo - self.cell_size * 2, yo], [xo, yo - self.cell_size],
                             [xo + self.cell_size * 2, yo], [xo, yo + self.cell_size]], 1)

    # Отрисовка
    def render(self):
        global scr
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                x, z = self.center_of_cell(i, j)
                self.one_Cell(x, z, self.board[i][j])

    def center_of_cell(self, ix, iy):
        xz = self.cell_size * 2 * self.height + self.left
        yz = self.top + self.cell_size
        ox = xz + ix * 2 * self.cell_size - iy * self.cell_size * 2
        oy = yz + iy * self.cell_size + ix * self.cell_size
        return ox, oy

    # Возврат индекса клетки в списке
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

    # Обработка
    def on_click(self, cell_coords):
        x, y = cell_coords
        self.board[x][y] = [1, 0][self.board[x][y]]


    # "Диспечер", связывающий два предыдущих элемента вместе
    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        if cell: self.on_click(cell)


board = Board(6, 6)
board.set_view(0, 0, 25)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            board.get_click(event.pos)
    clock.tick(fps)
    scr.fill((0, 0, 0))
    board.render()
    pygame.display.flip()
