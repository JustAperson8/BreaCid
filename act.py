from core import map_view
from core.download_something import download_map_format_brcd, download_list_of_images_format_brcd
from core.user_interface.widgets.minimap_widget import Mini_map
from core.user_interface.widgets.clock import Clock as widget_clock
from core.user_interface.widgets.information_bar import InformationBar
from core.user_interface import Cursor
from core.draw_something.object import ObjectImage
import pygame

# version 0.1
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
dock = ObjectImage("dock.png")
un = True


class Constructor(map_view.GameBoard):
    def on_click(self, cell_indexes):
        x, y = cell_indexes
        self.board[x][y] = [i for i in range(len(self.cell_color))][(self.board[x][y] + 1) % len(self.cell_color)]
        print(x, y)


map_data = download_map_format_brcd("./.data/maps/Test_map1/h.brcd")
tex_data = download_list_of_images_format_brcd("./.data/maps/Test_map1/t.brcd")
min_map = Mini_map(0, deviceInfo.current_h - 220, 180, 180, map_data[0], tex_data[2])
min_map.draw_in_widget()
wc = widget_clock(10, deviceInfo.current_h - 265, 255, "black", "#e0a339")
board = Constructor(len(map_data[0]), len(map_data[0][0]), scr, tex_data[0], tex_data[1])
ib = InformationBar(deviceInfo.current_w - 100 * len(res), 0, [".data/icons/RAM.png", "blue", "orange"], res,
                    transparency=100,
                    font_color="orange")
board.set_terrain(map_data[0], map_data[1], map_data[2])
board.render()
pygame.time.set_timer(MYEVENTTYPE, 1000)
clock = pygame.time.Clock()
camera = map_view.Camera()
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
            min_map.draw_in_widget()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            un = False
            cursor.hover_rect(0, event.pos)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 3 and not un:
                un = True
                print(cursor.hover_rect(2, event.pos))
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
    min_map.update(scr)
    ib.draw_in_widget()
    ib.update(scr)
    dock.render_image(scr, 0, deviceInfo.current_h - 280)
    wc.update(scr)
    cursor.switch_image(un)
    cursor.render_image(scr, x - 10, y - 5)
    pygame.display.flip()
