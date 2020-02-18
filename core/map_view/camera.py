import pygame

class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0
        self.scale_left = 0
        self.scale_top = 0
        self.sensitivity = 16
        self.scale = 30

    def apply(self, obj):
        obj.cell_size = self.scale
        obj.left += self.dx * 2 + self.scale_left * self.scale
        obj.top += self.dy + self.scale_top * self.scale
        self.scale_top, self.scale_left = 0, 0

    def set_steps(self, x, y):
        self.dx, self.dy = x, y

    def update(self, situation):
        num = self.sensitivity
        if situation > 2: num = -self.sensitivity
        if situation % 2 == 0:
            self.dy += num
        else:
            self.dx += num

    def check_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.update(3)
        elif event.key == pygame.K_DOWN:
            self.update(4)
        elif event.key == pygame.K_LEFT:
            self.update(1)
        elif event.key == pygame.K_UP:
            self.update(2)

    def set_scale(self, event):
        if event.button == 5:
            if self.scale - 2 < 20:
                self.scale = 20
            else:
                self.scale -= 5
                self.scale_left += 1
                self.scale_top += 1
        elif event.button == 4:
            if self.scale + 2 > 50:
                self.scale = 50
            else:
                self.scale += 5
                self.scale_left -= 1
                self.scale_top -= 1
