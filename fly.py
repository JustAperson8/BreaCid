from core.objects.object_sprite import ObjectSprite
from core.user_interface.widgets.information_bar import InformationBar
from core.objects.object_image import ObjectImage
import pygame

pygame.init()
scr = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
deviceInfo = pygame.display.Info()
pygame.mixer.init()
gamer = pygame.sprite.Group()
pygame.mixer.music.load(".data/sound/Nature_sounds_1.wav")
# pygame.mixer.music.play()
# Можно включать, но при тестах бесит звук.
bird_size_w, bird_size_h = 100, 100
resources = [0]
ib = InformationBar(deviceInfo.current_w - 100 * len(resources), 0, ["green"], resources, letter_list=['M'],
                    transparency=100, font_style=".data/fonts/Od.ttf")


class GamersSprite(ObjectSprite):
    def __init__(self, *list_of_groups, acceleration=1, end_speed=20):
        super().__init__(list_of_groups)
        self._speed = 0
        self._end_speed = end_speed
        self._a = acceleration
        self._fly = True

    def set_physics(self, acceleration=1, end_speed=20):
        self._a = acceleration
        self._end_speed = end_speed

    def update(self, *args):
        self._fly = args[0]
        if args[1]:
            self._speed = 0
        if self._speed < self._end_speed:
            self._speed += self._a
        if self._fly:
            self.rect = self.rect.move(speed*2.5 - speed, int(-self._speed))
        else:
            self.rect = self.rect.move(-speed, int(self._speed * 2))


fly = False
bird = GamersSprite(gamer, acceleration=0.1, end_speed=5)
bird.add_group_of_images(".data/sprites/2.png", type_of_images=-1)
background = ObjectImage(".data/loading_screen/47.png")
bird.switch_image(0)
bird.set_image_size(bird_size_w, bird_size_h)
bird.set_rect_size(bird_size_w, bird_size_h)
bird.set_pos(100, 100)
run = True
start = False
speed = 1 
x = 0
clock = pygame.time.Clock()
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            fly = True
            start = True
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            start = True
            fly = False
    gamer.update(fly, start)
    start = False
    scr.fill((0, 0, 0))
    x -= speed / 10
    resources[0] += speed // 10
    ib.draw_in_widget()
    ib.set_list_of_information(resources)
    background.render_image(scr, x, 0)
    ib.update(scr)
    gamer.draw(scr)
    pygame.display.flip()
    clock.tick(60)
