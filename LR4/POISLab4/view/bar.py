from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton


class Bar:
    def __init__(self, controller) -> None:
        self._controller = controller

    def build_widget(self) -> MDBoxLayout:
        return MDBoxLayout(
            MDRaisedButton(
                text="Add new item",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self.add_entity()
            ),
            MDRaisedButton(
                text="Create new field",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self.warp()
            ),
            MDRaisedButton(
                text="Make a move",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self.play()
            ),

            id="bar",
            size=(200, 100),
            size_hint=(1, None),
            spacing=10,
            padding=10
        )

    def add_entity(self) -> None:
        self._controller.open_add_dialog()

    def warp(self) -> None:
        self._controller.open_warp_dialog()

    def play(self) -> None:
        self._controller.play()