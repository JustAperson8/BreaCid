import pygame
from core.draw_something.object import Object_image
from core.draw_something.useful_isntruments import set_color


class Cursor(Object_image):
    def __init__(self, *names_of_images, rect_color="green"):
        super().__init__(*names_of_images)
        pygame.mouse.set_visible(0)
        self.start_pos = None
        self.end_pos = None
        self.rect_pos = None
        self.rect_color = rect_color

    def hover_rect(self, type, event_pos):
        if type == 0:
            self.start_pos = event_pos
        elif type == 1:
            self.rect_pos = [self.start_pos, [-1 * (self.start_pos[0] - event_pos[0]),
                                              -1 * (self.start_pos[1] - event_pos[1])]]
            self.end_pos = event_pos
        elif type == 2:
            x, y = sorted([self.start_pos[0], self.end_pos[0]]), sorted([self.start_pos[1], self.end_pos[1]])
            self.start_pos = None
            self.end_pos = None
            self.rect_pos = None
            return [x[0], y[0]], [x[1], y[1]]

    def render_image(self, scr, x, y):
        if self.start_pos and self.end_pos and self.rect_pos:
            pygame.draw.rect(scr, set_color(self.rect_color, "green"), self.rect_pos, 1)
        if pygame.mouse.get_focused():
            scr.blit(self.ob_images[self.using_cursor], (x, y))

