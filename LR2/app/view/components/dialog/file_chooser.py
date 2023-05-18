import os
import sys

from kivymd.uix.filemanager import MDFileManager

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from app.services.action import Action


def confirm_choose_file(controller):
    def confirm(event):
        controller.dispatch(Action(type_='FILE_CHOOSE', content=event))

    return confirm


def deny_choose_file(controller):
    def deny(event):
        controller.dispatch(Action(type_='CLOSE_CHOOSE_FILE_DIALOG'))

    return deny


def choose_file_dialog(props):

    return MDFileManager(
        exit_manager=deny_choose_file(props['controller']),
        select_path=confirm_choose_file(props['controller']),
    )
