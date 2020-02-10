import pygame

def set_color(color):
    try:
        return pygame.Color(color)
    except ValueError:
        return pygame.Color("black")
