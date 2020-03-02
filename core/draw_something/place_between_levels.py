import pygame
from core.draw_something.useful_isntruments import set_color


def draw_place(screen, cell_size, x, y, color):
    """
    Draw, if you haven't a texture
    :param screen: using screen
    :param cell_size: size of cell(1/2 of height)
    :param x: x coordinate of place in top middle
    :param y: y coordinate of place in top middle
    :param color: using color
    """
    pygame.draw.polygon(screen, set_color(color),
                        [[x - cell_size * 2, y], [x, y + cell_size], [x + cell_size * 2, y],
                         [x + cell_size * 2, y + cell_size], [x, y + cell_size * 2],
                         [x - cell_size * 2, y + cell_size]])
    scr = pygame.Surface((cell_size * 2 + 1, cell_size * 2), pygame.SRCALPHA)
    pygame.draw.polygon(scr, pygame.Color(0, 0, 0, 100),
                        [[0, cell_size], [cell_size * 2, 0],
                         [cell_size * 2, cell_size], [0, cell_size * 2]])
    screen.blit(scr, (x, y))


def set_texture_for_place(screen, cell_size, x, y, name):
    image = pygame.transform.scale(name, (cell_size * 4, cell_size * 2))
    screen.blit(image, (x - cell_size * 2, y))
