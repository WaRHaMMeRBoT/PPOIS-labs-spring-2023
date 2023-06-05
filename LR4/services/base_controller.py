from gameboard.utils import FileUtils
from gameboard.state import State
from gameboard.models import GameBoard


class BaseController:
    def __init__(self):
        data = FileUtils.read_from_json("state.json")
        self.game_board = State.get_game_board(data)

    def add(self, entity, x, y):
        self.game_board[x - 1][y - 1].put_entity(entity)
        FileUtils.save_in_json(self.game_board.to_dict(), "state.json")

    def create_new_game_board(self, size):
        self.game_board = GameBoard(size)
        FileUtils.save_in_json(self.game_board.to_dict(), "state.json")

    def view(self):
        self.game_board()

    def play(self):
        self.game_board.iteration()
        FileUtils.save_in_json(self.game_board.to_dict(), "state.json")

    def get_game_board(self):
        return self.game_board.get_game_board()
