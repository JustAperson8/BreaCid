import pygame
from core.draw_something.useful_isntruments import set_color

def draw_cell(screen, width, height, xo, yo, color):
    """
    Draw isometric cell if you have not texture
    :param xo: x coordinate of top left angle
    :param yo: y coordinate of top left angle
    :param screen: using screen
    :param cell_size: size of cell
    :param color: fill colour for cell (just name, for examlpe: '#FF0000' or 'red)
    """
    pygame.draw.polygon(screen, set_color(color), [[xo, yo], [xo + width, yo],
                                                   [xo + width, yo + height], [xo, yo + height]])

def set_cells_texture(screen, width, height, xo, yo, name):
    """
    This function sets texture for cell.
    :param xo: x coordinate of top left angle
    :param yo: y coordinate of top left angle
    :param name: name of path
    """
    image = pygame.transform.scale(name, (width, height))
    screen.blit(image, (xo, yo))