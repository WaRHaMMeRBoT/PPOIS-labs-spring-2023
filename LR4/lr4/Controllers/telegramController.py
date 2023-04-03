from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from lr4.Controllers.baseController import BaseController

import telebot

from lr4.garden.model import create_dir


def init():
    create_dir(10, 5)


class TelegramController:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        init()
        self.controller = BaseController()
        self.warp = False
        self.weather = False
        self.delete = False
        self.add = False
        self.plant_add = False
        self.plant = ""

        self.plants = {
            "Помидор": "tomato",
            "Морковка": "carrot",
            "Картошка": "potato",
            "Огурчик": "cucumber",
            "Кабачок": "zucchini",
            "Сорняк": "weed"
        }

    def start(self, message):
        self.bot.send_message(message.chat.id, "Привет! Я бот!")

    def help(self, message):
        buttons = ReplyKeyboardMarkup(resize_keyboard=True)
        view = KeyboardButton(text="Просмотреть огород")
        warp = KeyboardButton(text="Перемещение во времени")
        weather = KeyboardButton(text="Поменять погоду")
        delete = KeyboardButton(text="Удалить растение")
        add = KeyboardButton(text="Добавить растение")
        buttons.add(view, warp, weather, delete, add)
        self.bot.send_message(message.chat.id, "Список доступных команд", reply_markup=buttons)

    def weather_menu(self, message):
        buttons = ReplyKeyboardMarkup(resize_keyboard=True)
        clear = KeyboardButton(text="Ясно")
        sunny = KeyboardButton(text="Солнечно")
        rainy = KeyboardButton(text="Дождь")
        buttons.add(clear, sunny, rainy)
        self.bot.send_message(message.chat.id, "Вот доступные виды погод:", reply_markup=buttons)
        self.weather = True

    def warping(self, message):
        if str(message.text).isdigit():
            if 0 < int(message.text) <= 100:
                self.controller.warp(time=int(message.text))
                self.bot.send_message(message.chat.id, "Перемещение произведено на " + message.text + " итераций")
            else:
                self.bot.send_message(message.chat.id, "Ты что, Глебаш?")
            self.warp = False
        else:
            self.bot.send_message(message.chat.id, "Неправильный ввод")

    def weather_changer(self, message):
        match message.text:
            case "Ясно":
                self.controller.weather("clear", 100)
            case "Солнечно":
                self.controller.weather("sunny", 100)
            case "Дождь":
                self.controller.weather("rainy", 100)
        self.bot.send_message(message.chat.id, "Погода изменена на " + message.text)
        self.weather = False

    def delete_plant(self, message):
        pos = str(message.text).split()
        if len(pos) > 1 and pos[0].isdigit() and pos[1].isdigit():
            if len(self.controller.garden.model.matrix) > int(pos[0]) >= 0 and len(
                    self.controller.garden.model.matrix[0]) > int(pos[1]) >= 0:
                self.controller.remove(int(pos[0]), int(pos[1]))
                self.bot.send_message(message.chat.id, "Сущность удалена")
            else:
                self.bot.send_message(message.chat.id, "Ну ты конечно out of bounds...")
        else:
            self.bot.send_message(message.chat.id, "Глебаш, давай нормально...")

    def add_plant_menu(self, message):
        buttons = ReplyKeyboardMarkup(resize_keyboard=True)
        tomato = KeyboardButton(text="Помидор")
        carrot = KeyboardButton(text="Морковка")
        potato = KeyboardButton(text="Картошка")
        weed = KeyboardButton(text="Сорняк")
        cucumber = KeyboardButton(text="Огурчик")
        zucchini = KeyboardButton(text="Кабачок")
        buttons.add(tomato, carrot, potato, cucumber, zucchini, weed)
        self.bot.send_message(message.chat.id, "Выберите тип растения:", reply_markup=buttons)
        self.add = True

    def get_plant_id(self, message):
        if len(str(message.text).split()) == 1 and not message.text.isdigit():
            if message.text in self.plants:
                self.plant = self.plants[message.text]
                self.plant_add = True
                self.bot.send_message(message.chat.id, "Введите значение: x y")
            else:
                self.bot.send_message(message.chat.id, "Ну ты конечно мда")
        else:
            self.bot.send_message(message.chat.id, "Совсем клоун?")

    def add_plant(self, message):
        pos = str(message.text).split()

        if len(pos) > 1 and pos[0].isdigit() and pos[1].isdigit():
            if len(self.controller.garden.model.matrix) > int(pos[0]) >= 0 and len(
                    self.controller.garden.model.matrix[0]) > int(pos[1]) >= 0:
                self.controller.add_seed(self.plant, int(pos[0]), int(pos[1]))
                self.bot.send_message(message.chat.id, "Сущность добавлена")
        else:
            self.bot.send_message(message.chat.id, "Ну ты конечно крутой...")

    def handle_message(self, message):
        if self.warp:
            self.warping(message)

        elif self.weather:
            self.weather_changer(message)

        elif self.add:
            self.get_plant_id(message)
            self.add = False

        elif self.plant_add:
            self.add_plant(message)
            self.plant_add = False

        elif self.delete:
            self.delete_plant(message)
            self.delete = False
        else:
            match message.text:
                case "Просмотреть огород":
                    self.bot.send_message(message.chat.id, self.controller.view())
                case "Перемещение во времени":
                    self.bot.send_message(message.chat.id, "Введите значение:")
                    self.warp = True
                case "Поменять погоду":
                    self.weather_menu(message)
                case "Удалить растение":
                    self.bot.send_message(message.chat.id, "Введите значение: x y")
                    self.delete = True
                case "Добавить растение":
                    self.add_plant_menu(message)

    def run(self):
        @self.bot.message_handler(commands=['start'])
        def handle_start(message):
            self.start(message)

        @self.bot.message_handler(commands=['commands'])
        def handle_help(message):
            self.help(message)

        @self.bot.message_handler(func=lambda message: True)
        def handle_message(message):
            self.handle_message(message)

        self.bot.polling()


def app():
    telegram = TelegramController("5629086421:AAHmbwjKCpyVJptr-c_-3KHQezWOiQXLSxM")
    telegram.run()


if __name__ == '__main__':
    app()
