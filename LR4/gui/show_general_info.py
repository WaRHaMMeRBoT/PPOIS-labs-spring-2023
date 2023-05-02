from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

from gui.handle_dialog_button import close_general_info

def show_info(controller, garden):
    return MDDialog(
        text = f'Урожай: {", ".join([str(i[0])+":"+str(i[1]) for i in garden.garden.get_product.items()])}\n Погода: {garden.garden.weather.get_name}',
        buttons = [
            MDFlatButton(
                text="ОК",
                font_style = 'Button',
                font_size='17',
                on_release = close_general_info(controller)
            )
        ]
    )