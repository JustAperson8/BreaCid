import os
from core.download_something.download_image import download_image
from core.user_interface.widgets.widget import Widget
from core.draw_something.mini_cell import *
from core.draw_something.useful_isntruments import set_color


class Menu(Widget):
    def __init__(self, x, y, width, height, cells_information, components_status, transparency=200,
                 margin_cell_x=5, margin_cell_y=10, space_between_cells=2, cell_height=40, border_radius=0,
                 background_color="#24414e", cells_passive_view="grey", cells_hovered_view="#949494"):
        super().__init__(x, y, width, height, transparency, background_color)
        self.cell_inf, self.component_status = cells_information, components_status
        self.m_c_x, self.m_c_y, self.s_b_c = margin_cell_x, margin_cell_y, space_between_cells
        self.cell_pass_view, self.cell_hover_view = cells_passive_view, cells_hovered_view
        self.cell_height = cell_height
        self.border_radius = border_radius

    def set_cell_inf(self, information):
        """
        This function sets color or texture for cell
        :return: list of images and colors
        :param colors: list of colors or paths
        """
        lofinf = []
        for i in information:
            el = []
            for j in i:
                if os.path.isfile(j):
                    el.append(download_image(j))
                else:
                    el.append(j)
            lofinf.append(el)
        return lofinf

    def draw_in_widget(self):
        self.surf.fill(self.back_col)
        for i in range(len(self.cell_inf)):
            for j in range(len(self.cell_inf[i])):
                if self.component_status[i][j] == 0:
                    pygame.draw.rect(self.surf, set_color(self.cell_pass_view),
                                     [[self.w // len(self.cell_inf[i]) * j + self.m_c_x,
                                       self.cell_height * i + self.m_c_y],
                                      [(self.w - self.s_b_c * len(self.cell_inf[i]) - self.m_c_x * (
                                          len(self.cell_inf[i]))) // len(self.cell_inf[i]),
                                       self.cell_height - self.s_b_c]],
                                     self.border_radius)
                elif self.component_status[i][j] == 1:
                    pygame.draw.rect(self.surf, set_color(self.cell_hover_view),
                                     [[self.w // len(self.cell_inf[i]) * j + self.m_c_x,
                                       self.cell_height * i + self.m_c_y],
                                      [(self.w - self.s_b_c * len(self.cell_inf[i]) - self.m_c_x * len(
                                          self.cell_inf[i])) // len(self.cell_inf[i]), self.cell_height - self.s_b_c]],
                                     self.border_radius)

    def get_cell(self, x, y):
        for i in range(len(self.cell_inf)):
            for j in range(len(self.cell_inf[i])):
                scx = self.w // len(self.cell_inf[i]) * j + self.m_c_x
                scy = self.cell_height * i + self.m_c_y
                if scx <= x <= scx + (
                        self.w - self.s_b_c * len(self.cell_inf[i]) - self.m_c_x * (len(self.cell_inf[i]))) // len(
                        self.cell_inf[i]) and scy <= y <= scy + self.cell_height - self.s_b_c:
                    return i, j
        return None

    def on_click(self, cell):
        pass

    def on_hover(self, cell):
        cx, cy = cell
        c_s = []
        for i in self.component_status:
            el = []
            for j in i:
                if j == 2:
                    el.append(2)
                else:
                    el.append(0)
            c_s.append(el)
        c_s[cx][cy] = 1
        self.component_status = c_s

    def get_click_or_hover(self, x, y, type_act=0):
        cell = self.get_cell(x - self.x, y - self.y)
        if not cell:
            return False
        if type_act:
            self.on_click(cell)
        else:
            self.on_hover(cell)
        return True
