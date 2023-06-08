from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDIconButton
from kivymd.uix.label import MDLabel

from wild_forest import Game

Activity = ''' 
#: import MDFlatButton kivymd.uix.button.MDFlatButton 

MDBoxLayout:

    MDScreenManager:
        id: sidebar
        size_hint: 0.25, 1

        MDScreen:
            name: 'buttons'

            MDStackLayout:
                md_bg_color: '#cccccc'
                padding: 8
                spacing: 8

                MDFlatButton:
                    md_bg_color: '#bbbbbb'
                    text: 'New Game'
                    size_hint_x: 1
                    on_press: root.ids.sidebar.current = 'modal_newgame'

                MDFlatButton:
                    md_bg_color: '#bbbbbb'
                    text: 'Save'
                    size_hint_x: 1
                    on_press: app.save()

                MDFlatButton:
                    md_bg_color: '#bbbbbb'
                    text: 'Load'
                    size_hint_x: 1
                    on_press: app.load()

                MDFlatButton:
                    md_bg_color: '#bbbbbb'
                    text: 'Skip day'
                    size_hint_x: 1
                    on_press: app.next()

                MDFlatButton:
                    md_bg_color: '#bbbbbb'
                    text: 'Spawn'
                    size_hint_x: 1
                    on_press: root.ids.sidebar.current = 'modal_spawn'

        MDScreen:
            name: 'modal_newgame'

            MDStackLayout:
                md_bg_color: '#cccccc'
                padding: 8
                spacing: 8

                MDLabel:
                    text: 'World size configuration'
                    size_hint: 1, 0.1

                MDTextField:
                    id: textfield_width
                    hint_text: 'Field width'
                    helper_text: 'Width of game world in blocks'
                    helper_text_mode: 'on_focus'

                MDTextField:
                    id: textfield_height
                    hint_text: 'Field height'
                    helper_text: 'Height of game world in blocks'
                    helper_text_mode: 'on_focus'

                MDFlatButton:
                    md_bg_color: '#bbbbbb'
                    text: 'Start'
                    size_hint_x: 1
                    on_press:
                        app.create_game(root.ids.textfield_height.text, root.ids.textfield_width.text) 
                        root.ids.sidebar.current = 'buttons'

        MDScreen:
            name: 'modal_spawn'

            MDStackLayout:
                md_bg_color: '#cccccc'
                padding: 8
                spacing: 8

                MDLabel:
                    text: 'Spawn manager'
                    size_hint: 1, 0.1

                MDTextField:
                    id : field_idf
                    hint_text: 'Entity id'
                    helper_text: 'Identifier of entity'
                    helper_text_mode: 'on_focus'

                MDTextField:
                    id : field_count
                    hint_text: 'Entity count'
                    helper_text: 'Count of entities to be spawned'
                    helper_text_mode: 'on_focus'

                MDFlatButton:
                    md_bg_color: '#bbbbbb'
                    text: 'Start'
                    size_hint_x: 1
                    on_press: 
                        app.spawn(root.ids.field_idf.text, root.ids.field_count.text) 
                        root.ids.sidebar.current = 'buttons'

    MDGridLayout:
        id: gamefield
        md_bg_color: '#444444'
        padding: 2
        spacing: 1

'''


class Program(MDApp):
    def __init__(self):
        super(Program, self).__init__()
        self.app = Builder.load_string(Activity)

        self.width = None
        self.height = None
        self.game = None
        self.tiles = {}

    def create_game(self, height, width):
        height, width = int(height), int(width)
        self.height, self.width = height, width
        self.app.ids.gamefield.cols = width
        self.app.ids.gamefield.rows = height
        self.game = Game(self.height, self.width)
        for i in range(self.width*self.height):
            tile = MDBoxLayout(
                    md_bg_color='black',
                    padding=2,
                    )
            self.tiles[i] = MDLabel(
                theme_text_color='Custom',
                text_color='white',
                halign='center',
                valign='center',
                id='label',
                text='B'
            )
            tile.add_widget(self.tiles[i])
            self.app.ids.gamefield.add_widget(tile)

    def next(self):
        if self.game:
            self.game.next()
            self.update_field()

    def save(self):
        if self.game:
            self.game.save('save')

    def load(self):
        if self.game:
            self.game.load('save')

    def spawn(self, idf, count):
        count = int(count)
        if self.game:
            idf_list = self.game.game_map.entity_dict.keys()
            if idf in idf_list:
                self.game.add_entity(idf, count)

    def update_field(self):
        if self.game:
            entities = self.game.game_map.entity_list
            mapper = self.game.game_map.icon_dict
            for i in range(self.width*self.height):
                self.tiles[i].text = ''
            for entity in entities:
                coords = entity.get_coords()
                print(coords.x, coords.y)
                i = coords.x + coords.y * self.width
                self.tiles[i].text = mapper[entity.get_idf()]

    def build(self):
        return self.app


if __name__ in ('__main__', '__android__'):
    Program().run()
