from Field import Field
from FieldLoader import FieldLoader
from View import View
from GameState import GameState
import msvcrt
import time

class Simulation:
    @staticmethod
    def start(field: Field, iterationsToSkip: int):
        try:
            while iterationsToSkip > 0:
                Simulation.executeGameLoop(field)
                iterationsToSkip -= 1
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
            if key == b'q':
                return
            elif key == b'g':
                field.spawnAnimalAnywhere("Gazelle")
            elif key == b't':
                field.spawnAnimalAnywhere("Tiger")
            elif key == b's':
                input("Simulation is paused. Press enter to resume...")
            elif key == b'e':
                FieldLoader.save(field)

        GameState.iterate()
        for i in range(0, field.height, 1):
            for j in range(0, field.width, 1):
                field.tiles[i][j].trySpawnCycle(field)

        for i in GameState.getAnimalList():
            i.act(field)
            i.tookTurn = False
            i.mateCooldown -= 1
            i.takeDamage(1, field)
