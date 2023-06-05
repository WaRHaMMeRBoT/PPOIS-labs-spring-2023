from .models import *


class State:
    @staticmethod
    def get_game_board(data: dict) -> GameBoard:
        cells = State.get_cells(data["board"])
        length = data["length"]

        game = GameBoard(length)
        game.set_board(cells)

        return game

    @staticmethod
    def get_cells(data: list) -> list:
        cells = []

        for row in data:
            cells_row = []
            for raw_cell in row:
                c = State.get_cell(raw_cell)
                cells_row.append(c)
            cells.append(cells_row)

        return cells

    @staticmethod
    def get_cell(data: dict) -> Cell:
        herbivore = []
        predator = []
        plant = None
        for item in ("herbivore", "predator"):
            for el in data[item]:
                args = {k: v for k, v in el.items() if k != "name"}
                if el["name"] == "Wolf":
                    herbivore.append(Wolf(**args))
                if el["name"] == "Rabbit":
                    predator.append(Rabbit(**args))
        if data["plant"]:
            plant = Plant(data["plant"]["age"], data["plant"]["size"])
        cell = Cell(herbivore, predator, plant)
        return cell


