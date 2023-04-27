from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton

class Bar:
    def __init__(self, controller) -> None:
        self._controller = controller

    def build_widget(self) -> MDBoxLayout:
        return MDBoxLayout(
            MDRaisedButton(
                text="Watering",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self.add_watering()
            ),
            MDRaisedButton(
                text="Drought",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self.add_drought()
            ),
            MDRaisedButton(
                text="Fertiliser",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self.add_fertiliser()
            ),
            MDRaisedButton(
                text="Weeding",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self.add_weeding()
            ),
            MDRaisedButton(
                text="Rain",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self.add_rain()
            ),
            MDRaisedButton(
                text="Disease",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self.add_disease()
            ),

            id="bar",
            size=(200, 100),
            size_hint=(1, None),
            spacing=10,
            padding=10
        )

    def add_watering(self) -> None:
        self._controller.open_add_watering()

    def add_drought(self) -> None:
        self._controller.open_add_drought()

    def add_fertiliser(self) -> None:
        self._controller.open_add_fertiliser()

    def add_weeding(self) -> None:
        self._controller.open_add_weeding()

    def add_rain(self) -> None:
        self._controller.open_add_rain()

    def add_disease(self) -> None:
        self._controller.open_add_disease()