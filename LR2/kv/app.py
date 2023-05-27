import pandas as pd
import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.screenmanager import MDScreenManager
from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRectangleFlatButton


class AppMainScreen(MDScreen):
    pass


class ScreenManager(MDScreenManager):
    pass


class AllProductScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = pd.read_csv("/Users/vanek/Documents/BSUIR/Labs /PPOIS/Sem_2/Kira/PPOIS/LR2/dataframe")
        # self.data = data

        self.table = MDDataTable(
            size_hint=(0.9, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            column_data=[
                ("Name product", dp(30)),
                ("manufacturers name", dp(30)),
                ("manufacturer unp", dp(30)),
                ("quantity in stock", dp(30)),
                ("stock address", dp(30)),
            ],
            use_pagination=True,
            row_data=data.values.tolist(),
        )
        self.add_widget(self.table)

    def update_table(self):
        self.table.row_data = pd.read_csv("/Users/vanek/Documents/BSUIR/Labs /PPOIS/Sem_2/Kira/PPOIS/LR2/dataframe").values.tolist()


class FindProductScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        data = pd.read_csv("/Users/vanek/Documents/BSUIR/Labs /PPOIS/Sem_2/Kira/PPOIS/LR2/dataframe")
        self.data = data
        self.table = MDDataTable(
            size_hint=(0.9, 0.6),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            column_data=[
                ("Name product", dp(30)),
                ("manufacturers name", dp(30)),
                ("manufacturer unp", dp(30)),
                ("quantity in stock", dp(30)),
                ("stock address", dp(30)),
            ],
            use_pagination=True,
            row_data=self.data.values.tolist(),
        )

        self.add_widget(self.table)
        self.filter_options = dict()
        self.filter_options_int = dict()

    def update_table(self):
        self.data = pd.read_csv("/Users/vanek/Documents/BSUIR/Labs /PPOIS/Sem_2/Kira/PPOIS/LR2/dataframe")
        self.table.row_data = pd.read_csv("/Users/vanek/Documents/BSUIR/Labs /PPOIS/Sem_2/Kira/PPOIS/LR2/dataframe").values.tolist()

    def df_filter_text(self, df: pd.DataFrame):
        table_data = df.copy()
        for key, val in self.filter_options.items():
            table_data = table_data[table_data[key].str.contains(val)]
        return table_data

    def df_filter_int(self, df: pd.DataFrame):
        table_data = df.copy()
        for key, val in self.filter_options_int.items():
            if val != '':
                table_data = table_data[table_data[key] == int(val)]
        return table_data

    def filter(self):
        self.filter_options['product_name'] = self.ids.product_name.text
        self.filter_options['manufacturers_name'] = self.ids.manufacturers_name.text
        self.filter_options['manufacturer_unp'] = self.ids.manufacturer_unp.text
        self.filter_options['stock_address'] = self.ids.stock_address.text
        self.filter_options_int['quantity_in_stock'] = self.ids.quantity_in_stock.text
        table_data = self.df_filter_text(self.data)
        table_data = self.df_filter_int(table_data)
        self.table.row_data = table_data.values.tolist()


class AddProductScreen(MDScreen):
    def __init__(self, **kwargs):
        super(AddProductScreen, self).__init__(**kwargs)
        self.dialog = None

    def save_data(self, product_info: dict):
        df = pd.read_csv('/Users/vanek/Documents/BSUIR/Labs /PPOIS/Sem_2/Kira/PPOIS/LR2/dataframe')
        if product_info['stock_address'] == '':
            product_info['stock_address'] = 'Нет адреса'
        tmp = pd.DataFrame([product_info], index=None)
        df = pd.concat([df, tmp])

        with open('/Users/vanek/Documents/BSUIR/Labs /PPOIS/Sem_2/Kira/PPOIS/LR2/dataframe', 'w') as f:
            df.to_csv(f, index=False)

        App.get_running_app().root.get_screen('all_product').update_table()
        App.get_running_app().root.get_screen('find_product').update_table()
        App.get_running_app().root.get_screen('delete_product').update_table()

    def send_add_data(self):
        product_info = dict()
        product_info['product_name'] = self.ids.product_name.text
        product_info['manufacturers_name'] = self.ids.manufacturers_name.text
        product_info['manufacturer_unp'] = self.ids.manufacturer_unp.text
        product_info['quantity_in_stock'] = self.ids.quantity_in_stock.text
        product_info['stock_address'] = self.ids.stock_address.text
        if product_info['product_name'] in ('', None):
            self.validation_dialog("Название товара - обязательный параметр")
            return
        if product_info['manufacturers_name'] in ('', None):
            self.validation_dialog("Производитель - обязательный параметр")
            return
        if product_info['manufacturer_unp'] in ('', None):
            self.validation_dialog("УНП - обязательный параметр")
            return
        if product_info['quantity_in_stock'] in ('', None):
            self.validation_dialog("Количество на складе - обязательный параметр")
            return

        if len(product_info['product_name']) <= 2 or len(product_info['product_name']) >= 50:
            self.validation_dialog("Название продукта должна содержать от 2 до 50 символов")
            return
        elif len(product_info['manufacturer_unp']) <= 6 and len(product_info['manufacturers_name']) >= 9:
            self.validation_dialog("Унп производтеля должен быть от 100.000-999.999.999")
            return
        elif len(product_info['manufacturers_name']) <= 4 or len(product_info['manufacturers_name']) >= 30:
            self.validation_dialog("Название производтеля должна содержать от 4 до 30 символов")
            return
        elif len(product_info['manufacturers_name']) <= 4 or len(product_info['manufacturers_name']) >= 30:
            self.validation_dialog("Название производтеля должна содержать от 4 до 30 символов")
            return
        elif int(product_info['quantity_in_stock']) < 0:
            self.validation_dialog("На складе должно быть больше 0 товара")
            return

        self.save_data(product_info)
        self.validation_dialog("Добавлено!")

    def validation_dialog(self, text: str):
        self.dialog = MDDialog(
            title=text,
            buttons=[MDRectangleFlatButton(
                text="Понятно",
                on_release=self.close_dialog
            )
            ]
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


class DeleteProductScreen(FindProductScreen):
    def __init__(self, **kwargs):
        super(DeleteProductScreen, self).__init__(**kwargs)
        self.dialog = None

    def delete(self):
        self.dialog = MDDialog(
            title=f'Вы действительно хотите удалить {len(self.table.row_data)} запись(и/ей)',
            buttons=[
                MDRectangleFlatButton(
                    text='Нет',
                    on_release=self.close_dialog
                ),
                MDRectangleFlatButton(
                    text='Да',
                    on_release=self.final_delete
                )
            ]
        )
        self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()

    def save_data(self, rows_to_delete: list):
        df = pd.read_csv('/Users/vanek/Documents/BSUIR/Labs /PPOIS/Sem_2/Kira/PPOIS/LR2/dataframe')
        for row in rows_to_delete:
            df = df.loc[~(
                        (df['product_name'] == row[0]) & (df['manufacturers_name'] == row[1]) & (df['manufacturer_unp'] == row[2]) & (
                            df['quantity_in_stock'] == row[3]) & (df['stock_address'] == row[4]))]

        with open('/Users/vanek/Documents/BSUIR/Labs /PPOIS/Sem_2/Kira/PPOIS/LR2/dataframe', 'w') as f:
            df.to_csv(f, index=False)

        App.get_running_app().root.get_screen('all_product').update_table()
        App.get_running_app().root.get_screen('find_product').update_table()
        App.get_running_app().root.get_screen('delete_product').update_table()
        # self.table.row_data = df.copy().values.tolist()

        # self.update_table()

    def final_delete(self, obj):
        self.dialog.dismiss()
        delete = len(self.table.row_data)
        self.save_data(self.table.row_data)
        self.dialog = MDDialog(
            title=f'Успешно удалена(ы) {delete} запись(и/ей)',
            buttons=[
                MDRectangleFlatButton(
                    text='Хорошо',
                    on_release=self.close_dialog
                ),
            ]
        )
        self.dialog.open()


class ProductApp(MDApp):
    def build(self):
        # self.theme_cls.primary_palette = "Indigo"
        Builder.load_file("kv/product")
        Builder.load_file("kv/all_product")
        Builder.load_file("kv/find_product")
        Builder.load_file('kv/add_product')
        Builder.load_file('kv/delete_product')
        screen_manager = ScreenManager()
        screen_manager.add_widget(AppMainScreen(name='main'))
        my_all_product_screen_instance = AllProductScreen(name='all_product')
        screen_manager.add_widget(my_all_product_screen_instance)
        screen_manager.add_widget(FindProductScreen(name='find_product'))
        screen_manager.add_widget(AddProductScreen(name='add_product'))
        screen_manager.add_widget(DeleteProductScreen(name='delete_product'))


        return screen_manager
