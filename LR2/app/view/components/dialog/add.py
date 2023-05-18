import sys
import os

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.pickers import MDDatePicker

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from app.services.action import Action


def confirm_adding(controller):
    def confirm(event):
        controller.dispatch(Action(type_='ADD'))

    return confirm


def deny_adding(controller):
    def deny(event):
        controller.dispatch(Action(type_='CLOSE_DIALOG'))

    return deny


KV = '''
       
<Content>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "350dp"
    
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
        hint_text: "Name of sport"
        helper_text: "Enter the name of the sport"
        helper_text_mode: "on_error"
        
        
    MDTextField:
        id: name
        hint_text: "Full name of the athlete"
        helper_text: "Enter enter the name of the athlete"
        helper_text_mode: "on_error"
        
    MDTextField:
        id: reward
        hint_text: "Prize fund"
        helper_text: "Enter an integer, or a fractional number separated by a dot"
        helper_text_mode: "on_error"

'''


class Content(BoxLayout):

    def on_save(self, instance, value, date):
        self.ids.date.text = value.strftime("%d.%m.%Y")

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save)
        date_dialog.open()


def adding_dialog(props):
    Builder.load_string(KV)
    dialog = MDDialog(
        title="Add:",
        type="custom",
        content_cls=Content(),
        buttons=[
            MDFlatButton(
                text="CANCEL",
                theme_text_color="Custom",
                on_release=deny_adding(props['controller'])
            ),
            MDFlatButton(
                text="ADD",
                theme_text_color="Custom",
                on_release=confirm_adding(props['controller'])
            ),
        ],
    )
    return dialog
