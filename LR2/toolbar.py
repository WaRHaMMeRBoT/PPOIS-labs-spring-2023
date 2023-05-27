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
                    pos_hint = {'center_x':0.4,'center_y':0.967},
                    padding = [100,10],
                    font_style = 'Button',
                    on_press = add_new_line_in_table(controller_object)
                ),
                MDTextButton(
                    text = 'Удалить запись',
                    pos_hint = {'right':10, 'center_y':0.967},
                    padding = [100,10],
                    #md_bg_color = 'yellow',
                    font_style = 'Button',
                    on_press = delete_row_from_table(controller_object)
                ),
                MDTextButton(
                    text = 'Найти запись',
                    pos_hint = {'center_x':.6, 'center_y':0.967},
                    padding = [100,10],
                    font_style = 'Button',
                    on_press = filter_student(controller_object)
                ),
            ),
    )