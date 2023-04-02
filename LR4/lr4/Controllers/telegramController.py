from telebot.types import ReplyKeyboardMarkup, KeyboardButton

from lr4.Controllers.baseController import BaseController

import telebot


class TelegramController:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.controller = BaseController()
        self.warp = False
        self.delete_or_add = False

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

    def handle_message(self, message):
        if self.warp:
            if str(message.text).isdigit():
                self.controller.warp(time=int(message.text))
                self.bot.send_message(message.chat.id, "Перемещение произведено на " + message.text + " итераций")
                self.warp = False
            else:
                self.bot.send_message(message.chat.id, "Неправильный ввод")
        match message.text:
            case "Просмотреть огород":
                self.bot.send_message(message.chat.id, self.controller.view())
            case "Перемещение во времени":
                self.bot.send_message(message.chat.id, "Введите значение:")
                self.warp = True

    def run(self):
        @self.bot.message_handler(commands=['start'])
        def handle_start(message):
            self.start(message)

        @self.bot.message_handler(commands=['help'])
        def handle_help(message):
            self.help(message)

        @self.bot.message_handler(func=lambda message: True)
        def handle_message(message):
            self.handle_message(message)

        self.bot.polling()


if __name__ == '__main__':
    telegram = TelegramController("5629086421:AAHmbwjKCpyVJptr-c_-3KHQezWOiQXLSxM")
    telegram.run()
