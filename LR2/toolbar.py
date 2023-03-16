from kivymd.uix.button import MDTextButton, MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

def add_new_line_in_table(controller_object):
    def callback(*args):
        controller_object.open_add_window()
    return callback

def filter_student(controller_object):
    def callback(*args):
        controller_object.filter_students()
    return callback

def delete_row_from_table(controller_object):
    def callback(*args):
        controller_object.confirm_delete()
    return callback

def tool_bar(controller_object: object, app_object: object):
    return MDScreen(
            MDBoxLayout(
                MDTextButton(
                    text = 'Добавить запись',
                    pos_hint = {'center_x':0.1 ,'center_y':0.95},
                    padding = [28,10],
                    font_style = 'Button',
                    on_press = add_new_line_in_table(controller_object)
                ),
                MDTextButton(
                    text = 'Удалить запись',
                    pos_hint = {'center_x':0.3, 'center_y':0.95},
                    padding = [28,10],
                    font_style = 'Button',
                    on_press = delete_row_from_table(controller_object)
                ),
                MDTextButton(
                    text = 'Найти запись',
                    pos_hint = {'center_x':0.5, 'center_y':0.95},
                    padding = [28,10],
                    font_style = 'Button',
                    on_press = filter_student(controller_object)
                ),
            ),
            MDIconButton(
                icon = 'white-balance-sunny',
                on_release = app_object.switch_theme_style,
                pos_hint = {'center_y':0.95, 'center_x':0.95},
                padding = [10, 10],
            ),
    )