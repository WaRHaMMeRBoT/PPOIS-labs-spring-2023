from io import StringIO
import pickle
import sys
import threading
from classes.impl import Garden, Seed, Watering, Weed
import gui
from PyQt5.QtWidgets import QApplication


class GUI(threading.Thread):
    def __init__(self, buffer) -> None:
        super().__init__()
        self.__buffer = buffer

    def run(self) -> None:
        global garden_representation
        app = QApplication(sys.argv)
        win = gui.MainWindow(garden_representation, self.__buffer)
        win.show()
        sys.exit(app.exec_())


class Reader(threading.Thread):
    def run(self):
        global garden_representation
        try:
            with open("store.pickle", "rb") as f:
                garden_representation = pickle.load(f)
                garden_representation.is_saved = True
        except FileNotFoundError:
            garden_representation.new_bed()
            garden_representation.is_saved = False
        garden_representation.exist()


class Writer(threading.Thread):
    def run(self):
        global garden_representation

        while True:
            choice = input()
            if choice == "sd":
                garden_representation.new_seed()
            elif choice == "tr":
                garden_representation.new_fruit_tree()
            elif choice == "fl":
                garden_representation.fertile_garden()
            elif choice == "cr":
                garden_representation.love_garden()
            elif choice == "wt":
                watering = Watering()
                watering.pour_bed(garden_representation.bed)
            elif choice == "wd":
                garden_representation.weeding_garden()
            elif choice == "rt":
                for tree in garden_representation.trees:
                    if tree is None:
                        continue
                    garden_representation.get_trees().remove(tree)
                    break
            elif choice == "rs":
                for plant in garden_representation.bed.place:
                    if plant is None:
                        continue
                    if isinstance(plant, Seed):
                        garden_representation.bed.remove_from_bed(plant)
                        break
            elif choice == "rv":
                for plant in garden_representation.bed.place:
                    if plant is None:
                        continue
                    if not isinstance(plant, (Weed, Seed)):
                        garden_representation.bed.remove_from_bed(plant)
                        break
            elif choice == "rw":
                for plant in garden_representation.bed.place:
                    if plant is None:
                        continue
                    if isinstance(plant, Weed):
                        garden_representation.bed.remove_from_bed(plant)
                        break
            elif choice == "ex":
                with open("store.pickle", "wb") as f:
                    pickle.dump(garden_representation, f)
                garden_representation.is_on = False
                garden_representation.is_saved = True
                sys.exit()


garden_representation = Garden()

var = input("Choose the interface: CLI or GUI\n")

if var == "CLI":
    reader = Reader()
    writer = Writer()

    reader.start()
    writer.start()

    reader.join()
    writer.join()

if var == "GUI":
    gui_buffer = StringIO()
    sys.stdout = gui_buffer

    reader = Reader()
    gui_thread = GUI(gui_buffer)

    reader.start()
    gui_thread.start()

    reader.join()
    gui_thread.join()