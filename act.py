from core import map_view
from core.download_something import download_map_format_brcd, download_list_of_images_format_brcd
from core.user_interface.widgets.minimap_widget import Mini_map
from core.user_interface.widgets.clock import Clock as widget_clock
from core.user_interface.widgets.information_bar import InformationBar
from core.user_interface import Cursor
from core.objects.object_image import ObjectImage
from core.objects.groups_of_sprites import *
from core.objects.object_sprite import ObjectSprite
import pygame

pygame.mixer.init()
pygame.init()
deviceInfo = pygame.display.Info()
pygame.display.set_icon(pygame.image.load(".data/icons/icon.png"))
scr = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
loading_screen = ObjectImage(".data/loading_screen/wallpaper.jpg",
                             ".data/loading_screen/47.png")
loading_screen.switch_image(1)
loading_screen.render_image(scr, 0, 0)

pygame.display.flip()
MYEVENTTYPE = 30
fps = 60
res = [0, 0, 0]
cursor = Cursor(".data/cursors/cur1.png", ".data/cursors/cur2.png", rect_color="orange")
print(hover_group)
for i in hover_group:
    print(i.rect)
dock = ObjectImage("dock.png")
un = True


class Constructor(map_view.GameBoard):
    def on_click(self, cell_indexes):
        x, y = cell_indexes
        self.board[x][y] = [i for i in range(len(self.cell_color))][(self.board[x][y] + 1) % len(self.cell_color)]
        print(x, y)


map_data = download_map_format_brcd("./.data/maps/Test_map/h.brcd")
tex_data = download_list_of_images_format_brcd("./.data/maps/Test_map/t.brcd")
min_map = Mini_map(0, deviceInfo.current_h - 220, 180, 180, map_data[0], tex_data[2])
min_map.draw_in_widget()
wc = widget_clock(10, deviceInfo.current_h - 265, 255, "black", "#e0a339", font_style=".data/fonts/Od.ttf", font_size=16, left=5, top=5)
board = Constructor(len(map_data[0]), len(map_data[0][0]), scr, tex_data[0], tex_data[1], min_cell_size=10,
                    size_step=2, max_cell_size=30)
ib = InformationBar(deviceInfo.current_w - 100 * len(res), 0, [".data/icons/RAM.png", "blue", "orange"], res,
                    transparency=100,
                    font_color="orange", font_style=".data/fonts/Od.ttf")
board.set_terrain(map_data[0], map_data[1], map_data[2])
board.render()
pygame.time.set_timer(MYEVENTTYPE, 1000)
clock = pygame.time.Clock()
camera = map_view.Camera(10, 30, 2)
pygame.mixer.music.load(".data/sound/Deeb-Bridges.wav")
pygame.mixer.music.play()
gg = ObjectSprite(your_army_kernel)
gg.add_group_of_images(".data/sprites/1.png", type_of_images=-1)
gg.add_images(".data/cursors/cur1.png")
gg.switch_image(0)
gg.set_pos(1800, 900)
running = True
while running:
    x, y = pygame.mouse.get_pos()
    if not un:
        cursor.hover_rect(1, (x, y))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MYEVENTTYPE:
            wc.tick()
            wc.draw_in_widget()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            un = False
            cursor.hover_rect(0, event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1 and not un:
                un = True
                cursor.hover_rect(2, event.pos)
            elif event.button == 4 or event.button == 5:
                camera.set_scale(event)
            else:
                board.get_click(event.pos)
        elif event.type == pygame.KEYDOWN:
            camera.check_event(event)
        elif event.type == pygame.KEYUP and event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]:
            camera.set_steps(0, 0)
        elif event.type == pygame.KEYUP and event.key == pygame.K_q:
            cell = board.get_cell((x, y))
            if cell:
                k, v = cell
                board.level_of_terrain[k][v] += 1
        elif event.type == pygame.KEYUP and event.key == pygame.K_w:
            cell = board.get_cell((x, y))
            if cell:
                k, v = cell
                board.level_of_terrain[k][v] -= 1
    camera.apply(board)
    clock.tick(fps)
    scr.fill((0, 0, 0))
    board.draw()
    camera.apply_for_sprite(your_army_kernel)
    your_army_kernel.draw(scr)
    hover_group.draw(scr)
    min_map.update(scr)
    ib.draw_in_widget()
    ib.update(scr)
    dock.render_image(scr, 0, deviceInfo.current_h - 280)
    wc.update(scr)
    cursor.switch_image(un)
    cursor.render_image(scr, x - 10, y - 5)
    pygame.display.flip()
