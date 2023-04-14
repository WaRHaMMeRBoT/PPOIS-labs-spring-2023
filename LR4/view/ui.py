from itertools import product

import pygame
import pygame_menu

from controller.utils import add_instance, next


class Ui:
    def __init__(self, field):
        self.field = field
        self.menu = pygame_menu.Menu(
            "",
            pygame.display.Info().current_w,
            pygame.display.Info().current_h,
            theme=pygame_menu.themes.THEME_DARK,
            columns=4,
            rows=2,
        )

        self.table = self.menu.add.table()
        self.table.resize(width=60, height=60)

        for y in range(self.field.area[1]):
            row = list()
            for x in range(self.field.area[0]):
                row.append(
                    pygame_menu.widgets.Image("./img/back.png", scale=(0.2, 0.2))
                )
            self.table.add_row(
                row, cell_align=pygame_menu.locals.ALIGN_CENTER, cell_border_width=0
            )

        self.menu.add.button("Next", next, field, 1, self._draw_field)
        self.menu.add.button(
            "Add shark", add_instance, field, "shark", self._draw_field
        )
        self.menu.add.button(
            "Add parrotfish", add_instance, field, "parrotfish", self._draw_field
        )
        self.menu.add.button(
            "Add barracuda", add_instance, field, "barracuda", self._draw_field
        )
        self.menu.add.button(
            "Add plant", add_instance, field, "plant", self._draw_field
        )
        self.menu.add.button("Exit", self.menu.disable)

    def _draw_field(self):
        for x, y in product(range(self.field.area[0]), range(self.field.area[1])):
            image = pygame_menu.baseimage.BaseImage("./img/back.png")
            image.scale(0.2, 0.2)
            self.table.get_cell(x + 1, y + 1).set_image(image)
        for animal in self.field.livings:
            cell = self.table.get_cell(
                self.field.livings[animal][0] + 1, self.field.livings[animal][1] + 1
            )
            match animal.class_name():
                case "shark":
                    image = pygame_menu.baseimage.BaseImage("./img/shark.png")
                    image.scale(0.2, 0.2)
                    cell.set_image(image)
                case "parrotfish":
                    image = pygame_menu.baseimage.BaseImage("./img/parrotfish.png")
                    image.scale(0.118, 0.118)
                    cell.set_image(image)
                case "barracuda":
                    image = pygame_menu.baseimage.BaseImage("./img/barracuda.png")
                    image.scale(0.092, 0.1)
                    cell.set_image(image)

        for plant in self.field.plants:
            cell = self.table.get_cell(
                self.field.plants[plant][0] + 1, self.field.plants[plant][1] + 1
            )
            image = pygame_menu.baseimage.BaseImage("./img/grass.png")
            image.scale(0.035, 0.035)
            cell.set_image(image)

    def run_ui(self, display: pygame.display):
        self.menu.mainloop(display, bgfun=self._draw_field)
