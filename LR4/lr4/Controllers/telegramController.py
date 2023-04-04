import datetime
import time

from telebot.apihelper import ApiTelegramException

from lr4.Controllers.baseController import BaseController

import telebot as tb

from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from lr4.garden.model import create_dir


def init():
    create_dir(10, 5)


class TelegramController:
    def __init__(self, token):
        self.restricted_users = []
        self.bot = tb.TeleBot(token)
        init()
        self.controller = BaseController()
        self.plant = ""
        self.message_times = {}
        self.interval = 1
        self.counter = 0
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
        get = KeyboardButton(text="Получить информацию о растении")
        buttons.add(view, warp, weather, delete, add, get)
        self.bot.send_message(message.chat.id, "Список доступных команд", reply_markup=buttons)

    def weather_menu(self, message):
        buttons = ReplyKeyboardMarkup(resize_keyboard=True)
        clear = KeyboardButton(text="Ясно")
        sunny = KeyboardButton(text="Солнечно")
        rainy = KeyboardButton(text="Дождь")
        buttons.add(clear, sunny, rainy)
        self.bot.send_message(message.chat.id, "Вот доступные виды погод:", reply_markup=buttons)
        self.bot.register_next_step_handler(message, self.weather_changer)

    def warping(self, message):
        try:
            if int(message.text) < 100:
                self.controller.warp(time=int(message.text))
                self.bot.send_message(message.chat.id, "Перемещение произведено на " + message.text + " итераций")
            else:
                raise
        except Exception:
            self.bot.send_message(message.chat.id, "Ты что, Глебаш?")

    def weather_changer(self, message):
        match message.text:
            case "Ясно":
                self.controller.weather("clear", 100)
            case "Солнечно":
                self.controller.weather("sunny", 100)
            case "Дождь":
                self.controller.weather("rainy", 100)
        self.bot.send_message(message.chat.id, "Погода изменена на " + message.text)
        self.help(message)

    def delete_plant(self, message):
        pos = str(message.text).split()
        try:
            self.controller.remove(int(pos[0]), int(pos[1]))
            self.bot.send_message(message.chat.id, "Сущность удалена")
        except IndexError:
            self.bot.send_message(message.chat.id, "Задал значения которые превышают размер сетки? А ты хорош...")
        except Exception:
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
        self.bot.register_next_step_handler(message, self.get_plant_id)

    def get_plant_id(self, message):
        try:
            self.plant = self.plants[message.text]
            self.bot.send_message(message.chat.id, "Введите значение: x y")
            self.bot.register_next_step_handler(message, self.add_plant)
        except KeyError:
            self.bot.send_message(message.chat.id, "Ну ты конечно мда")
            self.help(message)

    def add_plant(self, message):
        pos = str(message.text).split()
        try:
            self.controller.add_seed(self.plant, int(pos[0]), int(pos[1]))
            self.bot.send_message(message.chat.id, "Сущность добавлена")
        except IndexError:
            self.bot.send_message(message.chat.id, "Задал значения которые превышают размер сетки? А ты хорош...")
        except Exception:
            self.bot.send_message(message.chat.id, "Глебаш, давай нормально...")
        self.help(message)

    def get_plant(self, message):
        self.bot.send_message(message.chat.id, "Введите x y:")
        self.bot.register_next_step_handler(message, self.get_plant_by_x_y)

    def get_plant_by_x_y(self, message):
        pos = str(message.text).split()

        try:
            plant = self.controller.get_plants()[int(pos[0])][int(pos[1])]
            if plant:
                self.bot.send_message(message.chat.id, plant)
            else:
                self.bot.send_message(message.chat.id, "Эта клетка пуста")
        except IndexError:
            self.bot.send_message(message.chat.id, "Ну ты выдал базу канеш, ну держи пустоту")
        except Exception:
            self.bot.send_message(message.chat.id, "Произошла непонятность")

    def handle_message(self, message):

        user_id = message.from_user.id

        current_time = time.time()

        previous_time = self.message_times.get(user_id, None)

        print(self.restricted_users)
        if previous_time and (current_time - previous_time) < self.interval:
            self.restricted_users.append(user_id)
            self.bot.send_message(message.chat.id, "Ну ты и клоун, тебя забанили!")
        else:
            self.message_times[user_id] = current_time

            match message.text:
                case "Просмотреть огород":
                    self.bot.send_message(chat_id=message.chat.id, text=self.controller.view())
                case "Перемещение во времени":
                    self.bot.send_message(message.chat.id, "Введите значение:")
                    self.bot.register_next_step_handler(message, self.warping)
                case "Поменять погоду":
                    self.weather_menu(message)
                case "Удалить растение":
                    self.bot.send_message(message.chat.id, "Введите значение: x y")
                    self.bot.register_next_step_handler(message, self.delete_plant)
                case "Добавить растение":
                    self.add_plant_menu(message)
                case "Получить информацию о растении":
                    self.get_plant(message)
            self.message_times[user_id] = time.time()
            print(self.counter)
            self.counter += 1
            if self.counter % 10 == 0:
                self.bot.send_message(message.chat.id,
                                      "Текущая погода: " + self.controller.garden.model.weather.weather)
            self.counter = 0

    def run(self):
        @self.bot.message_handler(commands=['start'])
        def handle_start(message):
            self.start(message)
            self.counter += 1

        @self.bot.message_handler(commands=['commands'])
        def handle_help(message):
            self.help(message)
            self.counter += 1

        @self.bot.message_handler(func=lambda message: True and message.from_user.id not in self.restricted_users)
        def handle_message(message):
            self.handle_message(message)

        @self.bot.message_handler(func=lambda message: True and message.from_user.id in self.restricted_users)
        def banned_message(message):
            self.bot.send_message(message.chat.id, "тебя забанили!")
            current_time = time.time()
            try:
                index = self.restricted_users.index(message.chat.id)
                previous_time = self.message_times.get(self.restricted_users[index], None)
                if previous_time and (current_time - previous_time) > self.interval:
                    self.restricted_users.remove(message.from_user.id)
            except Exception:
                print("ой")

        self.bot.polling()


def app():
    telegram = TelegramController("5629086421:AAHmbwjKCpyVJptr-c_-3KHQezWOiQXLSxM")
    telegram.run()


if __name__ == '__main__':
    app()
