import sys
import os
from datetime import datetime

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDDatePicker

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from app.services.action import Action


def confirm_filter(controller):
    def confirm(event):
        controller.dispatch(Action(type_='FILTER'))

    return confirm


def disable_filter(controller):
    def confirm(event):
        controller.dispatch(Action(type_='DISABLE_FILTER'))

    return confirm


def deny_filter(controller):
    def deny(event):
        controller.dispatch(Action(type_='CLOSE_DIALOG'))

    return deny


KV = '''



<Content>
    id: content
    orientation: "vertical"
    padding_y: 10

    spacing: "12dp"
    size_hint_y: None
    height: "420dp"

    MDTextField:
        id: tour_name
        hint_text: "Tournament name"
        helper_text: "Enter the name of the tournament"
        helper_text_mode: "on_error"

    MDTextField:
        id: date
        hint_text: "Date"
        icon_right: "calendar"
        on_focus: if self.focus: root.show_date_picker()
    
    MDTextField:
        id: sport
        hint_text: "sport"
        icon_right: "Enter the name of the sport"
        helper_text_mode: "on_error"

    MDTextField:
        id: name
        hint_text: "Full name of the athlete"
        helper_text: "Enter enter the name of the athlete"
        helper_text_mode: "on_error"
    
    MDBoxLayout:
        id: reward
        hint_text: "Prize fund"
        helper_text: "Min should be less then Max"
        helper_text_mode: "on_error"
        adaptive_height: True
        spacing: "12dp"
        
        MDTextField:
            id: min_reward
            hint_text: "Min Prize fund"
            helper_text: "Enter an integer, or a fractional number separated by a dot"
            helper_text_mode: "on_error"
            
        MDTextField:
            id: max_reward
            hint_text: "Max Prize fund"
            helper_text: "Enter an integer, or a fractional number separated by a dot"
            helper_text_mode: "on_error"
            
    MDBoxLayout:
        id: winner_reward
        hint_text: "Winner reward"
        helper_text: "Min should be less or equal then Max"
        helper_text_mode: "on_error"
        adaptive_height: True
        spacing: "10dp"
        
        MDTextField:
            id: min_winner_reward
            hint_text: "Min Winner Prize fund"
            helper_text: "Enter an integer, or a fractional number separated by a dot"
            helper_text_mode: "on_error"
            
        MDTextField:
            id: max_winner_reward
            hint_text: "Max Winner Prize fund"
            helper_text: "Enter an integer, or a fractional number separated by a dot"
            helper_text_mode: "on_error"

'''


class Content(BoxLayout):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.dialog = None

    def on_save(self, instance, value, date):
        self.ids.date.text = value.strftime("%d.%m.%Y")

    def show_date_picker(self):
        date = datetime.strptime(self.ids.date.text, '%d.%m.%Y') if self.ids.date.text != '' else datetime.now()
        date_dialog = MDDatePicker(day=date.day, month=date.month, year=date.year)
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()


def filter_dialog(props):
    Builder.load_string(KV)
    dialog = MDDialog(
        title="Filter:",
        type="custom",
        content_cls=Content(),
        buttons=[
            MDFlatButton(
                text="DISABLE",
                theme_text_color="Custom",
                on_release=disable_filter(props['controller'])
            ),
            MDFlatButton(
                text="CANCEL",
                theme_text_color="Custom",
                on_release=deny_filter(props['controller'])
            ),
            MDFlatButton(
                text="SEARCH",
                theme_text_color="Custom",
                on_release=confirm_filter(props['controller'])
            ),
        ],
    )
    return dialog
