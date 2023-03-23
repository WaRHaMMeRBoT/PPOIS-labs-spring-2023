import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from DataControl import *
from PyQt6.QtCore import *


class AddWindow(QMainWindow):
    submitClicked = pyqtSignal(Tournament)

    def __init__(self, parent=None):
        super(AddWindow, self).__init__(parent)

        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("Добавление турнир")

        self.lable_tournament_name = QLabel(self)
        self.lable_tournament_name.setText('Название турнира: ')

        self.tournament_name_line = QLineEdit(self)
        self.tournament_name_line.move(110, 0)

        self.lable_date = QLabel(self)
        self.lable_date.setText('Дата турнира: ')
        self.lable_date.move(0, 40)

        self.date_edit = QDateEdit(self, calendarPopup=True)
        self.date_edit.dateTimeChanged.connect(self.update)
        self.date_edit.move(110, 40)

        self.lable_sport_name = QLabel(self)
        self.lable_sport_name.setText('Название спорта: ')
        self.lable_sport_name.move(0, 80)

        self.sport_name_line = QLineEdit(self)
        self.sport_name_line.move(110, 80)

        self.lable_winner_name = QLabel(self)
        self.lable_winner_name.setText('Имя победителя: ')
        self.lable_winner_name.move(0, 120)

        self.winner_name_line = QLineEdit(self)
        self.winner_name_line.move(110, 120)

        self.lable_prize_money = QLabel(self)
        self.lable_prize_money.setText('Призовые: ')
        self.lable_prize_money.move(0, 160)

        self.prize_money_line = QLineEdit(self)
        self.prize_money_line.move(110, 160)

        self.button = QPushButton('Добавить турнир', self)
        self.button.resize(120, 40)
        self.button.move(150, 200)
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        tournament = Tournament()
        tournament.tournament_name = self.tournament_name_line.text()
        self.tournament_name_line.clear()
        tournament.date = self.date_edit.date().toPyDate().strftime('%d/%m/%Y')
        self.date_edit.clear()
        tournament.sport_name = self.sport_name_line.text()
        self.sport_name_line.clear()
        tournament.winner_name = self.winner_name_line.text()
        self.winner_name_line.clear()
        tournament.prize_money = int(self.prize_money_line.text())
        self.prize_money_line.clear()
        tournament.set_winner_money()
        self.submitClicked.emit(tournament)
        self.close()


class ViewWindow(QMainWindow):
    def __init__(self, parent=None, tournament_list=[], title=''):
        super(ViewWindow, self).__init__(parent)

        self.setWindowTitle(title)
        self.setFixedSize(QSize(400, 300))

        self.tournaments_list = tournament_list

        self.table = QTableWidget(self)
        self.table_row = 0
        self.table.resize(400, 300)
        self.table.setColumnCount(6)
        self.table.setColumnWidth(1, 70)
        self.table.setRowCount(len(self.tournaments_list))
        self.set_table_data()

    def table_add_item(self, tournament):
        self.table.setItem(self.table_row, 0, QTableWidgetItem(tournament.tournament_name))
        self.table.setItem(self.table_row, 1, QTableWidgetItem(tournament.date))
        self.table.setItem(self.table_row, 2, QTableWidgetItem(tournament.sport_name))
        self.table.setItem(self.table_row, 3, QTableWidgetItem(tournament.winner_name))
        self.table.setItem(self.table_row, 4, QTableWidgetItem(str(tournament.prize_money)))
        self.table.setItem(self.table_row, 5, QTableWidgetItem(str(tournament.winner_money)))
        self.table_row += 1

    def set_table_data(self):
        self.table.setHorizontalHeaderLabels(
            ['Название:', 'Дата:', 'Спорт:', 'Имя победителя:', 'Общие \nпризовые:', 'Призовые \nпобедителю:'])
        for tournament in self.tournaments_list:
            self.table_add_item(tournament)


