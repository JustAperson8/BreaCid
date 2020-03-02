import pygame
from core.objects.object_image import ObjectImage
from core.objects.groups_of_sprites import *
from core.draw_something.useful_isntruments import set_color


class Cursor(ObjectImage, pygame.sprite.Sprite):
    def __init__(self, *names_of_images, rect_color="green"):
        ObjectImage.__init__(self, *names_of_images)
        pygame.mouse.set_visible(0)
        self.start_pos = None
        self.end_pos = None
        self.rect_pos = None
        self.default_rect()
        pygame.sprite.Sprite.__init__(self, hover_group)
        self.rect_color = rect_color

    def hover_rect(self, type, event_pos):
        if type == 0:
            self.start_pos = event_pos
        elif type == 1:
            self.rect_pos = [self.start_pos, [-1 * (self.start_pos[0] - event_pos[0]),
                                              -1 * (self.start_pos[1] - event_pos[1])]]
            self.end_pos = event_pos
        elif type == 2:
            self.start_pos = None
            self.end_pos = None
            self.rect_pos = None
            self.default_rect()
            return [self.rect.x, self.rect.y], [self.rect.x + self.rect.w, self.rect.y + self.rect.h]

    def render_image(self, scr, x, y):
        if self.start_pos and self.end_pos and self.rect_pos:
            self.update()
            hover_group.draw(scr)
            pygame.draw.rect(scr, set_color(self.rect_color, "green"), self.rect_pos, 1)
        if pygame.mouse.get_focused():
            scr.blit(self.ob_images[self.using_image], (x, y))

    def default_rect(self):
        rect_surf = pygame.Surface((0, 0))
        self.image = rect_surf
        self.rect = self.image.get_rect()

    def update(self, *args):
        x, y = sorted([self.start_pos[0], self.end_pos[0]]), sorted([self.start_pos[1], self.end_pos[1]])
        rect_surf = pygame.Surface((abs(x[1]-x[0]), abs(y[1]-y[0])), pygame.SRCALPHA)
        self.image = rect_surf
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x[0], y[0]
