from kivymd.uix.anchorlayout import MDAnchorLayout

from gui.toolbar import tool_bar
from gui.table import table

from gui.show_general_info import show_info
from gui.add_new_plant import add_new_plant
from gui.actions import action_dialog

class View:
    def __init__(self, controller, app_object, garden) -> None:
        self.controller = controller
        self.garden = garden
        self.tool_bar = tool_bar(controller, app_object)
        self.table = table(controller)
        self.base_view = MDAnchorLayout(self.tool_bar, self.table)
        self.show_general_data = show_info(self.controller, garden)
        self.add_new_entity = add_new_plant(controller)
        self.action_window = action_dialog(controller)
        
    def update_table(self):
        self.base_view.remove_widget(self.table)
        self.table = table(self.controller)
        self.base_view.add_widget(self.table)

    def show_general_data_dialog(self):
        self.show_general_data = show_info(self.controller, self.garden)
        self.show_general_data.open()

    def close_general_info_dialog(self):
        self.show_general_data.dismiss()
    
    def add_new_dialog(self):
        self.add_new_entity.open()
    
    def launch_action_window(self):
        self.action_window.open()

        