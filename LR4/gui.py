import pygame

import models.ocean as ocean
import view.ui as ui


def main():
    pygame.init()
    display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    field = ocean.Ocean((20, 20))

    try:
        with open("./state.json", "r") as area:
            field = ocean.parse_json(area.read())
    except FileNotFoundError:
        pass

    menu = ui.Ui(field)
    menu.run_ui(display)

    text = ocean.convert_to_json(field)
    with open("./state.json", "w") as area:
        area.write(text)


if __name__ == "__main__":
    main()
