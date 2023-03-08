from lr2.controllers.controller import Controller


class MarksController(Controller):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def print(self):
        print("хаю хай")
