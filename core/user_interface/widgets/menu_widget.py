from core.user_interface.widgets.widget import Widget
import pygame
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

    def draw_in_widget(self):
        self.surf.fill(self.back_col)
        for i in range(len(self.cell_inf)):
            for j in range(len(self.cell_inf[i])):
                if self.component_status[i][j] == 0:
                    pygame.draw.rect(self.surf, set_color(self.cell_pass_view),
                                     [[self.w // len(self.cell_inf[i]) * j + self.m_c_x, self.cell_height * i + self.m_c_y],
                                      [(self.w - self.s_b_c*len(self.cell_inf[i]) - self.m_c_x*(len(self.cell_inf[i]))) // len(self.cell_inf[i]), self.cell_height-self.s_b_c]],
                                     self.border_radius)
                elif self.component_status[i][j] == 1:
                    pygame.draw.rect(self.surf, set_color(self.cell_hover_view),
                                     [[self.w // len(self.cell_inf[i]) * j + self.m_c_x, self.cell_height * i + self.m_c_y],
                                      [(self.w - self.s_b_c*len(self.cell_inf[i]) - self.m_c_x*len(self.cell_inf[i])) // len(self.cell_inf[i]), self.cell_height-self.s_b_c]],
                                     self.border_radius)

    def get_cell(self, x, y):
        return x, y

    def on_click(self, cx, cy):
        pass

    def get_click(self, mouse_pos):
        x, y, = mouse_pos
        cx, cy = self.get_cell(x - self.x, y - self.y)
        self.on_click(cx, cy)