class RemoveByTournamentNameOrDateWindow(QMainWindow):
    submitClicked = pyqtSignal(list)

    def __init__(self, parent=None, tournament_list=[]):
        super(RemoveByTournamentNameOrDateWindow, self).__init__(parent)

        self.tournaments_list = tournament_list

        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("Удаление турниров")

        self.label1 = QLabel('Название турнира', self)
        self.label1.resize(120, 40)

        self.label2 = QLabel('Дата турнира', self)
        self.label2.resize(120, 40)
        self.label2.move(0, 80)

        self.date_edit = QDateEdit(self, calendarPopup=True)
        self.date_edit.dateTimeChanged.connect(self.update)
        self.date_edit.move(0, 120)

        self.name_line = QLineEdit(self)
        self.name_line.resize(120, 40)
        self.name_line.move(0, 40)

        self.button = QPushButton('Удалить турниры', self)
        self.button.resize(120, 40)
        self.button.move(150, 200)
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        remove_list = []
        for tournament in self.tournaments_list:
            if tournament.tournament_name == self.name_line.text() or \
                    tournament.date == self.date_edit.date().toPyDate().strftime('%#d/%#m/%Y'):
                remove_list.append(tournament)
        self.tournaments_list = [x for x in self.tournaments_list if x not in remove_list]
        self.name_line.clear()
        self.date_edit.clear()
        view = ViewWindow(self, remove_list, 'Удаленные турниры')
        view.show()
        self.submitClicked.emit(self.tournaments_list)
        self.close()


class RemoveByWinnerNameOrSportNameWindow(QMainWindow):
    submitClicked = pyqtSignal(list)

    def __init__(self, parent=None, tournament_list=[]):
        super(RemoveByWinnerNameOrSportNameWindow, self).__init__(parent)

        self.tournaments_list = tournament_list

        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("Удаление турниров")

        self.label1 = QLabel('Название спорта', self)
        self.label1.resize(120, 40)

        self.label2 = QLabel('ФИО победителя', self)
        self.label2.resize(120, 40)
        self.label2.move(0, 80)

        self.sport_name_line = QLineEdit(self)
        self.sport_name_line.resize(120, 40)
        self.sport_name_line.move(0, 40)

        self.winner_name_line = QLineEdit(self)
        self.winner_name_line.resize(120, 40)
        self.winner_name_line.move(0, 120)

        self.button = QPushButton('Удалить турниры', self)
        self.button.resize(120, 40)
        self.button.move(150, 200)
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        remove_list = []
        for tournament in self.tournaments_list:
            if tournament.sport_name == self.sport_name_line.text() or \
                    (self.winner_name_line.text() != '' and -1 != tournament.winner_name.find(
                        self.winner_name_line.text())):
                remove_list.append(tournament)
        self.tournaments_list = [x for x in self.tournaments_list if x not in remove_list]
        self.winner_name_line.clear()
        self.sport_name_line.clear()
        view = ViewWindow(self, remove_list, 'Удаленные турниры')
        view.show()
        self.submitClicked.emit(self.tournaments_list)
        self.close()


class RemoveByWinnerMoneyOrPrizeMoneyWindow(QMainWindow):
    submitClicked = pyqtSignal(list)

    def __init__(self, parent=None, tournament_list=[]):
        super(RemoveByWinnerMoneyOrPrizeMoneyWindow, self).__init__(parent)

        self.tournaments_list = tournament_list

        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("Удаление турниров")

        self.label1 = QLabel('Общие призовые,\nверхний предел', self)
        self.label1.resize(120, 40)

        self.label2 = QLabel('Общие призовые,\nнижний предел', self)
        self.label2.resize(120, 40)
        self.label2.move(0, 80)

        self.label3 = QLabel('Призовые победителю,\nверхний предел', self)
        self.label3.move(150, 0)
        self.label3.resize(130, 40)

        self.label4 = QLabel('Призовые победителю,\nнижний предел', self)
        self.label4.resize(150, 40)
        self.label4.move(150, 80)

        self.prize_money_low_line = QLineEdit(self)
        self.prize_money_low_line.resize(120, 40)
        self.prize_money_low_line.move(0, 120)
        self.prize_money_low_line.setText('0')

        self.prize_money_high_line = QLineEdit(self)
        self.prize_money_high_line.resize(120, 40)
        self.prize_money_high_line.move(0, 40)
        self.prize_money_high_line.setText('0')

        self.winner_money_low_line = QLineEdit(self)
        self.winner_money_low_line.resize(120, 40)
        self.winner_money_low_line.move(150, 120)
        self.winner_money_low_line.setText('0')

        self.winner_money_high_line = QLineEdit(self)
        self.winner_money_high_line.resize(120, 40)
        self.winner_money_high_line.move(150, 40)
        self.winner_money_high_line.setText('0')

        self.button = QPushButton('Удалить турниры', self)
        self.button.resize(120, 40)
        self.button.move(150, 200)
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        remove_list = []
        for tournament in self.tournaments_list:
            if (int(self.prize_money_high_line.text()) >= tournament.prize_money >=
                int(self.prize_money_low_line.text())) or \
                    (int(self.winner_money_high_line.text()) >= tournament.winner_money >=
                     int(self.winner_money_low_line.text())):
                remove_list.append(tournament)
        self.tournaments_list = [x for x in self.tournaments_list if x not in remove_list]
        self.prize_money_low_line.clear()
        self.prize_money_high_line.clear()
        self.winner_money_high_line.clear()
        self.winner_money_low_line.clear()
        view = ViewWindow(self, remove_list, 'Удаленные турниры')
        view.show()
        self.submitClicked.emit(self.tournaments_list)
        self.close()


