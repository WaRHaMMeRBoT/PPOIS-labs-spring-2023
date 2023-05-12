class Controller:
    def __init__(self, model):
        self.model = model

    def setView(self, view):
        self.view = view

    def add_garden_bed(self, status):
        if self.model.garden_bed_kol() >= 7:
            status.text = 'Не хватает места для грядок'
        else:
            st = self.model.add_garden_bed()
            status.text = st
        self.view.update_data()

    def get_data_from_file(self):
        self.model.get_data_from_file()
        self.view.update_data()

    def set_data_in_file(self, status):
        self.model.set_data_in_file()
        status.text = 'Сохранено в файле data.json'

    def plant_tree(self, tree_name, status):
        if tree_name.text == '>':
            status.text = 'Выберите дерево из списка'
        else:
            if self.model.tree_kol() < 5:
                st = self.model.plant_tree(tree_name.text)
                status.text = st
            else:
                status.text = 'Не хватает места для деревьев'

        self.view.update_data()

    def next_day(self, status):
        status.text = 'Наступил следующий день'
        self.model.next_day()
        self.view.update_data()

    def watering(self, num, status):
        if num.text == '':
            status.text = 'Введите номер грядки для полива'
        else:
            st = self.model.watering(int(num.text) - 1)
            status.text = st
        self.view.update_data()

    def weeding(self, num, status):
        if num.text == '':
            status.text = 'Введите номер грядки для прополки'
        else:
            st = self.model.weeding(int(num.text) - 1)
            status.text = st
        self.view.update_data()

    def fertilize(self, num, status):
        if num.text == '':
            status.text = 'Введите номер грядки для добавления удобрения'
        else:
            st = self.model.fertilize(int(num.text) - 1)
            status.text = st
        self.view.update_data()

    def plant_cultivated_plant(self, cultivated_plant_name, num, status):
        if cultivated_plant_name.text == '>':
            status.text = 'Выберите растение для посадки'
        elif num.text == '':
            status.text = 'Введите номер грядки для посадки растения'
        else:
            st = self.model.plant_cultivated_plant(cultivated_plant_name.text, int(num.text) - 1)
            status.text = st
        self.view.update_data()

    def kill_pest(self, type_herb, num, status):
        if type_herb.text == '>':
            status.text = 'Выберите тип растение для обработки'
        elif num.text == '':
            status.text = 'Введите номер растения для обработки'
        else:
            st = self.model.kill_pest(type_herb.text, int(num.text) - 1)
            status.text = st
        self.view.update_data()

    def treatment(self, type_herb, num, status):
        if type_herb.text == '>':
            status.text = 'Выберите тип растение для лечения'
        elif num.text == '':
            status.text = 'Введите номер растения для лечения'
        else:
            st = self.model.treatment(type_herb.text, int(num.text) - 1)
            status.text = st
        self.view.update_data()

    def harvesting(self, type_herb, num, status):
        if type_herb.text == '>':
            status.text = 'Выберите тип растение для сбора урожая'
        elif num.text == '':
            status.text = 'Введите номер растения для сбора урожая'
        else:
            st = self.model.harvesting(type_herb.text, int(num.text) - 1)
            status.text = st
        self.view.update_data()


