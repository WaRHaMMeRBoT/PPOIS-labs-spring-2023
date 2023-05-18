import copy
import SimulationEngine
import kivy
import kivy.app
import kivy.uix.button
import kivy.uix.stacklayout
import kivy.uix.gridlayout
import kivy.uix.popup
import kivy.uix.textinput
import kivy.uix.label
import Classes
import Visualizer
import kivy.uix.checkbox


class MainMenu(kivy.uix.stacklayout.StackLayout, SimulationEngine.Engine):
    save_dialog = None
    load_dialog = None
    add_dialog = None
    text_for_load = None
    text_for_save = None
    text_for_add = [0, 0, 0, 0, 0, 0, 0]
    text_for_plant = [0, 0, 0, 0, 0]
    load_data = ''
    save_data = ''
    add_data = ''
    add_data_plant = ''
    add_data_specie = ''

    def load_fill(self):
        self.load_data = copy.deepcopy(self.text_for_load.text)

    def save_fill(self):
        self.save_data = copy.deepcopy(self.text_for_save.text)
        self.save(new_path=self.save_data)

    def add_fill(self):
        self.add_data = ''
        for substr in self.text_for_add:
            substr: kivy.uix.textinput
            self.add_data += substr.text + ' '
        self.add_data = self.add_data.removesuffix(' ')

    def plant_fill(self):
        self.add_data_plant = ''
        for text_field in self.text_for_plant:
            text_field: kivy.uix.textinput
            self.add_data_plant += text_field.text + ' '
        self.add_data_plant = self.add_data_plant.removesuffix(' ')

    def __init__(self, **kwargs):
        super(kivy.uix.stacklayout.StackLayout, self).__init__(**kwargs)
        super(SimulationEngine.Engine, self).__init__()
        super(MainMenu, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(kivy.uix.button.Button(text='Load', size_hint=(0.2, 0.1), color=(1, 1, 100, 1),
                                               background_color=(100, 1, 1, 0.2),
                                               on_press=lambda x: self.load_button_action()))
        self.add_widget(kivy.uix.button.Button(text='Save', size_hint=(0.2, 0.1), color=(100, 1, 100, 1),
                                               background_color=(100, 1, 1, 0.2),
                                               on_press=lambda x: self.save_button_action()))
        self.add_widget(kivy.uix.button.Button(text='Next turn', size_hint=(0.2, 0.1), color=(1, 1, 100, 1),
                                               background_color=(100, 1, 1, 0.2),
                                               on_press=lambda x: self.next_turn_button_action()))
        self.add_widget(kivy.uix.button.Button(text='Add creature', size_hint=(0.2, 0.1), color=(1, 1, 100, 1),
                                               background_color=(100, 1, 1, 0.2),
                                               on_press=lambda x: self.add_creature_button_action()))
        self.add_widget(kivy.uix.button.Button(text='Exit', size_hint=(0.2, 0.1), color=(1, 1, 100, 1),
                                               background_color=(100, 1, 1, 0.2), on_press=lambda x: exit()))
        self.game_field_layout = kivy.uix.gridlayout.GridLayout(cols=3, rows=3, size_hint=(1, 0.9), padding=[20, 20])
        for iteration in range(9):
            self.game_field_layout.add_widget(kivy.uix.button.Button(text=('Cell '+str(iteration)),
                                                                     color=(1, 1, 100, 1),
                                                                     background_color=(100, 1, 1, 0.2)))
        self.add_widget(self.game_field_layout)

    def save_dismiss(self):
        self.save_dialog.dismiss()

    def save_button_action(self):
        save_dialog_layout = kivy.uix.stacklayout.StackLayout(orientation='tb-rl')
        self.text_for_save = kivy.uix.textinput.TextInput(text='Write save file path', on_text=lambda x:
                                                          self.save_fill(), multiline=False, size_hint=(1.0, 0.8),
                                                          on_text_validate=lambda x: self.save_dismiss())
        save_dialog_layout.add_widget(self.text_for_save)
        save_dialog_layout.add_widget(kivy.uix.button.Button(text='Dismiss', size_hint=(0.2, 0.2),
                                                             on_press=lambda x: self.save_dialog.dismiss()))
        self.save_dialog = kivy.uix.popup.Popup(title='Save menu', auto_dismiss=False, content=save_dialog_layout)
        self.save_dialog.open()

    def load_dismiss(self):
        self.load_fill()
        self.load(new_path=self.load_data)
        self.load_dialog.dismiss()
        self.flip_screen()

    def load_button_action(self):
        load_dialog_layout = kivy.uix.stacklayout.StackLayout(orientation='tb-rl')
        self.text_for_load = kivy.uix.textinput.TextInput(text='Write save file path', size_hint=(1.0, 0.8),
                                                          on_text=lambda x: self.load_fill(), multiline=False,
                                                          on_text_validate=lambda x: self.load_dismiss())
        load_dialog_layout.add_widget(self.text_for_load)
        load_dialog_layout.add_widget(kivy.uix.button.Button(text='Dismiss', size_hint=(0.2, 0.2),
                                                             on_press=lambda x: self.load_dialog.dismiss()))
        self.load_dialog = kivy.uix.popup.Popup(title='Load menu',  auto_dismiss=False, content=load_dialog_layout)
        self.load_dialog.open()

    def flip_screen(self):
        output_table = Visualizer.visualizer(self.current_field)
        self.current_field: Classes.Field
        self.remove_widget(self.game_field_layout)
        self.game_field_layout.clear_widgets()
        for column in output_table:
            for row in column:
                temp_cell_container = ''
                for creature in row:
                    temp_cell_container+=creature+',\n'
                temp_cell_container = temp_cell_container.removesuffix(',')
                self.game_field_layout.add_widget(kivy.uix.button.Button(text=temp_cell_container, disabled=False,
                                                                         color=(1, 1, 100, 1),
                                                                         background_color=(100, 1, 1, 0.2)))
        self.add_widget(self.game_field_layout)

    def add_dialog_dismiss(self):
        self.plant_fill()
        self.add_fill()
        if self.add_data != 'Specie name satiety age body size coordinates gender':
            self.add_creature(self.text_for_add[0].text,
                              creature_stats_animal=self.add_data.removeprefix(self.text_for_add[0].text + ' '))
        if not copy.deepcopy(self.add_data_plant) == 'Specie name age size coordinates':
            self.add_creature(self.text_for_plant[0].text,
                              creature_stats_plant=self.add_data_plant.removeprefix(self.text_for_plant[0].text
                                                                                    + ' '))
        self.flip_screen()
        self.add_dialog.dismiss()

    def add_creature_button_action(self):
        pop_up_layout = kivy.uix.stacklayout.StackLayout(orientation='tb-lr')
        self.text_for_add[0] = kivy.uix.textinput.TextInput(text='Specie', size_hint=(0.5, 0.1),
                                                            hint_text_color=(1, 1, 100, 1),
                                                            background_color=(100, 1, 1, 1),
                                                            on_text_validate=lambda x: self.add_fll())
        pop_up_layout.add_widget(kivy.uix.label.Label(text='Animal', size_hint=(0.1, 0.3)))
        self.text_for_add[1] = kivy.uix.textinput.TextInput(text='name', size_hint=(0.5, 0.1),
                                                            background_color=(100, 1, 1, 1),
                                                            on_text_validate=lambda x: self.add_fll())
        self.text_for_add[2] = kivy.uix.textinput.TextInput(text='satiety', size_hint=(0.5, 0.1),
                                                            background_color=(100, 1, 1, 1),
                                                            on_text_validate=lambda x: self.add_fll())
        self.text_for_add[3] = kivy.uix.textinput.TextInput(text='age', size_hint=(0.5, 0.1),
                                                            background_color=(100, 1, 1, 1),
                                                            on_text_validate=lambda x: self.add_fill())
        self.text_for_add[4] = kivy.uix.textinput.TextInput(text='body size', size_hint=(0.5, 0.1),
                                                            background_color=(100, 1, 1, 1),
                                                            on_text_validate=lambda x: self.add_fill())
        self.text_for_add[5] = kivy.uix.textinput.TextInput(text='coordinates', size_hint=(0.5, 0.1),
                                                            background_color=(100, 1, 1, 1),
                                                            on_text_validate=lambda x: self.add_fill())
        self.text_for_add[6] = kivy.uix.textinput.TextInput(text='gender', size_hint=(0.5, 0.1),
                                                            background_color=(100, 1, 1, 1),
                                                            on_text_validate=lambda x: self.add_fill())
        for text_field in self.text_for_add:
            pop_up_layout.add_widget(text_field)
        pop_up_layout.add_widget(kivy.uix.label.Label(text='Plant', size_hint=(0.1, 0.1)))
        self.text_for_plant[0] = kivy.uix.textinput.TextInput(text='Specie', size_hint=(0.5, 0.1),
                                                              background_color=(100, 1, 1, 1),
                                                              on_text_validate=lambda x: self.plant_fill())
        self.text_for_plant[1] = kivy.uix.textinput.TextInput(text='name', size_hint=(0.5, 0.1),
                                                              background_color=(100, 1, 1, 1),
                                                              on_text_validate=lambda x: self.plant_fill())
        self.text_for_plant[2] = kivy.uix.textinput.TextInput(text='age', size_hint=(0.5, 0.1),
                                                              background_color=(100, 1, 1, 1),
                                                              on_text_validate=lambda x: self.plant_fill())
        self.text_for_plant[3] = kivy.uix.textinput.TextInput(text='size', size_hint=(0.5, 0.1),
                                                              background_color=(100, 1, 1, 1),
                                                              on_text_validate=lambda x: self.plant_fill())
        self.text_for_plant[4] = kivy.uix.textinput.TextInput(text='coordinates', size_hint=(0.5, 0.1),
                                                              background_color=(100, 1, 1, 1),
                                                              on_text_validate=lambda x: self.plant_fill())
        for text_input in self.text_for_plant:
            pop_up_layout.add_widget(text_input)
        pop_up_layout.add_widget(kivy.uix.button.Button(text='Add', size_hint=(0.2, 0.2),
                                                        on_press=lambda x: self.add_dialog_dismiss()))
        pop_up_layout.add_widget(kivy.uix.button.Button(text='Dismiss', size_hint=(0.2, 0.2),
                                                        on_press=lambda x: self.add_dialog.dismiss()))
        self.add_dialog = kivy.uix.popup.Popup(title='Add menu', auto_dismiss=False, content=pop_up_layout,
                                               background_color=(1, 0, 0, 1))
        self.add_dialog.open()

    def next_turn_button_action(self):
        self.next_turn()
        self.flip_screen()


class SimulationVisual(kivy.app.App):
    def build(self):
        return MainMenu()