class FindByTournamentNameOrDateWindow(QMainWindow):
    def __init__(self, parent=None, tournament_list=[]):
        super(FindByTournamentNameOrDateWindow, self).__init__(parent)

        self.tournaments_list = tournament_list

        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("Поиск турниров")

        self.label1 = QLabel('Название турнира', self)
        self.label1.resize(120, 40)

        self.label2 = QLabel('Дата турнира', self)
        self.label2.resize(120, 40)
        self.label2.move(0, 80)

        self.date_edit = QDateEdit(self, calendarPopup=True)
        self.date_edit.dateTimeChanged.connect(self.update)
        self.date_edit.move(0, 120)

        self.name_line = QLineEdit(self)
        self.name_line.resize(120, 40)
        self.name_line.move(0, 40)

        self.button = QPushButton('Найти турниры', self)
        self.button.resize(120, 40)
        self.button.move(150, 200)
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        find_list = []
        for tournament in self.tournaments_list:
            if tournament.tournament_name == self.name_line.text() or \
                    tournament.date == self.date_edit.date().toPyDate().strftime('%#d/%#m/%Y'):
                find_list.append(tournament)
        self.name_line.clear()
        self.date_edit.clear()
        view = ViewWindow(self, find_list, 'Найденные турниры')
        view.show()
        self.close()


class FindByWinnerNameOrSportNameWindow(QMainWindow):
    def __init__(self, parent=None, tournament_list=[]):
        super(FindByWinnerNameOrSportNameWindow, self).__init__(parent)

        self.tournaments_list = tournament_list

        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("Поиск турниров")

        self.label1 = QLabel('Название спорта', self)
        self.label1.resize(120, 40)

        self.label2 = QLabel('ФИО победителя', self)
        self.label2.resize(120, 40)
        self.label2.move(0, 80)

        self.sport_name_line = QLineEdit(self)
        self.sport_name_line.resize(120, 40)
        self.sport_name_line.move(0, 40)

        self.winner_name_line = QLineEdit(self)
        self.winner_name_line.resize(120, 40)
        self.winner_name_line.move(0, 120)

        self.button = QPushButton('Найти турниры', self)
        self.button.resize(120, 40)
        self.button.move(150, 200)
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        find_list = []
        for tournament in self.tournaments_list:
            if tournament.sport_name == self.sport_name_line.text() or \
                    (self.winner_name_line.text() != '' and -1 != tournament.winner_name.find(
                        self.winner_name_line.text())):
                find_list.append(tournament)
        self.winner_name_line.clear()
        self.sport_name_line.clear()
        view = ViewWindow(self, find_list, 'Найденные турниры')
        view.show()
        self.close()


