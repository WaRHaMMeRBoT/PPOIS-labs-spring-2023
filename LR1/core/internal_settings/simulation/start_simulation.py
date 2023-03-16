import sys

from core.internal_settings.screen.field import Field
from core.internal_settings.game_loader.file_loader import FieldLoader
from core.internal_settings.simulation.simulation import Simulation
from core.settings import settings


def start_simulation():
    loaded = False
    path = settings.FILE_PATH
    height = settings.HEIGHT
    width = settings.WIDTH

    for i in range(1, len(sys.argv)):
        if sys.argv[i] == "--load":
            loaded = True
            path = sys.argv[i + 1]
            i += 1
        elif sys.argv[i] == "--h":
            height = int(sys.argv[i + 1])
            i += 1
        elif sys.argv[i] == "--w":
            width = int(sys.argv[i + 1])
            i += 1

    if loaded:
        field = FieldLoader.load(path)
    else:
        field = Field(height=height, width=width)

    Simulation.start(field, settings.MAX_ITERS)
