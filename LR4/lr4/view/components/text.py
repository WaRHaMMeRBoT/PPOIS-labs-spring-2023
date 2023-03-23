from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel


def weather_info(controller):
    layer = MDBoxLayout()
    weather = MDLabel(
        text="weather:" + controller.baseController.garden.model.weather.weather +
             " elapsed:" + str(controller.baseController.garden.model.weather.time),
        theme_text_color="Custom",
        text_color=(1, 1, 1, 1),
        font_style="H4")

    layer.add_widget(weather)
    layer.pos = (80, 425)
    return layer