class FindByWinnerMoneyOrPrizeMoneyWindow(QMainWindow):
    def __init__(self, parent=None, tournament_list=[]):
        super(FindByWinnerMoneyOrPrizeMoneyWindow, self).__init__(parent)

        self.tournaments_list = tournament_list

        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("Поиск турниров")

        self.label1 = QLabel('Общие призовые,\nверхний предел', self)
        self.label1.resize(120, 40)

        self.label2 = QLabel('Общие призовые,\nнижний предел', self)
        self.label2.resize(120, 40)
        self.label2.move(0, 80)

        self.label3 = QLabel('Призовые победителю,\nверхний предел', self)
        self.label3.move(150, 0)
        self.label3.resize(130, 40)

        self.label4 = QLabel('Призовые победителю,\nнижний предел', self)
        self.label4.resize(150, 40)
        self.label4.move(150, 80)

        self.prize_money_low_line = QLineEdit(self)
        self.prize_money_low_line.resize(120, 40)
        self.prize_money_low_line.move(0, 120)
        self.prize_money_low_line.setText('0')

        self.prize_money_high_line = QLineEdit(self)
        self.prize_money_high_line.resize(120, 40)
        self.prize_money_high_line.move(0, 40)
        self.prize_money_high_line.setText('0')

        self.winner_money_low_line = QLineEdit(self)
        self.winner_money_low_line.resize(120, 40)
        self.winner_money_low_line.move(150, 120)
        self.winner_money_low_line.setText('0')

        self.winner_money_high_line = QLineEdit(self)
        self.winner_money_high_line.resize(120, 40)
        self.winner_money_high_line.move(150, 40)
        self.winner_money_high_line.setText('0')

        self.button = QPushButton('Найти турниры', self)
        self.button.resize(120, 40)
        self.button.move(150, 200)
        self.button.clicked.connect(self.the_button_was_clicked)

    def the_button_was_clicked(self):
        find_list = []
        for tournament in self.tournaments_list:
            if (int(self.prize_money_high_line.text()) >= tournament.prize_money >=
                int(self.prize_money_low_line.text())) or \
                    (int(self.winner_money_high_line.text()) >= tournament.winner_money >=
                     int(self.winner_money_low_line.text())):
                find_list.append(tournament)
        self.prize_money_low_line.clear()
        self.prize_money_high_line.clear()
        self.winner_money_high_line.clear()
        self.winner_money_low_line.clear()
        view = ViewWindow(self, find_list, 'Найденные турниры')
        view.show()
        self.close()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        size_x = 600
        size_x_2 = int(size_x / 2)
        size_y = 500

        self.setFixedSize(QSize(size_x, size_y))
        self.setWindowTitle("Таблица турниров")

        self.tournaments_list = []
        read(self.tournaments_list)

        self.table = QTableWidget(self)
        self.table_row = 0
        self.table.move(0, 160)
        self.table.resize(size_x, int(size_y/2))
        self.table.setColumnCount(6)
        self.table.setColumnWidth(1, 70)
        self.table.setRowCount(len(self.tournaments_list))
        self.set_table_data()

        self.add_button = QPushButton('Добавить турнир', self)
        self.add_button.resize(120, 40)
        self.add_tournament = AddWindow(self)
        self.add_button.clicked.connect(self.the_add_button_was_clicked)

        self.remove_by_tname_or_date_button = QPushButton('Удалить турниры по названию или дате', self)
        self.remove_by_tname_or_date_button.resize(size_x_2, 40)
        self.remove_by_tname_or_date_button.move(0, 80)
        self.remove_by_tname_tournaments = RemoveByTournamentNameOrDateWindow(self, self.tournaments_list)
        self.remove_by_tname_or_date_button.clicked.connect(self.the_remove_by_tname_or_date_button_was_clicked)

        self.find_by_tname_or_date_button = QPushButton('Найти турниры по названию или дате', self)
        self.find_by_tname_or_date_button.resize(size_x_2, 40)
        self.find_by_tname_or_date_button.move(size_x_2, 80)
        self.find_by_tname_or_date_tournaments = FindByTournamentNameOrDateWindow(self, self.tournaments_list)
        self.find_by_tname_or_date_button.clicked.connect(self.the_find_by_tname_or_date_button_was_clicked)

        self.remove_by_wname_or_sname_button = QPushButton('Удалить турниры по названию спорта\nили имени победителя',
                                                           self)
        self.remove_by_wname_or_sname_button.resize(size_x_2, 40)
        self.remove_by_wname_or_sname_button.move(0, 40)
        self.remove_by_wname_or_sname_tournaments = RemoveByWinnerNameOrSportNameWindow(self, self.tournaments_list)
        self.remove_by_wname_or_sname_button.clicked.connect(self.the_remove_by_wname_or_sname_button_was_clicked)

        self.find_by_wname_or_sname_button = QPushButton('Найти турниры по названию спорта\nили имени победителя',
                                                           self)
        self.find_by_wname_or_sname_button.resize(size_x_2, 40)
        self.find_by_wname_or_sname_button.move(size_x_2, 40)
        self.find_by_wname_or_sname_tournaments = FindByWinnerNameOrSportNameWindow(self, self.tournaments_list)
        self.find_by_wname_or_sname_button.clicked.connect(self.the_find_by_wname_or_sname_button_was_clicked)

        self.remove_by_pmoney_or_wmoney_button = QPushButton(
            'Удалить турниры по общим призовым\nили призовым победителя',
            self)
        self.remove_by_pmoney_or_wmoney_button.resize(size_x_2, 40)
        self.remove_by_pmoney_or_wmoney_button.move(0, 120)
        self.remove_by_pmoney_or_wmoney_tournaments = RemoveByWinnerMoneyOrPrizeMoneyWindow(self, self.tournaments_list)
        self.remove_by_pmoney_or_wmoney_button.clicked.connect(self.the_remove_by_pmoney_or_wmoney_button_was_clicked)

        self.find_by_pmoney_or_wmoney_button = QPushButton(
            'Найти турниры по общим призовым\nили призовым победителя',
            self)
        self.find_by_pmoney_or_wmoney_button.resize(size_x_2, 40)
        self.find_by_pmoney_or_wmoney_button.move(size_x_2, 120)
        self.find_by_pmoney_or_wmoney_tournaments = FindByWinnerMoneyOrPrizeMoneyWindow(self, self.tournaments_list)
        self.find_by_pmoney_or_wmoney_button.clicked.connect(self.the_find_by_pmoney_or_wmoney_button_was_clicked)

        self.add_tournament.submitClicked.connect(self.append_tournament)

        self.remove_by_tname_tournaments.submitClicked.connect(self.remove_tournaments_fun)
        self.remove_by_wname_or_sname_tournaments.submitClicked.connect(self.remove_tournaments_fun)
        self.remove_by_pmoney_or_wmoney_tournaments.submitClicked.connect(self.remove_tournaments_fun)

    def remove_tournaments_fun(self, tournaments_list):
        self.tournaments_list = tournaments_list
        write(self.tournaments_list)
        while self.table.rowCount() > 0:
            self.table.removeRow(0)
        self.table_row = 0
        self.table.setRowCount(len(self.tournaments_list))
        self.set_table_data()

    def the_add_button_was_clicked(self):
        self.add_tournament.show()

    def the_remove_by_tname_or_date_button_was_clicked(self):
        self.remove_by_tname_tournaments.show()

    def the_find_by_tname_or_date_button_was_clicked(self):
        self.find_by_tname_or_date_tournaments.show()

    def the_remove_by_wname_or_sname_button_was_clicked(self):
        self.remove_by_wname_or_sname_tournaments.show()

    def the_find_by_wname_or_sname_button_was_clicked(self):
        self.find_by_wname_or_sname_tournaments.show()

    def the_remove_by_pmoney_or_wmoney_button_was_clicked(self):
        self.remove_by_pmoney_or_wmoney_tournaments.show()

    def the_find_by_pmoney_or_wmoney_button_was_clicked(self):
        self.find_by_pmoney_or_wmoney_tournaments.show()

    def table_add_item(self, tournament):
        self.table.setItem(self.table_row, 0, QTableWidgetItem(tournament.tournament_name))
        self.table.setItem(self.table_row, 1, QTableWidgetItem(tournament.date))
        self.table.setItem(self.table_row, 2, QTableWidgetItem(tournament.sport_name))
        self.table.setItem(self.table_row, 3, QTableWidgetItem(tournament.winner_name))
        self.table.setItem(self.table_row, 4, QTableWidgetItem(str(tournament.prize_money)))
        self.table.setItem(self.table_row, 5, QTableWidgetItem(str(tournament.winner_money)))
        self.table_row += 1

    def append_tournament(self, tournament):
        self.tournaments_list.append(tournament)
        self.table.insertRow(self.table_row)
        self.table_add_item(tournament)
        write(self.tournaments_list)

    def set_table_data(self):
        self.table.setHorizontalHeaderLabels(
            ['Название:', 'Дата:', 'Спорт:', 'Имя победителя:', 'Общие \nпризовые:', 'Призовые \nпобедителю:'])
        for tournament in self.tournaments_list:
            self.table_add_item(tournament)
