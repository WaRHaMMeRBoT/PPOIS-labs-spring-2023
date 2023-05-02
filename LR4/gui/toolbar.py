from kivymd.uix.button import MDTextButton, MDIconButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen

def add_new_garden_bed(controller_object):
    def callback(*args):
        controller_object.add_new_garden_bed()
    return callback

def show_garden_general_data(controller_object):
    def callback(*args):
        controller_object.show_garden_general_data()
    return callback

def next_step(controller_object):
    def callback(*args):
        controller_object.next_garden_step()
    return callback

def take_harvest(controller_object):
    def callback(*args):
        controller_object.take_garden_harvest()
    return callback

def add_new_entity(controller_object):
    def callback(*args):
        controller_object.add_new_plant()
    return callback

def action_window(controller_object):
    def callback(*args):
        controller_object.open_action_window()
    return callback

def tool_bar(controller_object: object, app_object: object):
    return MDScreen(
            MDBoxLayout(
                MDTextButton(
                    text = 'Добавить грядку',
                    pos_hint = {'center_x':0.1 ,'center_y':0.965},
                    padding = [28,10],
                    font_style = 'Button',
                    on_press = add_new_garden_bed(controller_object)
                ),
                MDTextButton(
                    text = 'Общая информация',
                    pos_hint = {'center_x':0.3, 'center_y':0.965},
                    padding = [28,10],
                    font_style = 'Button',
                    on_press = show_garden_general_data(controller_object)
                ),
                MDTextButton(
                    text = 'Далее',
                    pos_hint = {'center_x':0.5, 'center_y':0.965},
                    padding = [28,10],
                    font_style = 'Button',
                    on_press = next_step(controller_object)
                ),
                MDTextButton(
                    text = 'Посадить',
                    pos_hint = {'center_x':0.5, 'center_y':0.965},
                    padding = [28,10],
                    font_style = 'Button',
                    on_press = add_new_entity(controller_object)
                ),
                MDTextButton(
                    text = 'Действия',
                    pos_hint = {'center_x':0.5, 'center_y':0.965},
                    padding = [28,10],
                    font_style = 'Button',
                    on_press = action_window(controller_object)
                ),
                MDTextButton(
                    text = 'Собрать урожай',
                    pos_hint = {'center_x':0.5, 'center_y':0.965},
                    padding = [28,10],
                    font_style = 'Button',
                    on_press = take_harvest(controller_object)
                ),
            ),
    )