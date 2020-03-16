from core import map_view
from core.download_something import download_map_format_brcd, download_list_of_images_format_brcd
from core.user_interface.widgets.minimap_widget import Mini_map
from core.user_interface.widgets.clock import Clock as widget_clock
from core.user_interface.widgets.information_bar import InformationBar
from core.user_interface import Cursor
from core.save_something.format_brcd import save_map_format_brcd, save_list_of_images_format_brcd
from core.objects.object_image import ObjectImage
import pygame

pygame.init()
pygame.display.set_icon(pygame.image.load(".data/icons/icon.png"))
MYEVENTTYPE = 30
pygame.time.set_timer(MYEVENTTYPE, 1000)
scr = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
clock = pygame.time.Clock()
fps = 60
res = [0, 0, 0]
cursor = Cursor(".data/cursors/cur1.png", ".data/cursors/cur2.png", rect_color="orange")
dock = ObjectImage("dock.png")
un = True


class Constructor(map_view.Board):
    def _on_click(self, cell_indexes):
        x, y = cell_indexes
        self.board[x][y] = [i for i in range(len(self.cell_color))][(self.board[x][y] + 1) % len(self.cell_color)]

    def get_key(self, cell_coordinates, event):
        x, y = cell_coordinates
        cell = board._get_cell((x, y))
        if cell:
            if event.key == pygame.K_w:
                self.up_or_down(cell, 1)
            elif event.key == pygame.K_q:
                self.up_or_down(cell, -1)

    def up_or_down(self, cell, step):
        k, v = cell
        self.level_of_terrain[k][v] += step


map_data = download_map_format_brcd("./.data/maps/Test_map/h.brcd")
tex_data = download_list_of_images_format_brcd("./.data/maps/Test_map/t.brcd")
min_map = Mini_map(0, 750 - 200, 200, 255, map_data[0], tex_data[2])
min_map.draw_in_widget()
wc = widget_clock(9, 750 - 260, 255, "black", "#e0a339", font_style=".data/fonts/Od.ttf", font_size=16, left=6, top=5)
board = Constructor(len(map_data[0]), len(map_data[0][0]), scr, tex_data[0], tex_data[1])
ib = InformationBar(1366 - 100 * len(res), 0, [".data/icons/RAM.png", "blue", "orange"], res, transparency=100,
                    font_color="orange", font_size=16)
board.set_view(0, 0, 30)
board.set_terrain(map_data[0], map_data[1], map_data[2])
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
        elif event.type == pygame.KEYUP:
            board.get_key((x, y), event)
        elif event.type == pygame.KEYUP and event.key == pygame.K_s:
            save_map_format_brcd("./.data/maps/Test_map1/h.brcd",
                                 [board.board, board.level_of_terrain, board.texture_for_place],
                                 ["board", "level_of_terrain", "texture_for_place"])
            save_list_of_images_format_brcd("./.data/maps/Test_map1/t.brcd",
                                            tex_data,
                                            ["for_cell", "for_place", "for_minimap"])
    camera.apply(board)
    clock.tick(fps)
    scr.fill((55, 55, 55))
    board.render()
    min_map.update(scr)
    ib.draw_in_widget()
    ib.update(scr)
    dock.render_image(scr, 0, 478)
    wc.update(scr)
    cursor.switch_image(un)
    cursor.render_image(scr, x - 10, y - 5)
    pygame.display.flip()
