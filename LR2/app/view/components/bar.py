import sys
import os

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from app.services.action import Action


def adding_competition(controller):
    def callback(x):
        controller.dispatch(Action(type_='OPEN_ADDING_DIALOG'))

    return callback


def remove_competition(controller):
    def callback(widget):
        controller.dispatch(Action(type_='REMOVE', content=widget))

    return callback


def filter_table(controller):
    def callback(widget):
        controller.dispatch(Action(type_='OPEN_FILTER_DIALOG', content=widget))

    return callback


def choose_file(controller):
    def callback(widget):
        controller.dispatch(Action(type_='OPEN_CHOOSE_FILE_DIALOG', content=widget))

    return callback


def bar(props):
    print("BAR:", props)
    return MDBoxLayout(
        MDRaisedButton(
            text='Add',
            size_hint=(1, 1),
            elevation=0,
            on_press=adding_competition(props['controller'])

        ),
        MDRaisedButton(
            text='Filter',
            size_hint=(1, 1),
            elevation=0,
            on_press=filter_table(props['controller'])
        ),
        MDRaisedButton(
            text='Remove',
            size_hint=(1, 1),
            elevation=0,
            on_press=remove_competition(props['controller'])
        ),
        MDRaisedButton(
            text='Choose File',
            size_hint=(1, 1),
            elevation=0,
            on_press=choose_file(props['controller'])
        ),
        id='bar',
        size=(200, 100),
        size_hint=(1, None),
        spacing=10,
        padding=10,
    )
