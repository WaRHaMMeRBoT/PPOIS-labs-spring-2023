from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.config import Config
from kivy.core.window import Window

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "1000")
Config.set("graphics", "height", "700")

Window.clearcolor = (.61, .87, .95, 1)

class Garden(MDApp):
    def __init__(self, model, controller):
        super().__init__()
        self.controller = controller
        self.controller.setView(self)
        self.model = model
        self.money = 99

    def exit(self):
        self.stop()

    def build(self):
        root = Builder.load_file('lib.kv')
        return root

    def clear_label(self):
        x = self.root.ids.display_data_screen.ids.gl_2
        x.clear_widgets()

    def update_data(self):
        self.root.ids.main_screen.ids.weather.text = "Погода: " + str(self.model.get_weather())
        self.root.ids.main_screen.ids.tree_kol.text = "Кол-во деревьев: " + str(self.model.tree_kol())
        self.root.ids.main_screen.ids.money.text = "Деньги: " + str(self.model.money())
        self.root.ids.main_screen.ids.garden_bed_kol.text = "Кол-во грядок: " + str(self.model.garden_bed_kol())
        self.root.ids.main_screen.ids.day.text = "День: " + str(self.model.day())
        self.show_data()

    def show_data(self):
        st = self.model.show()
        lst = st.split('|')
        lst_new = []
        for i in range(len(lst)):
            if lst[i].find('===') == -1 and lst[i].find("----") == -1:
                lst_new.append(lst[i])

        cell = [self.root.ids.main_screen.ids.cell_1,
                self.root.ids.main_screen.ids.cell_2,
                self.root.ids.main_screen.ids.cell_3,
                self.root.ids.main_screen.ids.cell_4,
                self.root.ids.main_screen.ids.cell_5,
                self.root.ids.main_screen.ids.cell_6,
                self.root.ids.main_screen.ids.cell_7]

        tree = [self.root.ids.main_screen.ids.tree_1,
                self.root.ids.main_screen.ids.tree_2,
                self.root.ids.main_screen.ids.tree_3,
                self.root.ids.main_screen.ids.tree_4,
                self.root.ids.main_screen.ids.tree_5]

        for i in tree:
            i.background_normal = 'pictures/lol.png'
            i.background_color = 1, 1, 1, 1

        for i in range(len(lst_new)):
            if lst_new[i].find('Garden bed') != -1:
                st = lst_new[i].split()
                num = int(st[2])
                error = False
                if lst_new[i + 1] == 'tomato':
                    cell[num-1].background_normal = 'pictures/tomato.png'
                    cell[num-1].background_color = 1, 1, 1, 1
                elif lst_new[i + 1] == 'potato':
                    cell[num-1].background_normal = 'pictures/potato.png'
                    cell[num-1].background_color = 1, 1, 1, 1
                elif lst_new[i + 1] == 'pepper':
                    cell[num-1].background_normal = 'pictures/pepper.png'
                    cell[num-1].background_color = 1, 1, 1, 1
                else:
                    cell[num-1].background_color = .81, .76, .07, 1
                    cell[num-1].background_normal = ''
                    cell[num-1].text = '1'
                    error = True
                    if lst_new[i + 2] == 'Weed+':
                        cell[num-1].background_normal = 'pictures/weed.png'
                        cell[num-1].background_color = 1, 1, 1, 1

                if not error:
                    if lst_new[i + 2] == 'Ill+':
                        cell[num-1].background_color = 0, 1, 0, 1

                    if lst_new[i + 3] == 'Pest+':
                        cell[num-1].background_color = 0, 0, 0, 1

                    if lst_new[num + 4] == 'Harvest+':
                        if lst_new[num + 1] == 'tomato':
                            cell[num-1].background_normal = 'pictures/tomato_harvest.png'

                        elif lst_new[i + 1] == 'potato':
                            cell[num-1].background_normal = 'pictures/potato_harvest.png'

                        elif lst_new[i + 1] == 'pepper':
                            cell[num-1].background_normal = 'pictures/pepper_harvest.png'

                    if lst_new[i + 7] == 'Weed+':
                        cell[num-1].background_normal = 'pictures/weed.png'
                        cell[num-1].background_color = 1, 1, 1, 1

            if lst_new[i].find('Tree') != -1:
                st = lst_new[i].split()
                num = int(st[1])
                if lst_new[i + 1] == 'apple':
                    tree[num-1].background_normal = 'pictures/apple_little.png'
                    tree[num-1].background_color = 1, 1, 1, 1
                elif lst_new[i + 1] == 'peer':
                    tree[num-1].background_normal = 'pictures/peer_little.png'
                    tree[num-1].background_color = 1, 1, 1, 1
                else:
                    tree[num-1].background_normal = 'pictures/lol.png'
                    tree[num-1].background_color = 1, 1, 1, 1

                if lst_new[i + 2] == 'Ill+':
                    tree[num-1].background_color = 0, 1, 0, 1

                if lst_new[i + 3] == 'Pest+':
                    tree[num-1].background_color = 0, 0, 0, 1

                if lst_new[i + 4] == 'Harvest+':
                    if lst_new[i + 1] == 'apple':
                        tree[num-1].background_normal = 'pictures/apple.png'

                    elif lst_new[i + 1] == 'peer':
                        tree[num-1].background_normal = 'pictures/peer.png'


class MainScreen(Screen):
    pass


class MenuScreen(Screen):
    pass


class GardenScreen(Screen):
    pass


class WindowManager(ScreenManager):
    pass
