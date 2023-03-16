import msvcrt
import time

from core.internal_settings.screen.field import Field
from core.internal_settings.game_loader.file_loader import FieldLoader
from core.internal_settings.game_state import GameState
from core.internal_settings.screen.view import View


class Simulation:
    @staticmethod
    def start(field: Field, max_iters: int):
        try:
            while max_iters > 0:
                Simulation.executeGameLoop(field)
                max_iters -= 1
            while True:
                Simulation.executeGameLoop(field)
                View.draw(field)
                time.sleep(1)
        except Exception:
            View.clear()
            print("Something gone wrong. Simulation will continue in 5 seconds.")
            time.sleep(5)

    @staticmethod
    def executeGameLoop(field):
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b"q":
                return
            elif key == b"g":
                field.spawn_animal_anywhere("Keta")
            elif key == b"t":
                field.spawn_animal_anywhere("Shark")
            elif key == b"s":
                input("Simulation is paused. Press enter to resume...")
            elif key == b"e":
                FieldLoader.save(field)

        GameState.iterate()
        for i in range(0, field.height, 1):
            for j in range(0, field.width, 1):
                field.tiles[i][j].try_spawn_cycle(field)

        for i in GameState.getAnimalList():
            i.act(field)
            i.took_turn = False
            i.friend_cool_down -= 1
            i.take_damage(1, field)
