import pygame
from core.draw_something.useful_isntruments import set_color


def draw_cell(screen, cell_size, xo, yo, color):
    """
    Draw isometric cell if you have not texture
    :param xo: x coordinate of center
    :param yo: y coordinate of center
    :param screen: using screen
    :param cell_size: size of cell
    :param color: fill colour for cell (just name, for examlpe: '#FF0000' or 'red)
    """
    pygame.draw.polygon(screen, set_color(color),
                            [[xo - cell_size * 2, yo], [xo, yo - cell_size],
                             [xo + cell_size * 2, yo], [xo, yo + cell_size]])


def set_cells_texture(screen, cell_size, xo, yo, name):
    """
    This function sets texture for cell.
    Proportion of isometric cell must be - width:height = 2:Test_map
    :param xo: y coordinate of cell
    :param yo: x coordinate of cell
    :param name: name of path
    """
    image = pygame.transform.scale(name, (cell_size * 4, cell_size * 2))
    screen.blit(image, (xo - cell_size * 2, yo - cell_size))
