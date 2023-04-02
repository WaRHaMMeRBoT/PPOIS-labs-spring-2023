import os

from kivy.metrics import dp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFloatingActionButton
from kivymd.uix.gridlayout import MDGridLayout

from lr4.garden.plants import Seed, Plant


def menu_buttons(controller):
    buttons = MDBoxLayout(spacing=20)

    warp_button = MDFloatingActionButton(
        icon=os.path.realpath(os.path.dirname(__file__)) + "/../assets/tardis.png",
        icon_size=dp(40),
        type="standard",
        theme_icon_color="Custom",
        elevation=0,
        md_bg_color="#fefbff",
        icon_color="#6851a5",
    )
    warp_button.bind(on_press=controller.warp_dialog)

    buttons.add_widget(
        warp_button
    )

    weather_button = MDFloatingActionButton(
        icon=os.path.realpath(os.path.dirname(__file__)) + "/../assets/weather.png",
        icon_size=dp(35),
        type="standard",
        theme_icon_color="Custom",
        elevation=0,
        md_bg_color="#fefbff",
        icon_color="#6851a5",
    )
    weather_button.bind(on_press=controller.weather_dialog)
    buttons.add_widget(
        weather_button
    )
    buttons.pos = (dp(600), dp(10))
    return buttons


def plants_buttons(controller):
    buttons = MDGridLayout(rows=5, cols=10, spacing=20)
    plants = controller.baseController.get_plants()

    index = 0
    for i in range(len(plants)):
        for j in range(len(plants[0])):
            if plants[i][j] is None:
                button = MDFloatingActionButton(
                    id=str(index),
                    icon="",
                    type="standard",
                    theme_icon_color="Custom",
                    elevation=0,
                    md_bg_color="#fefbff",
                    icon_color="#6851a5",
                )
                button.bind(on_press=controller.get_info_of_plant)
                buttons.add_widget(button)
                index += 1
            elif issubclass(plants[i][j].__class__, Plant):
                button = MDFloatingActionButton(
                    icon=os.path.realpath(os.path.dirname(__file__)) + "/../assets/" + plants[i][
                        j].name + ".png",
                    icon_size=dp(35),
                    id=str(index),
                    type="standard",
                    theme_icon_color="Custom",
                    elevation=0,
                    md_bg_color="#fefbff",
                    icon_color="#6851a5",
                )
                buttons.add_widget(button)
                button.bind(on_press=controller.get_info_of_plant)
                index += 1
            elif issubclass(plants[i][j].__class__, Seed):
                button = MDFloatingActionButton(
                    icon=os.path.realpath(os.path.dirname(__file__)) + "/../assets/seed.png",
                    icon_size=dp(35),
                    id=str(index),
                    type="standard",
                    theme_icon_color="Custom",
                    elevation=0,
                    md_bg_color="#fefbff",
                    icon_color="#6851a5",
                )
                buttons.add_widget(button)
                button.bind(on_press=controller.get_info_of_plant)
                index += 1
    buttons.pos = (dp(30), dp(-100))
    return buttons
