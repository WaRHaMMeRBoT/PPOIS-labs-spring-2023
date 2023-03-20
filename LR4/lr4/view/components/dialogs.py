from kivy.metrics import dp
from kivy.properties import NumericProperty
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from kivymd.uix.list import OneLineAvatarIconListItem, CheckboxLeftWidget
from kivymd.uix.slider import MDSlider
from kivymd.uix.textfield import MDTextField

from lr4.garden.plants import Plant


def add_seed_dialog(controller):
    dialog = MDDialog(
        title="not implimented ground:",
        type="custom",

        content_cls=MDBoxLayout(
            MDTextField(
                id="name",
                hint_text="Name",
                required=True,
                helper_text_mode="on_error",
                helper_text="Enter text"
            ),
            height=dp(100),
            size_hint_y=None,
            orientation='vertical',
            spacing=20

        ),

        buttons=[
            MDFlatButton(
                text="CANCEL",
                theme_text_color="Custom",
                on_release=controller.close_dialog,
            ),
            MDFlatButton(
                text="OK",
                theme_text_color="Custom",
                on_release=controller.add_seed
            )
        ],
    )
    dialog.height = dp(40)
    dialog.width = dp(600)
    return dialog


def get_info_about_plant(controller):
    plant = controller.baseController.get_plants()[controller.index_and_row[0]][controller.index_and_row[1]]
    layout = MDBoxLayout(orientation='vertical', spacing=20)
    layout.add_widget(
        MDSlider(min=0, max=100, value=plant.health, hint=True, color="green",
                 thumb_color_inactive="green", track_color_inactive="red"))
    layout.height = dp(100)
    layout.size_hint_y = None
    if issubclass(plant.__class__, Plant):
        layout.add_widget(MDLabel(text="length:" + str(plant.length)))
    layout.add_widget(MDLabel(text="time:" + str(plant.time)))
    dialog = MDDialog(
        title=plant.name,
        type="custom",
        content_cls=layout,
        buttons=[
            MDFlatButton(
                text="Remove",
                theme_text_color="Custom",
                text_color="red",
                on_release=controller.remove_plant,
            ),
            MDFlatButton(
                text="Cancel",
                theme_text_color="Custom",
                on_release=controller.close_dialog,
            )
        ],
    )
    dialog.height = dp(40)
    dialog.width = dp(600)
    return dialog


class CustomDialog(MDBoxLayout):
    value = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = "10dp"
        self.spacing = "10dp"
        self.slider = MDSlider(min=0, max=100, value=50, hint=True, hint_bg_color="red", hint_text_color="white")
        self.slider.bind(value=self.on_value_change)
        self.add_widget(self.slider)
        self.size_hint_y = None

    def on_value_change(self, instance, value):
        self.value = value


def warp_dialog(controller):
    dialog = MDDialog(
        title="Warp:",
        type="custom",

        content_cls=CustomDialog(),

        buttons=[
            MDFlatButton(
                text="CANCEL",
                theme_text_color="Custom",
                on_release=controller.close_dialog,
            ),
            MDFlatButton(
                text="OK",
                theme_text_color="Custom",
                on_release=controller.warp
            )
        ],
    )
    dialog.height = dp(40)
    dialog.width = dp(600)
    return dialog


class ItemConfirm(OneLineAvatarIconListItem):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.checkbox = CheckboxLeftWidget(group="items")
        self.add_widget(self.checkbox)

    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.checkbox.active = not self.checkbox.active


def weather_dialog(controller):
    clear = ItemConfirm(text="clear")
    clear.checkbox.active = True
    dialog = MDDialog(
        title="Weather changer",
        type="confirmation",
        items=[
            ItemConfirm(text="sunny"),
            ItemConfirm(text="rainy"),
            ItemConfirm(text="drought"),
            clear
        ],
        buttons=[
            MDFlatButton(
                text="CANCEL",
                theme_text_color="Custom"
            ),
            MDFlatButton(
                text="OK",
                theme_text_color="Custom",
                on_release=controller.change_weather
            ),
        ],
    )
    return dialog
