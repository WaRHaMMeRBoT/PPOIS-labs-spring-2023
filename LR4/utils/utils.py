import pygame
from pygame import Surface


def overlay_fill(surface, color) -> Surface:                                            #отрисовка экрана меню
    """Multiply all pixels of the surface by color, preserve transparency."""
    w, h = surface.get_size()
    r, g, b, _ = color
    for x in range(w):
        for y in range(h):
            surface.set_at((x, y), pygame.Color(int(r / 255 * surface.get_at((x, y))[0]),\
                                                 int(g / 255 * surface.get_at((x, y))[1]),\
                                                   int(b / 255  * surface.get_at((x, y))[2]),\
                                                     int(surface.get_at((x, y))[3])))

    return surface


def render_multiline(surface, font, text, x, y, fsize):                                     #отрисовка таблицы лидеров
        lines = text.splitlines()
        for i, l in enumerate(lines):
            surface.blit(font.render(l, 0, 'White'), (x, y + fsize * i))                    #отрисовка пиксельного текста
