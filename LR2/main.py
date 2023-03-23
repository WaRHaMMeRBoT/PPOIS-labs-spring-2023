import datetime
import random

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import Qt

import Tournament
from Tournament import *
import sys
import json
import App
from DataControl import *


def main():
    """l = []
    sp = ['Баскетбол', 'Бейсбол', 'Бокс', 'Борьба вольная', 'Борьба греко-римская', 'Велосипедный спорт', 'Водное поло',
          'Волейбол', 'Волейбол пляжный',
          'Гандбол', 'Гимнастика спортивная', 'Гимнастика художественная', 'Гребля академическая', 'Плавание',
          'Легкая атлетика',
          'Дзюдо', 'Конный спорт']
    name = ['Александр', 'Дмитрий', 'Максим', 'Сергей', 'Андрей', 'Алексей', 'Артём', 'Илья', 'Кирилл', 'Михаил',
            'Никита', 'Матвей', 'Роман', 'Егор', 'Арсений', 'Иван',
            'Денис', 'Евгений', 'Даниил', 'Тимофей', 'Владислав']
    surn = ['Смирнов', 'Иванов', 'Кузнецов', 'Соколов', 'Попов', 'Лебедев', 'Козлов', 'Новиков', 'Морозов', 'Петров',
            'Волков', 'Соловьёв', 'Васильев', 'Зайцев', 'Павлов',
            'Семёнов', 'Голубев', 'Виноградов', 'Богданов', 'Воробьёв', 'Фёдоров', 'Михайлов', 'Беляев']
    for i in range(101):
        t = Tournament()
        a = random.randint(0, len(sp)-1)
        t.tournament_name = 'Турнир по ' + sp[a]
        t.sport_name = sp[a]
        t.prize_money = random.randint(10, 500)
        t.set_winner_money()
        t.date = '{}/{}/{}'.format(str(random.randint(0, 30)), str(random.randint(1, 12)),
                                   str(random.randint(2000, 2002)))
        t.winner_name = name[random.randint(0, len(name)-1)] + ' ' + surn[random.randint(0, len(surn)-1)]
        l.append(t)
    write(l)"""

    app = QApplication(sys.argv)

    window = App.MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()
