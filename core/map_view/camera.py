import pygame


class Camera:
    def __init__(self, min_cell_size=20, max_cell_size=50, size_step=5):
        self.dx = 0
        self.dy = 0
        self.scale_left = 0
        self.scale_top = 0
        self.sensitivity = 16
        self.scale = 30
        self.min_cell_size = min_cell_size
        self.max_cell_size = max_cell_size
        self.size_step = size_step

    def apply(self, obj):
        # obj.cell_size = self.scale
        obj.set_view(obj.left + self.dx * 2, obj.top + self.dy, self.scale)

    def apply_for_sprite(self, obj):
        obj.update(self.dx*2, self.dy, self.scale)

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
            if self.scale - self.size_step < self.min_cell_size:
                self.scale = self.min_cell_size
            else:
                self.scale -= self.size_step
        elif event.button == 4:
            if self.scale + self.size_step > self.max_cell_size:
                self.scale = self.max_cell_size
            else:
                self.scale += self.size_step
