import pygame

def set_color(color, exception_color="black"):
    try:
        return pygame.Color(color)
    except ValueError:
        return pygame.Color(exception_color)
