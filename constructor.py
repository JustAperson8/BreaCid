import core.MapView as MapView
import pygame

pygame.init()
scr = pygame.display.set_mode((0, 0), pygame.RESIZABLE)
clock = pygame.time.Clock()
fps = 60
pygame.mouse.set_visible(0)
curB = MapView.download_image(".data/cursors/cur1.png")
curA = MapView.download_image(".data/cursors/cur2.png")
un = True


def cursor(scr, x, y, yn):
    if not pygame.mouse.get_focused():
        return
    if yn:
        scr.blit(curB, (x, y))
    else:
        scr.blit(curA, (x, y))


class Constructor(MapView.Board):
    def on_click(self, cell_coords):
        x, y = cell_coords
        self.board[x][y] = [i for i in range(len(self.cell_color))][(self.board[x][y] + 1) % len(self.cell_color)]


board = Constructor(100, 100, scr, [0, ".data/textures/Dirt_texture.png",
                                    ".data/textures/Slime_texture.png",
                                    ".data/textures/White_and_brown_texture.png", "#00557f", "#005500"])
board.set_view(0, 0, 30)
camera = MapView.Camera()
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
            un = not un
        elif event.type == pygame.MOUSEBUTTONUP:
            board.get_click(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                camera.update(3)
            elif event.key == pygame.K_DOWN:
                camera.update(4)
            elif event.key == pygame.K_LEFT:
                camera.update(1)
            elif event.key == pygame.K_UP:
                camera.update(2)
        elif event.type == pygame.KEYUP and event.key in [pygame.K_UP, pygame.K_DOWN, pygame.K_RIGHT, pygame.K_LEFT]:
            camera.set_steps(0, 0)

    camera.apply(board)
    clock.tick(fps)
    scr.fill((0, 0, 0))
    board.render()
    x, y = pygame.mouse.get_pos()
    cursor(scr, x - 10, y - 5, un)
    pygame.display.flip()
