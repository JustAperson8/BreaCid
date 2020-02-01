class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0
        self.sensitivity = 8

    def apply(self, obj):
        obj.left += self.dx
        obj.top += self.dy

    def set_steps(self, x, y):
        self.dx, self.dy = x, y

    def update(self, sit):
        num = self.sensitivity
        if sit > 2: num = -self.sensitivity
        if sit % 2 == 0:
            self.dy += num
        else:
            self.dx += num * 2
