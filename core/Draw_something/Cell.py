import pygame


def draw_cell(screen, cell_size, xo, yo, color):
    """
    Draw isometric cell if you have not texture
    :param xo: x coordinate of center
    :param yo: y coordinate of center
    :param screen: your screen
    :param cell_size: size of cell
    :param color: fill colour for cell (just name, for examlpe: '#FF0000' or 'red)
    """
    try:
        pygame.draw.polygon(screen, pygame.Color(color),
                            [[xo - cell_size * 2, yo], [xo, yo - cell_size],
                             [xo + cell_size * 2, yo], [xo, yo + cell_size]])
    except ValueError:
        pygame.draw.polygon(screen, pygame.Color("#353535"),
                            [[xo - cell_size * 2, yo], [xo, yo - cell_size],
                             [xo + cell_size * 2, yo], [xo, yo + cell_size]], 1)


def set_cells_texture(screen, cell_size, xo, yo, name):
    """
    This function sets texture for cell.
    Proportion of isometric cell must be - width:height = 2:1
    :param xo: y coordinate of cell
    :param yo: x coordinate of cell
    :param name: name of path
    """
    image = pygame.transform.scale(name, (cell_size * 4, cell_size * 2))
    screen.blit(image, (xo - cell_size * 2, yo - cell_size))
