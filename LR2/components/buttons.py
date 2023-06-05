from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFloatingActionButton


def edit_menu_button_layout(controller) -> MDBoxLayout:
    remove_button = MDFloatingActionButton(
        icon="delete-forever",
        type="small",
        theme_icon_color="Custom",
        md_bg_color="#EAF4EF",
        elevation=0,
        icon_color="#4DC0A5",
        pos_hint={"center_x": 0.07, "center_y": .06}
    )
    remove_button.bind(on_press=controller.delete_selected_rows)

    cancel_button = MDFloatingActionButton(
        icon="close-octagon",
        type="small",
        theme_icon_color="Custom",
        elevation=0,
        md_bg_color="#EAF4EF",
        icon_color="#4DC0A5",
        pos_hint={"center_x": 0.07, "center_y": .06}
    )
    cancel_button.bind(on_press=controller.transition_to_menu)

    buttons = MDBoxLayout(spacing=20)
    buttons.add_widget(remove_button)
    buttons.add_widget(cancel_button)
    return buttons


def main_menu_buttons(controller) -> MDBoxLayout:
    edit_button = MDFloatingActionButton(
        icon="pencil",
        type="small",
        theme_icon_color="Custom",
        elevation=0,
        md_bg_color="#EAF4EF",
        icon_color="#4DC0A5",
        pos_hint={"center_x": 0.07, "center_y": .06},
    )
    edit_button.bind(on_press=controller.transition_to_deleting)

    find_button = MDFloatingActionButton(
        icon="magnify",
        type="small",
        theme_icon_color="Custom",
        md_bg_color="#EAF4EF",
        icon_color="#4DC0A5",
        pos_hint={"center_x": 0.13, "center_y": .06}
    )
    find_button.bind(on_press=controller.find_dialog)

    add_button = MDFloatingActionButton(
        icon="plus",
        type="small",
        theme_icon_color="Custom",
        elevation=0,
        md_bg_color="#EAF4EF",
        icon_color="#4DC0A5",
        pos_hint={"center_x": 0.19, "center_y": .06}
    )
    add_button.bind(on_press=controller.add_dialog)

    save_button = MDFloatingActionButton(
        icon="content-save",
        type="small",
        theme_icon_color="Custom",
        elevation=0,
        md_bg_color="#EAF4EF",
        icon_color="#4DC0A5",
        pos_hint={"center_x": 0.25, "center_y": .06}
    )
    save_button.bind(on_press=controller.save)
    buttons = MDBoxLayout(spacing=20)

    buttons.add_widget(add_button)
    buttons.add_widget(find_button)
    buttons.add_widget(edit_button)
    buttons.add_widget(save_button)
    return buttons


def marks_button_layout(controller) -> MDBoxLayout:
    buttons = MDBoxLayout(spacing=20)

    back_button = MDFloatingActionButton(
        icon="keyboard-backspace",
        type="small",
        theme_icon_color="Custom",
        md_bg_color="#EAF4EF",
        icon_color="#4DC0A5",
        pos_hint={"center_x": 0.07, "center_y": .06}
    )
    back_button.bind(on_press=controller.transition_to_menu)

    edit_button = MDFloatingActionButton(
        icon="pencil",
        type="small",
        theme_icon_color="Custom",
        elevation=0,
        md_bg_color="#EAF4EF",
        icon_color="#4DC0A5",
        pos_hint={"center_x": 0.13, "center_y": .06},
    )
    edit_button.bind(on_press=controller.transition_to_deleting)

    buttons.add_widget(back_button)
    buttons.add_widget(edit_button)
    return buttons
